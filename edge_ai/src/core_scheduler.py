# ==============================================================================
# PERLACOLABS - EDGE OS KERNEL v3.5 — STR-002 H3
# Inferencia YOLOv8-FDA + Control VRA con Lazo Cerrado de Caudalímetro
# Companion Computer: Raspberry Pi 4 / Jetson Nano
# ==============================================================================
# Hilos:
#   1. thread_yolo_vision    — Inferencia YOLOv8 (producción o simulación)
#   2. thread_mavlink_bridge — Comandos PWM al flight controller
#   3. thread_flowmeter_fb   — Retroalimentación GPIO del YF-S201
#   4. thread_watchdog       — Health-check de todos los hilos
# ==============================================================================

import time
import threading
import queue
import os
import logging
import signal

try:
    from pymavlink import mavutil
except ImportError:
    mavutil = None

# Configuración vía entorno
UART_PORT = os.environ.get('PERLACO_UART_PORT', '/dev/ttyAMA0')
UART_BAUD = int(os.environ.get('PERLACO_UART_BAUD', '115200'))
SERVO_CHANNEL = int(os.environ.get('PERLACO_SERVO_CH', '9'))
FLOWMETER_GPIO = int(os.environ.get('PERLACO_FLOW_GPIO', '17'))

FLOW_PUMP_PWM_MIN = 1000
FLOW_PUMP_PWM_MAX = 2000
FLOW_PID_KP = 0.15
FLOW_PID_KI = 0.02
FLOW_PID_KD = 0.01
FLOW_PID_IMAX = 150

WATCHDOG_TIMEOUT_S = 3.0

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger('EdgeOS')


class FlowPIDController:
    """Controlador PID de caudal con retroalimentación YF-S201."""

    def __init__(self, kp=FLOW_PID_KP, ki=FLOW_PID_KI, kd=FLOW_PID_KD):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0.0
        self.prev_error = 0.0
        self.last_time = time.time()

    def compute(self, setpoint_lmin, measured_lmin):
        now = time.time()
        dt = now - self.last_time
        if dt <= 0:
            dt = 0.01
        self.last_time = now
        error = setpoint_lmin - measured_lmin
        p_term = self.kp * error
        self.integral += self.ki * error * dt
        self.integral = max(-FLOW_PID_IMAX, min(FLOW_PID_IMAX, self.integral))
        i_term = self.integral
        d_term = self.kd * (error - self.prev_error) / dt
        self.prev_error = error
        return p_term + i_term + d_term


class EdgeOSKernel:
    """Kernel de Borde STR-002 H3 v3.5."""

    def __init__(self, uart_port=UART_PORT, baudrate=UART_BAUD):
        self.stop_event = threading.Event()
        self.q_telemetry = queue.Queue(maxsize=50)
        self.q_flow_feedback = queue.Queue(maxsize=20)
        self.uart_port = uart_port
        self.baudrate = baudrate
        self.mav_connection = None
        self.flow_pid = FlowPIDController()
        self.current_pwm = 1500
        self.thread_timestamps = {}
        self.watchdog_alert = False
        self.pulse_count = 0
        self.flow_rate_lmin = 0.0
        self.flowmeter_available = False
        self._pulse_lock = threading.Lock()

    def inicializar_enlace_uart(self):
        if not mavutil:
            logger.warning("pymavlink no instalado — simulacion completa")
            self.mav_connection = None
            return
        try:
            logger.info("Conectando a Cube Orange+ en %s @ %d baud...", self.uart_port, self.baudrate)
            self.mav_connection = mavutil.mavlink_connection(self.uart_port, baud=self.baudrate)
            self.mav_connection.wait_heartbeat(timeout=3)
            logger.info("Enlace MAVLink establecido")
        except Exception as e:
            logger.warning("Sin conexion UART (%s). Simulacion local.", e)
            self.mav_connection = None

    def inicializar_caudalimetro_gpio(self):
        try:
            import RPi.GPIO as GPIO
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(FLOWMETER_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            def pulse_callback(channel):
                with self._pulse_lock:
                    self.pulse_count += 1
            GPIO.add_event_detect(FLOWMETER_GPIO, GPIO.FALLING, callback=pulse_callback)
            self.flowmeter_available = True
            logger.info("Caudalimetro YF-S201 en GPIO%d", FLOWMETER_GPIO)
        except ImportError:
            logger.warning("RPi.GPIO no disponible — caudal en simulacion")
            self.flowmeter_available = False
        except Exception as e:
            logger.warning("Error GPIO: %s — simulacion activa", e)
            self.flowmeter_available = False

    def leer_caudal_gpio(self):
        FLOWMETER_K_FACTOR = 450
        with self._pulse_lock:
            pulses = self.pulse_count
            self.pulse_count = 0
        if pulses > 0:
            liters = pulses / FLOWMETER_K_FACTOR
            self.flow_rate_lmin = liters * 60.0
        else:
            self.flow_rate_lmin *= 0.9
        return self.flow_rate_lmin

    def thread_yolo_vision(self):
        model = None
        cap = None
        try:
            from ultralytics import YOLO
            model = YOLO('yolov8n-fda.pt')
            logger.info("Modelo YOLOv8-FDA cargado — inferencia REAL")
        except ImportError:
            logger.warning("ultralytics no instalado — simulacion YOLO")
        except Exception as e:
            logger.warning("Modelo YOLOv8: %s — simulacion", e)
        if model:
            try:
                import cv2
                cap = cv2.VideoCapture(0)
                if not cap.isOpened():
                    cap = None
            except ImportError:
                pass
        logger.info("Hilo YOLOv8-FDA iniciado (19.2 FPS target)")
        while not self.stop_event.is_set():
            self.thread_timestamps['vision'] = time.time()
            inicio = time.time()
            if model and cap:
                ret, frame = cap.read()
                if ret:
                    results = model(frame, imgsz=640, conf=0.5, verbose=False)
                    dosis_pwm = 1500
                    confianza = float(results[0].boxes.conf.mean()) if len(results[0].boxes) > 0 else 0.0
                else:
                    dosis_pwm = 1500
                    confianza = 0.0
            else:
                time.sleep(0.052)
                import math
                dosis_pwm = 1500 + int(100 * math.sin(time.time() * 0.5))
                confianza = 0.94
            datos_frame = {
                'timestamp': time.time(),
                'dosis_pwm_setpoint': dosis_pwm,
                'confianza': confianza
            }
            if not self.q_telemetry.full():
                self.q_telemetry.put(datos_frame)
            duracion = time.time() - inicio
            if duracion < 1.0 / 19.2:
                time.sleep(1.0 / 19.2 - duracion)

    def thread_flowmeter_feedback(self):
        logger.info("Hilo retroalimentacion caudalimetro iniciado")
        while not self.stop_event.is_set():
            self.thread_timestamps['flowmeter'] = time.time()
            if self.flowmeter_available:
                measured = self.leer_caudal_gpio()
            else:
                import random
                pwm_range = self.current_pwm - 1000
                measured = (pwm_range / 1000.0) * 8.0 * (0.9 + 0.2 * random.random())
            if not self.q_flow_feedback.full():
                self.q_flow_feedback.put(measured)
            time.sleep(1.0)

    def thread_mavlink_bridge(self):
        logger.info("Puente MAVLink iniciado")
        while not self.stop_event.is_set():
            self.thread_timestamps['mavlink'] = time.time()
            try:
                paquete = self.q_telemetry.get(timeout=0.1)
                pwm_setpoint = paquete['dosis_pwm_setpoint']
                measured_lmin = None
                try:
                    measured_lmin = self.q_flow_feedback.get_nowait()
                except queue.Empty:
                    pass
                if measured_lmin is not None:
                    expected_lmin = ((pwm_setpoint - 1000) / 1000.0) * 8.0
                    pwm_adjust = self.flow_pid.compute(expected_lmin, measured_lmin)
                    pwm_final = pwm_setpoint + int(pwm_adjust)
                else:
                    pwm_final = pwm_setpoint
                pwm_final = max(FLOW_PUMP_PWM_MIN, min(FLOW_PUMP_PWM_MAX, pwm_final))
                self.current_pwm = pwm_final
                if self.mav_connection:
                    self.mav_connection.mav.command_long_send(
                        self.mav_connection.target_system,
                        self.mav_connection.target_component,
                        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
                        0, SERVO_CHANNEL, pwm_final, 0, 0, 0, 0, 0
                    )
                else:
                    logger.debug("[Sim] PWM Bomba VRA: %d us | Caudal: %.2f L/min",
                               pwm_final, measured_lmin or 0)
                self.q_telemetry.task_done()
            except queue.Empty:
                continue

    def thread_watchdog(self):
        logger.info("Watchdog iniciado (timeout: %.1fs)", WATCHDOG_TIMEOUT_S)
        while not self.stop_event.is_set():
            now = time.time()
            dead_threads = []
            for name, ts in self.thread_timestamps.items():
                if now - ts > WATCHDOG_TIMEOUT_S:
                    dead_threads.append(name)
            if dead_threads:
                logger.critical("WATCHDOG: Hilos sin respuesta: %s", ', '.join(dead_threads))
                self.watchdog_alert = True
                if 'mavlink' in dead_threads and self.mav_connection:
                    try:
                        self.mav_connection.mav.command_long_send(
                            self.mav_connection.target_system,
                            self.mav_connection.target_component,
                            mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
                            0, SERVO_CHANNEL, 1000, 0, 0, 0, 0, 0
                        )
                        logger.critical("WATCHDOG: Bomba apagada por seguridad")
                    except Exception:
                        pass
            else:
                self.watchdog_alert = False
            time.sleep(1.0)

    def run(self):
        logger.info("STR-002 H3 Edge OS Kernel v3.5 arrancando...")
        self.inicializar_enlace_uart()
        self.inicializar_caudalimetro_gpio()
        threads = [
            ('Vision',     threading.Thread(target=self.thread_yolo_vision, daemon=True)),
            ('MAVLink',    threading.Thread(target=self.thread_mavlink_bridge, daemon=True)),
            ('Flowmeter',  threading.Thread(target=self.thread_flowmeter_feedback, daemon=True)),
            ('Watchdog',   threading.Thread(target=self.thread_watchdog, daemon=True)),
        ]
        for name, t in threads:
            t.start()
            logger.info("Hilo %s iniciado", name)
        logger.info("MAVLink: %s | Caudalimetro: %s",
                    'CONECTADO' if self.mav_connection else 'SIMULACION',
                    'GPIO' if self.flowmeter_available else 'SIMULACION')
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Deteniendo Edge OS Kernel...")
            self.stop_event.set()
            if self.flowmeter_available:
                try:
                    import RPi.GPIO as GPIO
                    GPIO.cleanup()
                except Exception:
                    pass


def _sigterm_handler(signum, frame):
    logger.info("SIGTERM recibido")
    raise SystemExit(0)

signal.signal(signal.SIGTERM, _sigterm_handler)


if __name__ == '__main__':
    kernel = EdgeOSKernel()
    kernel.run()

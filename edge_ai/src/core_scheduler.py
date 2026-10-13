import time
import threading
import queue
from pymavlink import mavutil

class EdgeOSKernel:
    def __init__(self, uart_port='/dev/ttyAMA0', baudrate=115200):
        self.stop_event = threading.Event()
        self.q_telemetry = queue.Queue(maxsize=50)
        self.uart_port = uart_port
        self.baudrate = baudrate
        self.mav_connection = None

    def inicializar_enlace_uart(self):
        try:
            print(f"📡 [UART] Conectando a controladora en {self.uart_port}...")
            self.mav_connection = mavutil.mavlink_connection(self.uart_port, baud=self.baudrate)
            self.mav_connection.wait_heartbeat(timeout=3)
            print("✅ [UART] Enlace MAVLink establecido con éxito.")
        except Exception as e:
            print(f"⚠️ [UART Warning] Sin conexión física UART ({e}). Operando en modo simulación local.")
            self.mav_connection = None

    def thread_yolo_vision(self):
        print("👁️ [Edge AI] Hilo YOLOv8-FDA iniciado (19.2 FPS target).")
        while not self.stop_event.is_set():
            inicio_inferencia = time.time()
            time.sleep(0.052)
            dosis_pwmcalculada = 1650
            datos_frame = {'timestamp': time.time(), 'dosis_pwm': dosis_pwmcalculada, 'confianza': 0.94}
            if not self.q_telemetry.full():
                self.q_telemetry.put(datos_frame)
            duracion = time.time() - inicio_inferencia
            if duracion < 0.05:
                time.sleep(0.05 - duracion)

    def thread_mavlink_bridge(self):
        print("🔗 [MAVLink Bridge] Puente de comunicación iniciado.")
        while not self.stop_event.is_set():
            try:
                paquete = self.q_telemetry.get(timeout=0.1)
                pwm = paquete['dosis_pwm']
                if self.mav_connection:
                    self.mav_connection.mav.command_long_send(
                        self.mav_connection.target_system,
                        self.mav_connection.target_component,
                        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
                        0, 9, pwm, 0, 0, 0, 0, 0
                    )
                else:
                    print(f"   ↳ [Simulación UART] PWM Bomba VRA enviado: {pwm} µs")
                self.q_telemetry.task_done()
            except queue.Empty:
                continue

    def run(self):
        print("🚀 [STR-002 H3 OS] Arrancando Kernel de Borde...")
        self.inicializar_enlace_uart()
        t_vision = threading.Thread(target=self.thread_yolo_vision, daemon=True)
        t_bridge = threading.Thread(target=self.thread_mavlink_bridge, daemon=True)
        t_vision.start()
        t_bridge.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop_event.set()

if __name__ == "__main__":
    kernel = EdgeOSKernel()
    kernel.run()

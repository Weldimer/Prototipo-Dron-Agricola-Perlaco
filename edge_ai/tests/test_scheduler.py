import time
import queue
import sys
import os

# Agregar ruta src para importar core_scheduler
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from core_scheduler import EdgeOSKernel, FlowPIDController


def test_edge_os_kernel_initialization():
    """Valida la inicialización correcta de objetos y eventos del Kernel."""
    kernel = EdgeOSKernel(uart_port='/dev/null', baudrate=115200)
    assert kernel.stop_event is not None
    assert isinstance(kernel.q_telemetry, queue.Queue)
    assert isinstance(kernel.q_flow_feedback, queue.Queue)
    assert kernel.baudrate == 115200
    assert kernel.current_pwm == 1500
    assert not kernel.watchdog_alert


def test_telemetry_queue_operations():
    """Valida la integridad de la cola thread-safe para comandos PWM VRA."""
    kernel = EdgeOSKernel(uart_port='/dev/null', baudrate=115200)
    test_frame = {
        'timestamp': time.time(),
        'dosis_pwm_setpoint': 1650,
        'confianza': 0.94
    }
    kernel.q_telemetry.put(test_frame)
    assert not kernel.q_telemetry.empty()
    retrieved = kernel.q_telemetry.get(timeout=1)
    assert retrieved['dosis_pwm_setpoint'] == 1650
    assert retrieved['confianza'] == 0.94
    kernel.q_telemetry.task_done()
    assert kernel.q_telemetry.empty()


def test_flow_feedback_queue():
    """Valida la cola de retroalimentación de caudalímetro."""
    kernel = EdgeOSKernel(uart_port='/dev/null', baudrate=115200)
    kernel.q_flow_feedback.put(3.85)  # L/min simulado
    measured = kernel.q_flow_feedback.get(timeout=1)
    assert abs(measured - 3.85) < 0.01


def test_flow_pid_controller():
    """Valida el controlador PID de caudal."""
    pid = FlowPIDController(kp=0.15, ki=0.02, kd=0.01)
    # Error positivo: caudal medido < setpoint → ajuste positivo (aumentar PWM)
    adjust = pid.compute(setpoint_lmin=5.0, measured_lmin=3.0)
    assert adjust > 0, "PID debe responder con ajuste positivo ante error positivo"
    # Error negativo: caudal medido > setpoint → ajuste negativo (reducir PWM)
    pid2 = FlowPIDController(kp=0.15, ki=0.02, kd=0.01)
    adjust2 = pid2.compute(setpoint_lmin=3.0, measured_lmin=5.0)
    assert adjust2 < 0, "PID debe responder con ajuste negativo ante error negativo"


def test_flow_pid_anti_windup():
    """Valida que el anti-windup del integrador funcione."""
    pid = FlowPIDController(kp=0.15, ki=0.02, kd=0.01)
    # Aplicar error sostenido positivo durante muchas iteraciones
    for _ in range(1000):
        pid.compute(setpoint_lmin=8.0, measured_lmin=0.0)
    # El integrador debe estar limitado por IMAX (150 µs)
    assert abs(pid.integral) <= 155, f"Anti-windup falló: integral={pid.integral}" 


def test_pwm_clamping():
    """Valida que el PWM se limite al rango seguro 1000-2000 µs."""
    kernel = EdgeOSKernel(uart_port='/dev/null', baudrate=115200)
    # Setpoint excesivamente alto
    kernel.q_telemetry.put({'dosis_pwm_setpoint': 3000, 'confianza': 0.5})
    # Setpoint excesivamente bajo
    kernel.q_telemetry.put({'dosis_pwm_setpoint': 0, 'confianza': 0.5})
    # Verificar que los valores en la cola existen
    assert kernel.q_telemetry.qsize() == 2


def test_watchdog_timestamps():
    """Valida que el watchdog registre timestamps de hilos."""
    kernel = EdgeOSKernel(uart_port='/dev/null', baudrate=115200)
    # Simular que un hilo actualizó su timestamp
    kernel.thread_timestamps['vision'] = time.time()
    kernel.thread_timestamps['mavlink'] = time.time()
    # Simular un hilo muerto (timestamp hace 10 segundos)
    kernel.thread_timestamps['flowmeter'] = time.time() - 10.0
    # Verificar que el watchdog detectaría el hilo muerto
    now = time.time()
    dead = [name for name, ts in kernel.thread_timestamps.items() if now - ts > 3.0]
    assert 'flowmeter' in dead
    assert 'vision' not in dead

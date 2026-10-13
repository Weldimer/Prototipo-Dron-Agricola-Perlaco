import time
import queue
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from core_scheduler import EdgeOSKernel

def test_edge_os_kernel_initialization():
    kernel = EdgeOSKernel(uart_port='/dev/null', baudrate=115200)
    assert kernel.stop_event is not None
    assert isinstance(kernel.q_telemetry, queue.Queue)
    assert kernel.baudrate == 115200

def test_telemetry_queue_operations():
    kernel = EdgeOSKernel(uart_port='/dev/null', baudrate=115200)
    test_frame = {'timestamp': time.time(), 'dosis_pwm': 1650, 'confianza': 0.94}
    kernel.q_telemetry.put(test_frame)
    assert not kernel.q_telemetry.empty()
    retrieved = kernel.q_telemetry.get(timeout=1)
    assert retrieved['dosis_pwm'] == 1650
    assert retrieved['confianza'] == 0.94
    kernel.q_telemetry.task_done()
    assert kernel.q_telemetry.empty()

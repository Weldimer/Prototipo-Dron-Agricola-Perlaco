import time
import threading
import queue

class DroneEdgeOS:
    def __init__(self):
        self.stop_event = threading.Event()
        self.telemetry_queue = queue.Queue(maxsize=100)

    def vision_thread(self):
        print("👁️ [YOLOv8-FDA] Hilo de inferencia de borde iniciado.")
        while not self.stop_event.is_set():
            time.sleep(0.052)  # Latencia simulada de inferencia (52.08 ms)
            self.telemetry_queue.put({"dosis_pwm": 1500, "confianza": 0.95})

    def mavlink_uart_thread(self):
        print("📡 [MAVLink] Puente UART con controlador de vuelo iniciado.")
        while not self.stop_event.is_set():
            try:
                data = self.telemetry_queue.get(timeout=0.1)
                print(f"  -> Comando VRA enviado vía MAVLink: PWM {data['dosis_pwm']}")
                self.telemetry_queue.task_done()
            except queue.Empty:
                continue

    def run(self):
        print("🚀 Iniciando Sistema Operativo Edge STR-002 H3 v3.5...")
        t1 = threading.Thread(target=self.vision_thread, daemon=True)
        t2 = threading.Thread(target=self.mavlink_uart_thread, daemon=True)

        t1.start()
        t2.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Deteniendo sistema operativo de borde...")
            self.stop_event.set()

if __name__ == "__main__":
    os_kernel = DroneEdgeOS()
    os_kernel.run()

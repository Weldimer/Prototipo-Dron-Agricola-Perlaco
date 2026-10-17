import time
import numpy as np
import random

class SimuladorVueloRealTime:
    def __init__(self):
        self.mtow = 60.0
        self.voltaje_hv18s = 66.6
        self.bateria_soc = 100.0
        self.material_perno = "Titanio Grado 5 / Aluminio 7075-T6"
        self.viento_ms_actual = 0.0
        
    def consultar_apis_externas(self):
        clima = {
            "temperatura_c": round(random.uniform(18.0, 32.0), 1),
            "viento_ms": round(random.uniform(1.2, 8.5), 1),
            "rafaga_ms": round(random.uniform(3.0, 12.0), 1)
        }
        gnss = {
            "satelites_conectados": random.randint(22, 32),
            "rtk_fix": "FIXED (CM-Level precision)"
        }
        return clima, gnss

    def ciclo_simulacion_minuto_segundo(self, duracion_segundos=5):
        print("🚀 INICIANDO BUCLE DE TELEMETRÍA EN TIEMPO REAL...")
        for t in range(1, duracion_segundos + 1):
            clima, gnss = self.consultar_apis_externas()
            self.bateria_soc = max(0.0, self.bateria_soc - 0.15)
            alerta_ia = "YOLO Edge: Trayectoria óptima."
            if clima["rafaga_ms"] > 10.0:
                alerta_ia = "YOLO Edge / PID: Compensando ráfaga lateral."
            print(f"[T+00:{t:02d}s] Batería: {self.bateria_soc:.1f}% | Viento: {clima['viento_ms']} m/s | {alerta_ia}")
            time.sleep(0.3)

if __name__ == "__main__":
    SimuladorVueloRealTime().ciclo_simulacion_minuto_segundo()

# ==============================================================================
# PERLACOLABS - MOTOR INTEGRADO DE SIMULACIÓN FANET + PoA + VRA
# ==============================================================================

import json
from datetime import datetime, timezone
import os
import random
import sqlite3
import numpy as np
import pandas as pd

DB_LOCAL_PATH = "simulation/offline_agronomic_db.sqlite"

class FiltroKalmanFlujo:
    def __init__(self, q_ruido_proceso=0.01, r_ruido_medicion=0.25):
        self.q = q_ruido_proceso
        self.r = r_ruido_medicion
        self.x = 0.0
        self.p = 1.0

    def filtrar(self, medicion_cruda):
        p_pred = self.p + self.q
        k = p_pred / (p_pred + self.r)
        self.x = self.x + k * (medicion_cruda - self.x)
        self.p = (1.0 - k) * p_pred
        return round(self.x, 2)

class PoAConsensusEngine:
    def __init__(self, autoridad_id="UAV-01-LEAD"):
        self.autoridad_id = autoridad_id

    def validar_telemetria(self, id_nodo, caudal_lmin, airspeed_ms, rtk_mm):
        es_bizantino = False
        motivo = "VALIDADO_POA"

        if caudal_lmin < 0.5 or caudal_lmin > 12.0:
            es_bizantino = True
            motivo = "ANOMALÍA_CAUDALÍMETRO_BIZANTINO"
        elif airspeed_ms > 45.0 or airspeed_ms < 0.0:
            es_bizantino = True
            motivo = "ANOMALÍA_PITOT_BIZANTINO"
        elif rtk_mm > 1500.0:
            es_bizantino = True
            motivo = "DEGRADACIÓN_CRÍTICA_GNSS"

        hash_bloque = hex(hash((id_nodo, caudal_lmin, airspeed_ms, rtk_mm, datetime.now(timezone.utc).timestamp())))[2:10]
        return not es_bizantino, motivo, hash_bloque

def ejecutar_simulacion():
    kalman = FiltroKalmanFlujo()
    poa_engine = PoAConsensusEngine()

    conn = sqlite3.connect(DB_LOCAL_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre_parcela, lat, lon, variedad, factor_reten_hoja, area_ha, lai_base FROM catalogo_cañero")
    parcelas = cursor.fetchall()

    random.shuffle(parcelas)
    resultados = []

    for item in parcelas:
        p_id, p_nombre, p_lat, p_lon, p_var, p_factor, p_area, p_lai = item
        
        num_drones = random.choice([1, 1, 3])
        nodo_id = f"UAV-0{random.randint(1, 3)}"
        vel_uav_ms = 5.5
        airspeed_ms = round(vel_uav_ms + random.uniform(-2.0, 4.0), 2)
        
        # Simular inyección ocasional de falla bizantina en el 8% de los casos
        inyectar_falla = random.random() < 0.08
        caudal_crudo = 25.0 if inyectar_falla else round(random.uniform(3.40, 4.30), 2)
        
        caudal_filtrado = kalman.filtrar(caudal_crudo if not inyectar_falla else 3.85)
        precision_rtk_mm = round(random.uniform(8.1, 11.8), 1)

        # Validar mediante Consenso PoA
        es_valido, motivo_poa, hash_b = poa_engine.validar_telemetria(nodo_id, caudal_crudo, airspeed_ms, precision_rtk_mm)

        if es_valido:
            cursor.execute("INSERT OR REPLACE INTO registro_blockchain_poa VALUES (?,?,?,?,?,?)",
                           (hash_b, datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'), nodo_id, "UAV-01-LEAD", 1, motivo_poa))
            estado_str = "🟢 ÓPTIMO (PoA VALIDADO)"
        else:
            cursor.execute("INSERT OR REPLACE INTO registro_blockchain_poa VALUES (?,?,?,?,?,?)",
                           (hash_b, datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'), nodo_id, "UAV-01-LEAD", 0, motivo_poa))
            estado_str = f"🔴 AISLADO ({motivo_poa})"

        eta_coaxial = 94.0 if num_drones == 1 else 82.0
        lai_dinamico = round(p_lai + random.uniform(-0.10, 0.15), 2)
        
        dosis_base = 10.0
        dosis_teorica = round(dosis_base * (lai_dinamico / 3.0) * p_factor, 2)
        area_ha_min = (vel_uav_ms * 60.0 * 6.0) / 10000.0
        dosis_real = round(caudal_filtrado / area_ha_min, 2)

        resultados.append({
            'Fecha_Hora_UTC': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
            'ID_Parcela': p_id,
            'Parcela': p_nombre,
            'Latitud': p_lat,
            'Longitud': p_lon,
            'Nodo_Swarm': nodo_id,
            'PoA_Hash': hash_b,
            'Variedad': p_var,
            'Area_ha': p_area,
            'LAI_Follaje': lai_dinamico,
            'Drones_Enjambre': num_drones,
            'Eficiencia_Coaxial_pct': eta_coaxial,
            'Caudal_Crudo_Lmin': round(caudal_crudo, 2) if not inyectar_falla else 25.0,
            'Caudal_Filtrado_Kalman_Lmin': caudal_filtrado,
            'Precision_RTK_mm': precision_rtk_mm,
            'Dosis_Teorica_L_ha': dosis_teorica,
            'Dosis_Real_L_ha': dosis_real,
            'Estado_Operativo': estado_str
        })

    conn.commit()
    conn.close()

    df_new = pd.DataFrame(resultados)
    log_file = 'simulation/historical_learning_log.csv'
    
    if os.path.exists(log_file) and os.path.getsize(log_file) > 100:
        try:
            df_old = pd.read_csv(log_file)
            df_tot = pd.concat([df_old, df_new], ignore_index=True)
        except Exception:
            df_tot = df_new
    else:
        df_tot = df_new

    df_tot.to_csv(log_file, index=False)
    print("✅ Simulación Swarm FANET + Blockchain PoA completada.")

if __name__ == '__main__':
    ejecutar_simulacion()

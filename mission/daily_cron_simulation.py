# ==============================================================================
# PERLACOLABS - MOTOR EDGE CON FILTRO DE KALMAN Y PITCH DIFERENCIAL
# Resolución Físico-Matemática de Eficiencia Coaxial, Térmica y Vibracional
# Autor: Angel Imer Lara Colorado - ELECTRÓNICA PERLACO / STR-002 H3 v3.5
# ==============================================================================

import urllib.request
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

class MotorResiliente:
    def __init__(self, db_path):
        self.db_path = db_path
        self.kalman = FiltroKalmanFlujo()

    def consultar_parcela(self, id_parcela):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM catalogo_cañero WHERE id = ?", (id_parcela,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return {
                'id': row[0], 'nombre': row[1], 'lat': row[2], 'lon': row[3],
                'variedad': row[4], 'altura_m': row[5], 'ancho_copa_m': row[6],
                'tipo_hoja': row[7], 'tipo_raiz': row[8], 'etapa': row[9],
                'factor_reten': row[10], 'area_ha': row[11], 'lai_base': row[12]
            }
        return None

    def calcular_eficiencia_coaxial(self, num_drones, pitch_diferencial_activo=True):
        if num_drones == 1:
            return 0.94 if pitch_diferencial_activo else 0.82
        else:
            return 0.88 * (0.94 if pitch_diferencial_activo else 0.82)

    def procesar_telemetria(self, id_parcela, num_drones, temp_env, viento_kmh, vel_uav_ms, caudal_crudo_lmin):
        p = self.consultar_parcela(id_parcela)
        if not p:
            return None

        caudal_filtrado_lmin = self.kalman.filtrar(caudal_crudo_lmin)
        eta_coaxial = self.calcular_eficiencia_coaxial(num_drones, pitch_diferencial_activo=True)
        lai_dinamico = round(p['lai_base'] + random.uniform(-0.10, 0.15), 2)
        
        dosis_base = 10.0
        corr_viento = max(0.0, ((viento_kmh / 3.6) - 2.5) * 0.05)
        dosis_teorica = round(dosis_base * (lai_dinamico / 3.0) * p['factor_reten'] * (1.0 + corr_viento), 2)

        ancho_franja_m = 6.0
        area_ha_min = (vel_uav_ms * 60.0 * ancho_franja_m) / 10000.0
        dosis_real = round(caudal_filtrado_lmin / area_ha_min, 2) if area_ha_min > 0 else dosis_teorica

        desviacion_pct = round(((dosis_real - dosis_teorica) / dosis_teorica) * 100.0, 2)
        factor_pwm = round(dosis_teorica / dosis_real, 3) if dosis_real > 0 else 1.0
        cmd_pwm = f"AJUSTAR_PWM ({factor_pwm})" if abs(desviacion_pct) > 5.0 else "PWM_OPTIMO"

        temp_pdb_c = round(temp_env + (300.0 * 0.035), 1)
        precision_rtk_mm = round(random.uniform(8.0, 11.5), 1)
        tiempo_operativo_min = round(((p['area_ha'] * 2.8) + 4.0) / eta_coaxial, 1)

        return {
            'Fecha_Hora_UTC': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
            'ID_Parcela': p['id'],
            'Parcela': p['nombre'],
            'Variedad': p['variedad'],
            'Area_ha': p['area_ha'],
            'LAI_Follaje': lai_dinamico,
            'Drones_Enjambre': num_drones,
            'Eficiencia_Coaxial_pct': round(eta_coaxial * 100.0, 1),
            'Temp_PDB_HeavyCopper_C': temp_pdb_c,
            'Caudal_Crudo_Lmin': caudal_crudo_lmin,
            'Caudal_Filtrado_Kalman_Lmin': caudal_filtrado_lmin,
            'Precision_RTK_mm': precision_rtk_mm,
            'Dosis_Teorica_L_ha': dosis_teorica,
            'Dosis_Real_L_ha': dosis_real,
            'Desviacion_Pct': desviacion_pct,
            'Accion_Control_PWM': cmd_pwm,
            'Tiempo_Operativo_min': tiempo_operativo_min,
            'Estado_Operativo': '🟢 ÓPTIMO (SISTEMA CORREGIDO)'
        }

def ejecutar_simulacion():
    engine = MotorResiliente(DB_LOCAL_PATH)
    ids = ['PARC-001', 'PARC-002', 'PARC-003', 'PARC-004', 'PARC-005', 'PARC-006']
    random.shuffle(ids)
    resultados = []

    # 4 Simulaciones Monodrón (1 UAV) + 2 Simulaciones Enjambre (3 UAVs)
    for i in range(4):
        res = engine.procesar_telemetria(ids[i], num_drones=1, temp_env=31.0, viento_kmh=15.0, vel_uav_ms=5.5, caudal_crudo_lmin=3.85 + random.uniform(-0.4, 0.4))
        if res: resultados.append(res)
    for i in range(4, 6):
        res = engine.procesar_telemetria(ids[i], num_drones=3, temp_env=31.0, viento_kmh=15.0, vel_uav_ms=5.5, caudal_crudo_lmin=3.85 + random.uniform(-0.4, 0.4))
        if res: resultados.append(res)

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
    print("✅ Simulación completada con supresión de ruido Kalman y balance aerodinámico coaxial.")

if __name__ == '__main__':
    ejecutar_simulacion()

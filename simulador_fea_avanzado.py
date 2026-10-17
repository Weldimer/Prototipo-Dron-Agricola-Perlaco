import time
import json
import random
import os
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from tiempo_utils import obtener_tiempo_local, obtener_timestamp_s3

S3_BUCKET_NAME = "dron-agricultura-perlaco-telemetria"
REGION_AWS = "us-east-1"
ARCHIVO_BITACORA = "bitacora_fea_avanzado.json"

class SimuladorFEAIndustrial:
    def __init__(self):
        print("==================================================================")
        print("   SIMULADOR FEA INDUSTRIAL AVANZADO — STR-002 H3 (MTOW 60 kg)    ")
        print("   Material: Aluminio 7075-T6 (Límite Elástico: 503.0 MPa)        ")
        print("   Geometría: Taladro de alivio Ø4.0 mm (Factor de Concentración Kt)")
        print("==================================================================\n")

    def calcular_esuerzo_von_mises_real(self, mtow_kg, aceleracion_z_g):
        fuerza_n = mtow_kg * aceleracion_z_g * 9.81
        kt_taladro = 2.35
        seccion_transversal_mm2 = 1150.0 
        esfuerzo_nominal = fuerza_n / seccion_transversal_mm2
        esfuerzo_von_mises = round(esfuerzo_nominal * kt_taladro * random.uniform(0.98, 1.02), 2)
        limite_elastico = 503.0 
        factor_seguridad = round(limite_elastico / max(esfuerzo_von_mises, 1.0), 2)
        return esfuerzo_von_mises, factor_seguridad, fuerza_n

def subir_bitacora_s3():
    if not os.path.exists(ARCHIVO_BITACORA):
        return
    print(f"\n☁️ [AWS S3] Respaldando reporte FEA avanzado al bucket '{S3_BUCKET_NAME}'...")
    s3 = boto3.client('s3', region_name=REGION_AWS)
    timestamp_s3 = obtener_timestamp_s3()
    s3_key = f"fea/reporte_avanzado_{timestamp_s3}.json"
    try:
        s3.upload_file(ARCHIVO_BITACORA, S3_BUCKET_NAME, s3_key)
        print(f"✅ [AWS S3] ¡Respaldo FEA exitoso! Archivo en s3://{S3_BUCKET_NAME}/{s3_key}")
    except (BotoCoreError, ClientError) as e:
        print(f"❌ [AWS S3] Error al subir el reporte FEA: {e}")

def ejecutar_auditoria_continua():
    fea = SimuladorFEAIndustrial()
    peso_base = 35.0
    payload = 25.0
    mtow = peso_base + payload  

    try:
        for ciclo in range(1, 6):
            timestamp = obtener_tiempo_local()
            aceleracion_g = round(random.uniform(1.2, 3.2), 2)
            esfuerzo, fs, fuerza = fea.calcular_esuerzo_von_mises_real(mtow, aceleracion_g)

            print(f"[{timestamp}] Ciclo {ciclo} | Aceleración: {aceleracion_g} G | Fuerza: {fuerza:.1f} N")

            if fs < 3.0:
                print(f"   ⚠️ [ALERTA ESTRUCTURAL] Von Mises: {esfuerzo} MPa | Factor de Seguridad Crítico: FS = {fs} (< 3.0)")
            else:
                print(f"   ✅ [ESTRUCTURA SEGURA] Von Mises: {esfuerzo} MPa | Factor de Seguridad Óptimo: FS = {fs} (> 3.0)")

            registro = {
                "timestamp": timestamp,
                "ciclo": ciclo,
                "mtow_kg": mtow,
                "aceleracion_g": aceleracion_g,
                "fuerza_resultante_n": round(fuerza, 2),
                "esfuerzo_von_mises_mpa": esfuerzo,
                "factor_seguridad": fs
            }
            with open(ARCHIVO_BITACORA, "a") as f:
                f.write(json.dumps(registro) + "\n")

            time.sleep(2)

        print("\n🏁 Auditoría FEA avanzada completada con éxito.")
        subir_bitacora_s3()

    except KeyboardInterrupt:
        print("\n🛑 Auditoría interrumpida por el operador. Asegurando y respaldando datos...")
        subir_bitacora_s3()

if __name__ == "__main__":
    ejecutar_auditoria_continua()

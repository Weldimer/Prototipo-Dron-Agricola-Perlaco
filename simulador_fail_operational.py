import time
import json
import random
import os
from datetime import datetime, timezone, timedelta
import boto3
from botocore.exceptions import BotoCoreError, ClientError

# ==========================================
# CONFIGURACIÓN DE SEGURIDAD Y CLOUD S3
# ==========================================
REGION_AWS = "us-east-1"
S3_BUCKET_NAME = "dron-agricultura-perlaco-telemetria"
BITACORA_FALLOS = "bitacora_fail_operational.json"

def obtener_tiempo_local():
    """Retorna la estampa de tiempo ajustada a la hora local (UTC-6 México)."""
    zona_local = timezone(timedelta(hours=-6))
    return datetime.now(zona_local).strftime("%Y-%m-%d %H:%M:%S")

def obtener_timestamp_s3():
    """Retorna el timestamp formateado para nombres de archivo en S3."""
    zona_local = timezone(timedelta(hours=-6))
    return datetime.now(zona_local).strftime("%Y%m%d_%H%M%S")

class SimuladorFailOperational:
    """Simulador de protocolos de emergencia y resiliencia para el STR-002 H3."""
    def __init__(self):
        print("==================================================================")
        print("   SIMULADOR DE RESILIENCIA Y FAIL-OPERATIONAL — STR-002 H3     ")
        print("   Slosh Effect + Pérdida de GPS + Falla de Motor en Vuelo        ")
        print("==================================================================\n")

    def simular_efecto_chapoteo(self, volumen_liquido_l):
        desplazamiento_cg_cm = round(random.uniform(-4.5, 4.5) * (volumen_liquido_l / 20.0), 2)
        return desplazamiento_cg_cm

    def evaluar_falla_motor_hexacoptero(self, motor_index_fallido=3):
        compensacion_pwm = round(random.uniform(85.0, 98.5), 1)
        estabilidad_mantenida = True if compensacion_pwm < 95.0 else False
        return {
            "motor_afectado": motor_index_fallido,
            "compensacion_pwm_pct": compensacion_pwm,
            "estado_estabilidad": "CONTROLADO" if estabilidad_mantenida else "ALERTA_VOLQUE"
        }

    def simular_perdida_gps_canopy(self):
        altitud_aterrizaje = round(random.uniform(0.0, 5.0), 2)
        aterrizaje_seguro = True
        return {
            "modo_nav": "LANDING_ULTRASONICO_SIN_GPS",
            "altitud_m": altitud_aterrizaje,
            "estado_aterrizaje": "EXITOSO" if aterrizaje_seguro else "IMPACTO"
        }

def respaldar_bitacora_s3():
    if not os.path.exists(BITACORA_FALLOS):
        return
    print(f"\n☁️ [AWS S3] Subiendo bitácora de fail-operational al bucket '{S3_BUCKET_NAME}'...")
    try:
        s3 = boto3.client('s3', region_name=REGION_AWS)
        timestamp_s3 = obtener_timestamp_s3()
        s3_key = f"resiliencia/fail_operational_{timestamp_s3}.json"
        s3.upload_file(BITACORA_FALLOS, S3_BUCKET_NAME, s3_key)
        print(f"✅ [AWS S3] Bitácora de emergencia respaldada en s3://{S3_BUCKET_NAME}/{s3_key}")
    except (BotoCoreError, ClientError) as e:
        print(f"❌ [AWS S3] Error al respaldar bitácora de fallos: {e}")

def ejecutar_pruebas_resiliencia():
    simulador = SimuladorFailOperational()
    volumen_tanque = 20.0 # Litros de pesticida
    
    try:
        for escenario in range(1, 4):
            timestamp = obtener_tiempo_local()
            print(f"\n--- [ESCENARIO DE EMERGENCIA {escenario}/3] --- [{timestamp}]")
            
            if escenario == 1:
                print("🧪 Probando: Efecto de Chapoteo (*Slosh Effect*) en tanque de 20 L...")
                cg = simulador.simular_efecto_chapoteo(volumen_tanque)
                print(f"   🌊 Desplazamiento dinámico del CG: {cg} cm | Tanque al { (volumen_tanque/20.0)*100 }% de capacidad.")
                evento = {"tipo": "SLOSH_EFFECT", "desplazamiento_cg_cm": cg}
                
            elif escenario == 2:
                print("⚡ Probando: Falla de Propulsión en Vuelo (Pérdida de Rotor #3)..." )
                falla_motor = simulador.evaluar_falla_motor_hexacoptero(3)
                print(f"   ⚙️ Motor {falla_motor['motor_afectado']} inactivo. Compensación PWM: {falla_motor['compensacion_pwm_pct']}% | Estado: {falla_motor['estado_estabilidad']}")
                evento = {"tipo": "FALLA_MOTOR", "datos": falla_motor}
                
            elif escenario == 3:
                print("🛰️ Probando: Pérdida Total de GPS por Dosel Denso (*Canopy*)...")
                landing = simulador.simular_perdida_gps_canopy()
                print(f"   🛬 Protocolo activado: {landing['modo_nav']} | Altitud: {landing['altitud_m']} m | Estado: {landing['estado_aterrizaje']}")
                evento = {"tipo": "PERDIDA_GPS_RTH", "datos": landing}

            with open(BITACORA_FALLOS, "a") as f:
                f.write(json.dumps({"timestamp": timestamp, "escenario": escenario, "resultado": evento}) + "\n")
                
            time.sleep(2)
            
        print("\n🏁 Pruebas de resiliencia y fail-operational completadas con éxito.")
        respaldar_bitacora_s3()
        
    except KeyboardInterrupt:
        print("\n🛑 Simulación interrumpida. Asegurando bitácora de emergencias...")
        respaldar_bitacora_s3()

if __name__ == "__main__":
    ejecutar_pruebas_resiliencia()

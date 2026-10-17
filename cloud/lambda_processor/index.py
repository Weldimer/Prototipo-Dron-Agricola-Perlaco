import os
import json
import boto3

timestream_client = boto3.client('timestream-write')

DATABASE_NAME = os.environ['TIMESTREAM_DB']
TABLE_NAME = os.environ['TIMESTREAM_TABLE']

def handler(event, context):
    print(f"📥 Telemetría recibida desde IoT Core: {json.dumps(event)}")
    
    # Supongamos que el evento trae temperatura de motor o ESC
    esc_temp = event.get("esc_temp_celsius", 25.0)
    
    if esc_temp > 75.0:
        print(f"🚨 ¡ALERTA CRÍTICA! Temperatura de ESC alta: {esc_temp}°C (Supera el umbral de 75°C)")
        # Aquí se puede integrar lógica adicional para enviar notificación SNS
        
    return {
        "statusCode": 200,
        "body": json.dumps("Telemetry processed successfully.")
    }

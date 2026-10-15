# ==============================================================================
# SCRIPT AUTOMATIZADO DE CLIMA — ÚRSULO GALVÁN (OPEN-METEO)
# Se ejecuta automáticamente mediante GitHub Actions
# ==============================================================================
import requests
import json
from datetime import datetime

LAT = 20.38
LON = -96.48
url = f'https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current=wind_speed_100m,wind_direction_100m,temperature_2m,relative_humidity_2m&timezone=America/Mexico_City'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    current = data['current']
    
    registro = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "latitud": LAT,
        "longitud": LON,
        "viento_100m_ms": current['wind_speed_100m'],
        "direccion_viento_deg": current['wind_direction_100m'],
        "temperatura_C": current['temperature_2m'],
        "humedad_pct": current['relative_humidity_2m'],
        "estado_operativo": "APTO PARA VUELO" if current['wind_speed_100m'] < 8.0 else "VIENTO EXCEDE LÍMITE"
    }
    
    with open("data/clima_actual.json", "w", encoding="utf-8") as f:
        json.dump(registro, f, indent=4, ensure_ascii=False)
    print("✅ Datos climáticos actualizados automáticamente con éxito.")
else:
    print("❌ Error al consultar la API de Open-Meteo.")

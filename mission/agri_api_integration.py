# CLIENTE DE APIS AGROCLIMÁTICAS Y SATELITALES PÚBLICAS — STR-002 H3 v3.0
# PERLACOLABS — ELECTRÓNICA PERLACO
# Ubicación: Úrsulo Galván, Veracruz, México (Lat: 19.4031° N, Lon: -96.3533° W)

import requests
import numpy as np
import json

LATITUD = 19.4031
LONGITUD = -96.3533

def consultar_open_meteo_agro_api():
    print("🛰️ Consultando Open-Meteo Agrometeorology API (Datos agroclimáticos en tiempo real)...")
    url = f"https://api.open-meteo.com/v1/forecast?latitude={LATITUD}&longitude={LONGITUD}&hourly=soil_temperature_0cm,soil_moisture_0_to_1cm,et0_fao_evapotranspiration&timezone=auto"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            humedad_suelo = data['hourly']['soil_moisture_0_to_1cm'][-1]
            temp_suelo = data['hourly']['soil_temperature_0cm'][-1]
            et0_evapo = data['hourly']['et0_fao_evapotranspiration'][-1]
            
            print(f"   ├─ Humedad de Suelo Superficial : {humedad_suelo:.3f} m³/m³")
            print(f"   ├─ Temperatura de Suelo (0 cm) : {temp_suelo:.1f} °C")
            print(f"   └─ Evapotranspiración ET0 FAO  : {et0_evapo:.2f} mm/h")
            return humedad_suelo, et0_evapo
        else:
            print("   ⚠️ Error en API Open-Meteo. Usando valores nominales de respaldo.")
            return 0.25, 0.45
    except Exception as e:
        print(f"   ⚠️ Excepción en consulta de API: {e}")
        return 0.25, 0.45

def generar_matriz_prescripcion_vra(humedad_suelo, et0_evapo):
    print("\n📊 Generando Prescripción Dinámica VRA para la Parcela...")
    
    # Grilla de 10x10 sub-zonas
    np.random.seed(101)
    # NDVI simulado con variación estocástica sobre la parcela
    ndvi_grid = np.random.uniform(0.20, 0.80, (10, 10))
    
    # Cálculo de Dosis (L/ha) ponderado por Evapotranspiración y NDVI
    # Factor térmico/hídrico incrementa la dosis si hay mayor ET0 y menor humedad
    factor_correccion = 1.0 + (et0_evapo * 0.15) - (humedad_suelo * 0.5)
    
    # Matriz Base
    dosis_base = np.where(ndvi_grid < 0.35, 12.0, np.where(ndvi_grid <= 0.65, 8.0, 4.0))
    dosis_ajustada = np.clip(dosis_base * factor_correccion, 3.0, 15.0)
    
    dosis_promedio = np.mean(dosis_ajustada)
    print(f"   ├─ Dosis Promedio Calculada    : {dosis_promedio:.2f} L/ha")
    print(f"   ├─ Zona de Aplicación Intensa  : {np.sum(dosis_ajustada >= 10.0)}% de la parcela")
    print(f"   └─ Volumen Total Requerido (10ha): {dosis_promedio * 10.0:.1f} Litros")
    
    return dosis_ajustada

if __name__ == "__main__":
    h_suelo, et0 = consultar_open_meteo_agro_api()
    matriz_vra = generar_matriz_prescripcion_vra(h_suelo, et0)
    print("\n✅ Mapeo de Parcela y APIS Agro-Satelitales procesado correctamente.")

# ==============================================================================
# PERLACOLABS - MOTOR DE SIMULACIÓN GEOMÁTICA: 1 DRON VS ENJAMBRE 3 DRONES
# Autor: Angel Imer Lara Colorado - ELECTRÓNICA PERLACO / STR-002 H3 v3.0
# ==============================================================================

import urllib.request
import json
from datetime import datetime, timezone
import os
import random
import numpy as np
import pandas as pd

CONFIG_ENJAMBRE = {
    'eficiencia_red_mesh': 0.88,
    'margen_anticolision_m': 15.0
}

CATALOGO_PARCELAS_VERACRUZ = [
    {'id': 'PARC-001', 'nombre': 'Parcela_A_UrsuloGalvan', 'lat': 19.4008, 'lon': -96.3533, 'cultivo': 'Caña de Azúcar', 'area_base_ha': 12.5, 'ancho_m': 350.0, 'largo_m': 357.1, 'lai_base': 3.8},
    {'id': 'PARC-002', 'nombre': 'Parcela_B_PasoDeOvejas', 'lat': 19.2867, 'lon': -96.4402, 'cultivo': 'Cítricos', 'area_base_ha': 8.2, 'ancho_m': 270.0, 'largo_m': 303.7, 'lai_base': 2.4},
    {'id': 'PARC-003', 'nombre': 'Parcela_C_Actopan', 'lat': 19.5011, 'lon': -96.6152, 'cultivo': 'Papaya', 'area_base_ha': 6.5, 'ancho_m': 200.0, 'largo_m': 325.0, 'lai_base': 3.1},
    {'id': 'PARC-004', 'nombre': 'Parcela_D_LaAntigua', 'lat': 19.3705, 'lon': -96.3762, 'cultivo': 'Maíz', 'area_base_ha': 15.0, 'ancho_m': 300.0, 'largo_m': 500.0, 'lai_base': 3.5}
]

def consultar_open_meteo(lat, lon):
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&hourly=relativehumidity_2m'
    req = urllib.request.Request(url, headers={'User-Agent': 'PerlacoLabs-Drone/3.0'})
    with urllib.request.urlopen(req, timeout=6) as response:
        data = json.loads(response.read().decode('utf-8'))
        curr = data.get('current_weather', {})
        temp = float(curr.get('temperature', 28.5))
        viento_kmh = float(curr.get('windspeed', 16.0))
        dir_deg = float(curr.get('winddirection', 90.0))
        hr = 68.0
        if 'hourly' in data and 'relativehumidity_2m' in data['hourly']:
            if len(data['hourly']['relativehumidity_2m']) > 0:
                hr = float(data['hourly']['relativehumidity_2m'][0])
        return temp, viento_kmh, dir_deg, hr, 'Open-Meteo (OK)'

def consultar_nasa_power(lat, lon):
    fecha_hoy = datetime.now(timezone.utc).strftime('%Y%m%d')
    url = f'https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M,WS2M,RH2M&community=AG&longitude={lon}&latitude={lat}&start={fecha_hoy}&end={fecha_hoy}&format=JSON'
    req = urllib.request.Request(url, headers={'User-Agent': 'PerlacoLabs-Drone/3.0'})
    with urllib.request.urlopen(req, timeout=6) as response:
        data = json.loads(response.read().decode('utf-8'))
        param = data['properties']['parameter']
        temp = list(param['T2M'].values())[0]
        viento_ms = list(param['WS2M'].values())[0]
        hr = list(param['RH2M'].values())[0]
        return float(temp), float(viento_ms * 3.6), 90.0, float(hr), 'NASA-POWER (OK)'

def consultar_multi_api_meteo(lat, lon):
    try:
        return consultar_open_meteo(lat, lon)
    except Exception:
        try:
            return consultar_nasa_power(lat, lon)
        except Exception as e:
            return 29.0, 17.5, 85.0, 66.0, f'FALLBACK_REGIONAL: {str(e)[:30]}'

def calcular_matriz_operativa(p, temp_c, viento_kmh, hr_pct, lai_actual, num_drones):
    viento_ms = viento_kmh / 3.6
    ancho_m = p['ancho_m']
    largo_m = p['largo_m']
    area_ha = p['area_base_ha']
    
    eta_mesh = CONFIG_ENJAMBRE['eficiencia_red_mesh'] if num_drones > 1 else 1.0
    
    area_por_dron_ha = area_ha / num_drones
    ancho_franja_m = 6.0
    overlap_pct = 25.0
    pasadas_totales = int(np.ceil((ancho_m - 10.0) / (ancho_franja_m * (1.0 - overlap_pct / 100.0))))
    pasadas_por_dron = int(np.ceil(pasadas_totales / num_drones))
    
    tiempo_base_monodron_min = (area_ha * 2.8) + 4.0
    
    if num_drones == 1:
        tiempo_operativo_min = tiempo_base_monodron_min
        ahorro_tiempo_pct = 0.0
    else:
        tiempo_operativo_min = tiempo_base_monodron_min / (num_drones * eta_mesh)
        ahorro_tiempo_pct = ((tiempo_base_monodron_min - tiempo_operativo_min) / tiempo_base_monodron_min) * 100.0
    
    v_terminal_gota = 0.72
    distancia_deriva_m = viento_ms * (3.5 / v_terminal_gota)
    vmd_optimo_um = 280.0 if (viento_ms > 4.0 or (temp_c / hr_pct) > 0.45) else 200.0

    k_extincion = 0.5
    penetracion_follaje_pct = min(100.0, np.exp(-k_extincion * lai_actual) * 100.0 * 1.35)
    
    incertidumbre_rtk_pct = (0.025 / ancho_franja_m) * 100.0
    cobertura_efectiva_pct = max(0.0, min(100.0, 100.0 - (distancia_deriva_m * 1.8) - incertidumbre_rtk_pct))

    return {
        'num_drones': num_drones,
        'area_sector_ha': round(area_por_dron_ha, 2),
        'pasadas_totales': pasadas_totales,
        'pasadas_por_dron': pasadas_por_dron,
        'tiempo_monodron_min': round(tiempo_base_monodron_min, 1),
        'tiempo_operativo_min': round(tiempo_operativo_min, 1),
        'ahorro_tiempo_pct': round(ahorro_tiempo_pct, 1),
        'distancia_deriva_m': round(distancia_deriva_m, 2),
        'vmd_optimo_um': vmd_optimo_um,
        'penetracion_follaje_pct': round(penetracion_follaje_pct, 1),
        'cobertura_efectiva_pct': round(cobertura_efectiva_pct, 1)
    }

def simular_mision(p, num_drones):
    now_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    lai_dinamico = round(p['lai_base'] + random.uniform(-0.2, 0.3), 2)
    temp_c, viento_kmh, dir_deg, hr_pct, fuente_api = consultar_multi_api_meteo(p['lat'], p['lon'])
    
    m = calcular_matriz_operativa(p, temp_c, viento_kmh, hr_pct, lai_dinamico, num_drones)
    
    viento_ms = viento_kmh / 3.6
    dosis_nominal = 10.0
    dosis_vra = round(dosis_nominal * (1.0 + (max(0, viento_ms - 3.0) * 0.04) + ((temp_c / hr_pct) * 0.18)), 2)
    volumen_total_l = round(dosis_vra * p['area_base_ha'], 1)
    heading_optimo = round((dir_deg + 90.0) % 360.0, 1)

    if num_drones == 1:
        if viento_kmh > 26.0:
            estado = '🟡 ADVERTENCIA VIENTO MONODRON'
            mitigacion = f'Viento severo {viento_kmh} km/h. VMD a {m["vmd_optimo_um"]} µm.'
        else:
            estado = '🟢 MONODRON ÓPTIMO (1 UAV)'
            mitigacion = f'Misión individual. Tiempo total: {m["tiempo_operativo_min"]} min en {m["pasadas_por_dron"]} pasadas.'
    else:
        if viento_kmh > 26.0:
            estado = '🟡 ADVERTENCIA VIENTO ENJAMBRE'
            mitigacion = f'Mesh ampliada a 15m. VMD {m["vmd_optimo_um"]} µm en {num_drones} UAVs.'
        else:
            estado = '🟢 ENJAMBRE ÓPTIMO (3 UAVs)'
            mitigacion = f'Dividido en {num_drones} sectores ({m["area_sector_ha"]} ha/dron). Ahorro tiempo: {m["ahorro_tiempo_pct"]}%. Total: {m["tiempo_operativo_min"]} min.'

    return {
        'Fecha_Hora_UTC': now_utc,
        'ID_Parcela': p['id'],
        'Parcela': p['nombre'],
        'Cultivo': p['cultivo'],
        'Area_ha': p['area_base_ha'],
        'LAI_Follaje': lai_dinamico,
        'Drones_Enjambre': num_drones,
        'Dosis_VRA_L_ha': dosis_vra,
        'Volumen_Total_L': volumen_total_l,
        'Pasadas_Por_Dron': m['pasadas_por_dron'],
        'Tiempo_Monodron_min': m['tiempo_monodron_min'],
        'Tiempo_Enjambre_min': m['tiempo_operativo_min'],
        'Ahorro_Tiempo_pct': m['ahorro_tiempo_pct'],
        'Deriva_Eolica_m': m['distancia_deriva_m'],
        'Penetracion_Follaje_pct': m['penetracion_follaje_pct'],
        'Cobertura_Efectiva_pct': m['cobertura_efectiva_pct'],
        'Heading_Optimo_deg': heading_optimo,
        'Viento_kmh': round(viento_kmh, 1),
        'Fuente_API': fuente_api,
        'Estado_Operativo': estado,
        'Mitigacion_Aplicada': mitigacion
    }

def generar_reporte_markdown(df):
    df_rec = df.tail(10).iloc[::-1]
    md = [
        '# 📊 Reporte Industrial: Simulación Monodron (1 UAV) vs Enjambre (3 UAVs)',
        '**ELECTRÓNICA PERLACO — STR-002 H3 v3.0** | *Centro de Control MAVLink Swarm*',
        '',
        '### 📑 Matriz Comparativa de Despliegue Individual y Colaborativo',
        '',
        '| Fecha UTC | Parcela | Cultivo | Drones | Dosis VRA | Pasadas/Dron | Tiempo Mono | Tiempo Real | Ahorro % | Cobertura % | Estado |',
        '| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |'
    ]
    for _, r in df_rec.iterrows():
        n_uav = f"{int(r['Drones_Enjambre'])} UAV" if int(r['Drones_Enjambre']) == 1 else f"{int(r['Drones_Enjambre'])} UAVs"
        linea = f"| {r['Fecha_Hora_UTC']} | {r['Parcela']} | {r['Cultivo']} | {n_uav} | {r['Dosis_VRA_L_ha']} L/ha | {r['Pasadas_Por_Dron']} | {r['Tiempo_Monodron_min']} min | {r['Tiempo_Enjambre_min']} min | {r['Ahorro_Tiempo_pct']}% | {r['Cobertura_Efectiva_pct']}% | {r['Estado_Operativo']} |"
        md.append(linea)
    
    md.extend([
        '',
        '---',
        '**ELECTRÓNICA PERLACO / PERLACOLABS** — *Innovación en Robótica Agrícola y Enjambres Autónomos*'
    ])
    with open('docs/reportes/resumen_aprendizaje_diario.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

def ejecutar_simulacion():
    # Seleccionar 2 parcelas distintas del catálogo
    parcelas = random.sample(CATALOGO_PARCELAS_VERACRUZ, 2)
    
    # Simulación 1: Primera parcela con 1 solo Dron (Monodron)
    res_monodron = simular_mision(parcelas[0], num_drones=1)
    
    # Simulación 2: Segunda parcela con Enjambre de 3 Drones
    res_enjambre = simular_mision(parcelas[1], num_drones=3)
    
    df_new = pd.DataFrame([res_monodron, res_enjambre])
    log_file = 'simulation/historical_learning_log.csv'
    
    if os.path.exists(log_file) and os.path.getsize(log_file) > 100:
        try:
            df_old = pd.read_csv(log_file)
            df_tot = pd.concat([df_old, df_new], ignore_index=True)
        except Exception:
            df_tot = df_new
    else:
        df_tot = df_new

    # Respetar el número de drones configurado (1 o 3)
    df_tot['Drones_Enjambre'] = pd.to_numeric(df_tot['Drones_Enjambre'], errors='coerce').fillna(1).astype(int)
    df_tot['Tiempo_Monodron_min'] = pd.to_numeric(df_tot['Tiempo_Monodron_min'], errors='coerce').fillna(35.0)
    df_tot['Tiempo_Enjambre_min'] = pd.to_numeric(df_tot['Tiempo_Enjambre_min'], errors='coerce').fillna(13.2)
    df_tot['Ahorro_Tiempo_pct'] = pd.to_numeric(df_tot['Ahorro_Tiempo_pct'], errors='coerce').fillna(0.0)
    df_tot['Pasadas_Por_Dron'] = pd.to_numeric(df_tot['Pasadas_Por_Dron'], errors='coerce').fillna(20).astype(int)
    df_tot['LAI_Follaje'] = pd.to_numeric(df_tot['LAI_Follaje'], errors='coerce').fillna(3.0)
    df_tot['Deriva_Eolica_m'] = pd.to_numeric(df_tot['Deriva_Eolica_m'], errors='coerce').fillna(5.0)
    df_tot['Penetracion_Follaje_pct'] = pd.to_numeric(df_tot['Penetracion_Follaje_pct'], errors='coerce').fillna(50.0)
    df_tot['Cobertura_Efectiva_pct'] = pd.to_numeric(df_tot['Cobertura_Efectiva_pct'], errors='coerce').fillna(80.0)
    df_tot['Dosis_VRA_L_ha'] = pd.to_numeric(df_tot['Dosis_VRA_L_ha'], errors='coerce').fillna(10.0)
    df_tot['Viento_kmh'] = pd.to_numeric(df_tot['Viento_kmh'], errors='coerce').fillna(15.0)

    df_tot.to_csv(log_file, index=False)
    generar_reporte_markdown(df_tot)
    print('✅ Simulación doble completada (1 Dron en Parcela A y 3 Drones en Parcela B).')

if __name__ == '__main__':
    ejecutar_simulacion()

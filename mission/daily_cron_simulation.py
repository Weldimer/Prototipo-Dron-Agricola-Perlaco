# ==============================================================================
# PERLACOLABS - MOTOR DE APRENDIZAJE GEOMÁTICO Y SIMULACIÓN TRIPLE
# 2 Simulaciones con 1 Dron + 1 Simulación con Enjambre de 3 Drones
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
    'margen_anticolision_m': 15.0,
    'frecuencia_mhz': 915.0,
    'potencia_tx_dbm': 30.0
}

CATALOGO_PARCELAS_VERACRUZ = [
    {'id': 'PARC-001', 'nombre': 'Parcela_A_UrsuloGalvan', 'lat': 19.4008, 'lon': -96.3533, 'cultivo': 'Caña de Azúcar', 'area_base_ha': 12.5, 'ancho_m': 350.0, 'largo_m': 357.1, 'lai_base': 3.8},
    {'id': 'PARC-002', 'nombre': 'Parcela_B_UrsuloGalvan_Cítricos', 'lat': 19.4120, 'lon': -96.3610, 'cultivo': 'Limón Persa', 'area_base_ha': 8.2, 'ancho_m': 270.0, 'largo_m': 303.7, 'lai_base': 2.4},
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

def calcular_enlace_rf_915mhz(distancia_m, lai_follaje):
    p_tx = CONFIG_ENJAMBRE['potencia_tx_dbm']
    freq_mhz = CONFIG_ENJAMBRE['frecuencia_mhz']
    d_km = max(0.05, distancia_m / 1000.0)
    
    fspl_db = 32.44 + 20 * np.log10(freq_mhz) + 20 * np.log10(d_km)
    atenuacion_vegetacion_db = lai_follaje * 1.8
    rssi_dbm = round(p_tx - fspl_db - atenuacion_vegetacion_db + random.uniform(-1.5, 1.5), 1)
    
    piso_ruido_dbm = -105.0
    snr_db = round(rssi_dbm - piso_ruido_dbm, 1)
    perdida_paquetes_pct = round(max(0.0, min(100.0, (1.0 / (1.0 + np.exp((snr_db - 12.0) / 2.0))) * 100.0)), 1)
    return rssi_dbm, snr_db, perdida_paquetes_pct

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
    
    distancia_max_rf_m = np.sqrt((ancho_m / 2.0)**2 + (largo_m)**2)
    rssi_dbm, snr_db, perdida_paquetes_pct = calcular_enlace_rf_915mhz(distancia_max_rf_m, lai_actual)
    
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
        'cobertura_efectiva_pct': round(cobertura_efectiva_pct, 1),
        'rssi_dbm': rssi_dbm,
        'snr_db': snr_db,
        'perdida_paquetes_pct': perdida_paquetes_pct
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
        estado = '🟢 MONODRON ÓPTIMO (1 UAV)' if viento_kmh <= 26.0 else '🟡 ADVERTENCIA VIENTO MONODRON'
        mitigacion = f'Enlace RFD900x ({m["rssi_dbm"]} dBm / SNR {m["snr_db"]} dB). Pérdida MAVLink: {m["perdida_paquetes_pct"]}%.'
    else:
        estado = '🟢 ENJAMBRE ÓPTIMO (3 UAVs)' if viento_kmh <= 26.0 else '🟡 ADVERTENCIA VIENTO ENJAMBRE'
        mitigacion = f'Red Mesh 915 MHz activa ({m["rssi_dbm"]} dBm). Ahorro tiempo: {m["ahorro_tiempo_pct"]}%. Pérdida paquetes: {m["perdida_paquetes_pct"]}%.'

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
        'RSSI_dBm': m['rssi_dbm'],
        'SNR_dB': m['snr_db'],
        'Perdida_Paquetes_pct': m['perdida_paquetes_pct'],
        'Heading_Optimo_deg': heading_optimo,
        'Viento_kmh': round(viento_kmh, 1),
        'Fuente_API': fuente_api,
        'Estado_Operativo': estado,
        'Mitigacion_Aplicada': mitigacion
    }

def generar_reporte_markdown(df):
    df_rec = df.tail(10).iloc[::-1]
    md = [
        '# 📊 Reporte Industrial: Telemetría RF 915 MHz (2 Monodron + 1 Enjambre)',
        '**ELECTRÓNICA PERLACO — STR-002 H3 v3.0** | *Centro de Control MAVLink Swarm & Off-Grid Sync*',
        '',
        '### 📑 Matriz de Operaciones y Calidad de Enlace de Radiofrecuencia',
        '',
        '| Fecha UTC | Parcela | Drones | Dosis VRA | Tiempo Real | Ahorro % | RSSI (dBm) | SNR (dB) | Pérdida % | Estado |',
        '| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |'
    ]
    for _, r in df_rec.iterrows():
        n_uav = f"{int(r['Drones_Enjambre'])} UAV" if int(r['Drones_Enjambre']) == 1 else f"{int(r['Drones_Enjambre'])} UAVs"
        linea = f"| {r['Fecha_Hora_UTC']} | {r['Parcela']} | {n_uav} | {r['Dosis_VRA_L_ha']} L/ha | {r['Tiempo_Enjambre_min']} min | {r['Ahorro_Tiempo_pct']}% | {r['RSSI_dBm']} dBm | {r['SNR_dB']} dB | {r['Perdida_Paquetes_pct']}% | {r['Estado_Operativo']} |"
        md.append(linea)
    
    md.extend([
        '',
        '---',
        '**ELECTRÓNICA PERLACO / PERLACOLABS** — *Úrsulo Galván, Veracruz, México*'
    ])
    with open('docs/reportes/resumen_aprendizaje_diario.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

def ejecutar_simulacion():
    # Seleccionar 3 parcelas del catálogo regional
    parcelas = random.sample(CATALOGO_PARCELAS_VERACRUZ, 3)
    
    # 2 Simulaciones con 1 Dron (Monodron)
    res_m1 = simular_mision(parcelas[0], num_drones=1)
    res_m2 = simular_mision(parcelas[1], num_drones=1)
    
    # 1 Simulación con 3 Drones (Enjambre Multi-UAV)
    res_swarm = simular_mision(parcelas[2], num_drones=3)
    
    df_new = pd.DataFrame([res_m1, res_m2, res_swarm])
    log_file = 'simulation/historical_learning_log.csv'
    
    if os.path.exists(log_file) and os.path.getsize(log_file) > 100:
        try:
            df_old = pd.read_csv(log_file)
            df_tot = pd.concat([df_old, df_new], ignore_index=True)
        except Exception:
            df_tot = df_new
    else:
        df_tot = df_new

    df_tot['Drones_Enjambre'] = pd.to_numeric(df_tot['Drones_Enjambre'], errors='coerce').fillna(1).astype(int)
    df_tot['Tiempo_Monodron_min'] = pd.to_numeric(df_tot['Tiempo_Monodron_min'], errors='coerce').fillna(35.0)
    df_tot['Tiempo_Enjambre_min'] = pd.to_numeric(df_tot['Tiempo_Enjambre_min'], errors='coerce').fillna(13.2)
    df_tot['Ahorro_Tiempo_pct'] = pd.to_numeric(df_tot['Ahorro_Tiempo_pct'], errors='coerce').fillna(0.0)
    df_tot['RSSI_dBm'] = pd.to_numeric(df_tot['RSSI_dBm'], errors='coerce').fillna(-75.0)
    df_tot['SNR_dB'] = pd.to_numeric(df_tot['SNR_dB'], errors='coerce').fillna(30.0)
    df_tot['Perdida_Paquetes_pct'] = pd.to_numeric(df_tot['Perdida_Paquetes_pct'], errors='coerce').fillna(0.1)

    df_tot.to_csv(log_file, index=False)
    generar_reporte_markdown(df_tot)
    print('✅ Simulación de 3 misiones (2 Monodron + 1 Enjambre) completada.')

if __name__ == '__main__':
    ejecutar_simulacion()

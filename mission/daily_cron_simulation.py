# ==============================================================================
# PERLACOLABS - MOTOR GEOMATICO MULTI-API CON FISICA DE FOLLAJE Y ERRORES
# Autor: Angel Imer Lara Colorado - ELECTRONICA PERLACO / STR-002 H3 v3.0
# ==============================================================================

import urllib.request
import json
from datetime import datetime, timezone
import os
import numpy as np
import pandas as pd

OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', 'free_tier_demo_key')
AGROMONITORING_API_KEY = os.getenv('AGROMONITORING_API_KEY', 'free_tier_demo_key')

PARCELAS = [
    {
        'id': 'PARC-001',
        'nombre': 'Parcela_A_UrsuloGalvan',
        'lat': 19.4008,
        'lon': -96.3533,
        'cultivo': 'Cana de Azucar',
        'variante': 'CP 72-2086 (Cana Maura)',
        'area_ha': 12.5,
        'ancho_m': 350.0,
        'largo_m': 357.1,
        'lai_follaje': 3.8,
        'altura_dosel_m': 2.8,
        'sopa': 'Herbicida Nicosulfuron + Coadyuvante Siliconado',
        'salinidad_ec': 1.8
    },
    {
        'id': 'PARC-002',
        'nombre': 'Parcela_B_PasoDeOvejas',
        'lat': 19.2867,
        'lon': -96.4402,
        'cultivo': 'Citricos',
        'variante': 'Limon Persa Injertado',
        'area_ha': 8.2,
        'ancho_m': 270.0,
        'largo_m': 303.7,
        'lai_follaje': 2.4,
        'altura_dosel_m': 3.2,
        'sopa': 'Fungicida Foliar + Bioestimulante Zn-B + Buffer pH',
        'salinidad_ec': 2.4
    }
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
    url = f'https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M,WS2M,RH2M,ALLSKY_SFC_SW_DWN&community=AG&longitude={lon}&latitude={lat}&start={fecha_hoy}&end={fecha_hoy}&format=JSON'
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

def calcular_fisica_cobertura_y_errores(p, temp_c, viento_kmh, hr_pct):
    viento_ms = viento_kmh / 3.6
    ancho_m = p['ancho_m']
    largo_m = p['largo_m']
    lai = p['lai_follaje']
    altura_vuelo_efectiva = 3.5
    ancho_franja_m = 6.0
    overlap_pct = 25.0

    ancho_efectivo_m = ancho_m - 10.0
    num_pasadas = int(np.ceil(ancho_efectivo_m / (ancho_franja_m * (1.0 - overlap_pct / 100.0))))
    distancia_total_vuelo_m = (num_pasadas * largo_m) + (num_pasadas * ancho_franja_m)

    v_terminal_gota = 0.72
    tiempo_caida_s = altura_vuelo_efectiva / v_terminal_gota
    distancia_deriva_m = viento_ms * tiempo_caida_s
    vmd_optimo_um = 280.0 if (viento_ms > 4.0 or (temp_c / hr_pct) > 0.45) else 200.0

    k_extincion = 0.5
    efecto_downwash_x8 = 1.35
    penetracion_follaje_pct = min(100.0, np.exp(-k_extincion * lai) * 100.0 * efecto_downwash_x8)

    error_posicionamiento_rtk_m = 0.025
    error_deriva_pct = (distancia_deriva_m / ancho_franja_m) * 100.0
    error_caudal_bomba_pct = 2.5
    
    incertidumbre_total_pct = np.sqrt(error_deriva_pct**2 + error_caudal_bomba_pct**2 + (error_posicionamiento_rtk_m * 10.0)**2)
    cobertura_efectiva_pct = max(0.0, min(100.0, 100.0 - incertidumbre_total_pct * 0.4))

    return {
        'num_pasadas': num_pasadas,
        'distancia_vuelo_m': round(distancia_total_vuelo_m, 1),
        'distancia_deriva_m': round(distancia_deriva_m, 2),
        'vmd_optimo_um': vmd_optimo_um,
        'penetracion_follaje_pct': round(penetracion_follaje_pct, 1),
        'incertidumbre_total_pct': round(incertidumbre_total_pct, 2),
        'cobertura_efectiva_pct': round(cobertura_efectiva_pct, 1)
    }

def evaluar_y_simular_parcela(p):
    now_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    temp_c, viento_kmh, dir_deg, hr_pct, fuente_api = consultar_multi_api_meteo(p['lat'], p['lon'])
    fisica = calcular_fisica_cobertura_y_errores(p, temp_c, viento_kmh, hr_pct)

    viento_ms = viento_kmh / 3.6
    dosis_nominal = 10.0
    factor_vra = 1.0 + (max(0, viento_ms - 3.0) * 0.04) + ((temp_c / hr_pct) * 0.18)
    dosis_ajustada = dosis_nominal * factor_vra
    volumen_total_l = dosis_ajustada * p['area_ha']
    heading_optimo = (dir_deg + 90.0) % 360.0
    score_ventana = max(0.0, 100.0 - (viento_kmh * 2.2) - (fisica['distancia_deriva_m'] * 12.0))

    vmd_val = fisica['vmd_optimo_um']
    deriva_val = fisica['distancia_deriva_m']
    pasadas_val = fisica['num_pasadas']
    cob_val = fisica['cobertura_efectiva_pct']

    if 'FALLBACK' in fuente_api:
        estado = '🔴 INCIDENTE_API_FALLBACK'
        mitigacion = 'Modelo de redundancia regional activado sin detener mision.'
    elif viento_kmh > 26.0:
        estado = '🟡 ADVERTENCIA_VIENTO'
        mitigacion = f'Gota VMD ampliada a {vmd_val} um. Deriva compensada: {deriva_val}m.'
    else:
        estado = '🟢 OPTIMO'
        mitigacion = f'Trazado en {heading_optimo:.1f} deg con {pasadas_val} pasadas. Cobertura: {cob_val}%.'

    return {
        'Fecha_Hora_UTC': now_utc,
        'ID_Parcela': p['id'],
        'Parcela': p['nombre'],
        'Cultivo': p['cultivo'],
        'Area_ha': p['area_ha'],
        'LAI_Follaje': p['lai_follaje'],
        'Dosis_VRA_L_ha': round(dosis_ajustada, 2),
        'Volumen_Total_L': round(volumen_total_l, 1),
        'Pasadas_Vuelo': fisica['num_pasadas'],
        'Distancia_Vuelo_m': fisica['distancia_vuelo_m'],
        'Deriva_Eolica_m': fisica['distancia_deriva_m'],
        'Penetracion_Follaje_pct': fisica['penetracion_follaje_pct'],
        'Incertidumbre_Error_pct': fisica['incertidumbre_total_pct'],
        'Cobertura_Efectiva_pct': fisica['cobertura_efectiva_pct'],
        'Heading_Optimo_deg': round(heading_optimo, 1),
        'Viento_kmh': round(viento_kmh, 1),
        'Temp_C': round(temp_c, 1),
        'Score_Ventana_IA': round(score_ventana, 1),
        'Fuente_API': fuente_api,
        'Estado_Operativo': estado,
        'Mitigacion_Aplicada': mitigacion
    }

def generar_tabla_markdown(df):
    df_rec = df.tail(10).iloc[::-1]
    md = [
        '# 📊 Reporte Industrial Geomatico y Mitigacion de Incidencias en Tiempo Real',
        '**ELECTRONICA PERLACO - STR-002 H3 v3.0** | *Centro de Misiones Autonomas*',
        '',
        '### 📑 Registro Geometrico, Cobertura y Follaje por Parcela',
        '',
        '| Fecha UTC | Parcela | Cultivo | LAI Follaje | Dosis VRA | Pasadas | Deriva (m) | Penetracion | Cobertura % | Estado | API Source |',
        '| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |'
    ]
    for _, r in df_rec.iterrows():
        f_utc = r['Fecha_Hora_UTC']
        parc = r['Parcela']
        cult = r['Cultivo']
        lai_val = r['LAI_Follaje']
        dosis_val = r['Dosis_VRA_L_ha']
        pas_val = r['Pasadas_Vuelo']
        der_val = r['Deriva_Eolica_m']
        pen_val = r['Penetracion_Follaje_pct']
        cob_val = r['Cobertura_Efectiva_pct']
        est_val = r['Estado_Operativo']
        api_val = r['Fuente_API']
        linea = f'| {f_utc} | {parc} | {cult} | {lai_val} | {dosis_val} L/ha | {pas_val} | {der_val} m | {pen_val}% | {cob_val}% | {est_val} | {api_val} |'
        md.append(linea)
    
    md.extend([
        '',
        '---',
        '**ELECTRONICA PERLACO / PERLACOLABS** - *Ingenieria Agricola de Alta Precision*'
    ])
    salida_md = '\n'.join(md)
    with open('docs/reportes/resumen_aprendizaje_diario.md', 'w', encoding='utf-8') as f:
        f.write(salida_md)

def ejecutar_simulacion():
    res = [evaluar_y_simular_parcela(p) for p in PARCELAS]
    df_new = pd.DataFrame(res)
    log_file = 'simulation/historical_learning_log.csv'
    df_tot = pd.concat([pd.read_csv(log_file), df_new], ignore_index=True) if os.path.exists(log_file) else df_new
    df_tot.to_csv(log_file, index=False)
    generar_tabla_markdown(df_tot)
    print('✅ Simulacion geomatica ejecutada correctamente.')

if __name__ == '__main__':
    ejecutar_simulacion()

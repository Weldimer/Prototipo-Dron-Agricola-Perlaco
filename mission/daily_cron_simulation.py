# ==============================================================================
# PERLACOLABS - MOTOR DINÁMICO DE SIMULACIÓN Y ROTACIÓN DE PARCELAS VERACRUZ
# Autor: Angel Imer Lara Colorado - ELECTRÓNICA PERLACO / STR-002 H3 v3.0
# ==============================================================================

import urllib.request
import json
from datetime import datetime, timezone
import os
import random
import numpy as np
import pandas as pd

# Catálogo Ampliado de Zonas Agrícolas Reales de Veracruz
CATALOGO_PARCELAS_VERACRUZ = [
    {
        'id': 'PARC-001',
        'nombre': 'Parcela_A_UrsuloGalvan',
        'lat': 19.4008,
        'lon': -96.3533,
        'cultivo': 'Caña de Azúcar',
        'variante': 'CP 72-2086 (Caña Maura)',
        'area_base_ha': 12.5,
        'ancho_m': 350.0,
        'largo_m': 357.1,
        'lai_base': 3.8,
        'sopa': 'Herbicida Nicosulfurón + Coadyuvante'
    },
    {
        'id': 'PARC-002',
        'nombre': 'Parcela_B_PasoDeOvejas',
        'lat': 19.2867,
        'lon': -96.4402,
        'cultivo': 'Cítricos',
        'variante': 'Limón Persa Injertado',
        'area_base_ha': 8.2,
        'ancho_m': 270.0,
        'largo_m': 303.7,
        'lai_base': 2.4,
        'sopa': 'Fungicida Foliar + Bioestimulante Zn-B'
    },
    {
        'id': 'PARC-003',
        'nombre': 'Parcela_C_Actopan',
        'lat': 19.5011,
        'lon': -96.6152,
        'cultivo': 'Papaya',
        'variante': 'Maradol Roja',
        'area_base_ha': 6.5,
        'ancho_m': 200.0,
        'largo_m': 325.0,
        'lai_base': 3.1,
        'sopa': 'Insecticida Sistemático + Adherente'
    },
    {
        'id': 'PARC-004',
        'nombre': 'Parcela_D_LaAntigua',
        'lat': 19.3705,
        'lon': -96.3762,
        'cultivo': 'Maíz',
        'variante': 'Híbrido Blanco H-516',
        'area_base_ha': 15.0,
        'ancho_m': 300.0,
        'largo_m': 500.0,
        'lai_base': 3.5,
        'sopa': 'Fertilizante Foliar N-P-K + Zinc'
    },
    {
        'id': 'PARC-005',
        'nombre': 'Parcela_E_PuenteNacional',
        'lat': 19.3312,
        'lon': -96.4815,
        'cultivo': 'Mango',
        'variante': 'Manila de Exportación',
        'area_base_ha': 10.0,
        'ancho_m': 250.0,
        'largo_m': 400.0,
        'lai_base': 2.9,
        'sopa': 'Cúprico + Aminoácidos Foliares'
    },
    {
        'id': 'PARC-006',
        'nombre': 'Parcela_F_SoledadDeDoblado',
        'lat': 19.0438,
        'lon': -96.4211,
        'cultivo': 'Piña',
        'variante': 'MD2 Cayenne',
        'area_base_ha': 9.5,
        'ancho_m': 220.0,
        'largo_m': 431.8,
        'lai_base': 4.1,
        'sopa': 'Inductor de Floración + Boro'
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

def calcular_fisica_cobertura_y_errores(p, temp_c, viento_kmh, hr_pct, lai_actual):
    viento_ms = viento_kmh / 3.6
    ancho_m = p['ancho_m']
    largo_m = p['largo_m']
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
    penetracion_follaje_pct = min(100.0, np.exp(-k_extincion * lai_actual) * 100.0 * efecto_downwash_x8)

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
    
    # Micro-variación fenológica dinámica (simula crecimiento foliar y superficie)
    variacion_lai = round(random.uniform(-0.3, 0.4), 2)
    lai_dinamico = round(max(1.2, p['lai_base'] + variacion_lai), 2)
    
    variacion_area = round(random.uniform(-0.2, 0.3), 2)
    area_dinamica = round(max(3.0, p['area_base_ha'] + variacion_area), 2)

    temp_c, viento_kmh, dir_deg, hr_pct, fuente_api = consultar_multi_api_meteo(p['lat'], p['lon'])
    fisica = calcular_fisica_cobertura_y_errores(p, temp_c, viento_kmh, hr_pct, lai_dinamico)

    viento_ms = viento_kmh / 3.6
    dosis_nominal = 10.0
    factor_vra = 1.0 + (max(0, viento_ms - 3.0) * 0.04) + ((temp_c / hr_pct) * 0.18)
    dosis_ajustada = dosis_nominal * factor_vra
    volumen_total_l = dosis_ajustada * area_dinamica
    heading_optimo = (dir_deg + 90.0) % 360.0
    score_ventana = max(0.0, 100.0 - (viento_kmh * 2.2) - (fisica['distancia_deriva_m'] * 12.0))

    vmd_val = fisica['vmd_optimo_um']
    deriva_val = fisica['distancia_deriva_m']
    pasadas_val = fisica['num_pasadas']
    cob_val = fisica['cobertura_efectiva_pct']

    if 'FALLBACK' in fuente_api:
        estado = '🔴 INCIDENTE API FALLBACK'
        mitigacion = 'Modelo atmosférico de respaldo activado sin interrupción.'
    elif viento_kmh > 26.0:
        estado = '🟡 ADVERTENCIA VIENTO'
        mitigacion = f'Gota VMD a {vmd_val} µm. Deriva compensada: {deriva_val} m.'
    else:
        estado = '🟢 ÓPTIMO'
        mitigacion = f'Trazado en {heading_optimo:.1f}° con {pasadas_val} pasadas. Cobertura: {cob_val}%.'

    return {
        'Fecha_Hora_UTC': now_utc,
        'ID_Parcela': p['id'],
        'Parcela': p['nombre'],
        'Cultivo': p['cultivo'],
        'Area_ha': area_dinamica,
        'LAI_Follaje': lai_dinamico,
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
        '# 📊 Reporte Industrial Geomático y Mitigación de Incidencias en Tiempo Real',
        '**ELECTRÓNICA PERLACO — STR-002 H3 v3.0** | *Centro de Misiones Autónomas*',
        '',
        '### 📑 Registro Geométrico, Cobertura y Follaje por Parcela',
        '',
        '| Fecha UTC | Parcela | Cultivo | LAI Follaje | Dosis VRA | Pasadas | Deriva (m) | Penetración | Cobertura % | Estado | Fuente API |',
        '| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |'
    ]
    for _, r in df_rec.iterrows():
        f_utc = str(r['Fecha_Hora_UTC'])
        parc = str(r['Parcela'])
        cult = str(r['Cultivo'])
        lai_val = str(r['LAI_Follaje'])
        dosis_val = str(r['Dosis_VRA_L_ha'])
        pas_val = str(r['Pasadas_Vuelo'])
        der_val = str(r['Deriva_Eolica_m'])
        pen_val = str(r['Penetracion_Follaje_pct'])
        cob_val = str(r['Cobertura_Efectiva_pct'])
        est_val = str(r['Estado_Operativo'])
        api_val = str(r['Fuente_API'])
        linea = f'| {f_utc} | {parc} | {cult} | {lai_val} | {dosis_val} L/ha | {pas_val} | {der_val} m | {pen_val}% | {cob_val}% | {est_val} | {api_val} |'
        md.append(linea)
    
    md.extend([
        '',
        '---',
        '**ELECTRÓNICA PERLACO / PERLACOLABS** — *Ingeniería Agrícola de Alta Precisión*'
    ])
    salida_md = '\n'.join(md)
    with open('docs/reportes/resumen_aprendizaje_diario.md', 'w', encoding='utf-8') as f:
        f.write(salida_md)

def ejecutar_simulacion():
    # Seleccionar dinámicamente 2 parcelas distintas del catálogo en cada corrida
    parcelas_seleccionadas = random.sample(CATALOGO_PARCELAS_VERACRUZ, 2)
    
    res = [evaluar_y_simular_parcela(p) for p in parcelas_seleccionadas]
    df_new = pd.DataFrame(res)
    log_file = 'simulation/historical_learning_log.csv'
    
    os.makedirs('simulation', exist_ok=True)
    
    if os.path.exists(log_file) and os.path.getsize(log_file) > 100:
        try:
            df_old = pd.read_csv(log_file)
            df_tot = pd.concat([df_old, df_new], ignore_index=True)
        except Exception:
            df_tot = df_new
    else:
        df_tot = df_new

    # Reemplazo de datos faltantes para evitar arreglos vacíos en Plotly
    df_tot['LAI_Follaje'] = pd.to_numeric(df_tot['LAI_Follaje'], errors='coerce').fillna(3.0)
    df_tot['Pasadas_Vuelo'] = pd.to_numeric(df_tot['Pasadas_Vuelo'], errors='coerce').fillna(60).astype(int)
    df_tot['Deriva_Eolica_m'] = pd.to_numeric(df_tot['Deriva_Eolica_m'], errors='coerce').fillna(5.0)
    df_tot['Penetracion_Follaje_pct'] = pd.to_numeric(df_tot['Penetracion_Follaje_pct'], errors='coerce').fillna(50.0)
    df_tot['Cobertura_Efectiva_pct'] = pd.to_numeric(df_tot['Cobertura_Efectiva_pct'], errors='coerce').fillna(80.0)
    df_tot['Dosis_VRA_L_ha'] = pd.to_numeric(df_tot['Dosis_VRA_L_ha'], errors='coerce').fillna(10.0)
    df_tot['Viento_kmh'] = pd.to_numeric(df_tot['Viento_kmh'], errors='coerce').fillna(15.0)

    df_tot.to_csv(log_file, index=False)
    generar_tabla_markdown(df_tot)
    print('✅ Simulación de parcelas dinámicas completada.')

if __name__ == '__main__':
    ejecutar_simulacion()

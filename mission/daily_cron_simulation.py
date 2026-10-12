# ==============================================================================
# PERLACOLABS - MOTOR DE SIMULACIÓN MULTIPARCELA Y APRENDIZAJE DE CULTIVOS
# Ingesta climática en tiempo real, física de gota, salinidad y EMI
# Autor: Angel Imer Lara Colorado — ELECTRÓNICA PERLACO
# ==============================================================================

import urllib.request
import json
import datetime
import os
import numpy as np
import pandas as pd

# PARCELA A: Úrsulo Galván (Caña de Azúcar - CP 72-2086)
PARCELA_A = {'nombre': 'Parcela_A_UrsuloGalvan', 'lat': 19.4008, 'lon': -96.3533, 'cultivo': 'Caña de Azúcar', 'variante': 'CP 72-2086 (Caña Maura)', 'area_ha': 12.5, 'sopa': 'Herbicida Nicosulfurón + Coadyuvante Siliconado', 'salinidad_ec': 1.8}

# PARCELA B: Paso de Ovejas (Cítricos - Limón Persa)
PARCELA_B = {'nombre': 'Parcela_B_PasoDeOvejas', 'lat': 19.2867, 'lon': -96.4402, 'cultivo': 'Cítricos', 'variante': 'Limón Persa Injertado', 'area_ha': 8.2, 'sopa': 'Fungicida Foliar + Bioestimulante Zn-B + Buffer pH', 'salinidad_ec': 2.4}

def consultar_weather_api(lat, lon):
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&hourly=relativehumidity_2m,direct_normal_irradiance'
    try:
        req = urllib.request.urlopen(url, timeout=10)
        data = json.loads(req.read().decode('utf-8'))
        curr = data.get('current_weather', {})
        temp_c = curr.get('temperature', 28.5)
        viento_kmh = curr.get('windspeed', 16.0)
        dir_deg = curr.get('winddirection', 90.0)
        return temp_c, viento_kmh, dir_deg, 68.0, 18.5
    except Exception:
        return 30.0, 20.0, 85.0, 65.0, 19.0

def simular_parcela(p_info):
    now_utc = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    temp_c, viento_kmh, dir_deg, hr_pct, rad_solar = consultar_weather_api(p_info['lat'], p_info['lon'])

    viento_ms = viento_kmh / 3.6
    v_ground_ms = 5.0
    viento_transversal = viento_ms * 0.6
    crab_angle_deg = np.degrees(np.arcsin(np.clip(viento_transversal / 15.0, -0.8, 0.8)))

    delta_t = temp_c - (temp_c * (1 - hr_pct / 100.0) / 2.0)
    if viento_ms > 4.0 or delta_t > 8.0:
        vmd_gota_um = 280.0
    else:
        vmd_gota_um = 180.0

    dosis_nominal_l_ha = 10.0
    factor_vra = 1.0 + (max(0, viento_ms - 3.0) * 0.045) + ((temp_c / hr_pct) * 0.2)
    dosis_ajustada_l_ha = dosis_nominal_l_ha * factor_vra
    volumen_total_sopa_l = dosis_ajustada_l_ha * p_info['area_ha']

    vuelos_requeridos = int(np.ceil(volumen_total_sopa_l / 10.0))
    tiempo_vuelo_min = (p_info['area_ha'] * 2.5) + (vuelos_requeridos * 2.0)
    corriente_12s_prom_a = 160.0 + (viento_ms * 4.5)
    emi_level_ut = corriente_12s_prom_a * 0.42

    if 'Caña' in p_info['cultivo']:
        ndvi_sim = 0.82
        altura_densa_m = 2.80
    else:
        ndvi_sim = 0.74
        altura_densa_m = 1.90

    return {
        'Fecha_Hora_UTC': now_utc,
        'Parcela': p_info['nombre'],
        'Cultivo': p_info['cultivo'],
        'Variante': p_info['variante'],
        'Area_ha': p_info['area_ha'],
        'Sopa_Formulacion': p_info['sopa'],
        'Dosis_L_ha': dosis_ajustada_l_ha,
        'Volumen_Sopa_Total_L': volumen_total_sopa_l,
        'VMD_Gota_um': vmd_gota_um,
        'Tiempo_Vuelo_min': tiempo_vuelo_min,
        'Cambios_Bateria_12S': vuelos_requeridos,
        'Viento_kmh': viento_kmh,
        'Crab_Angle_deg': crab_angle_deg,
        'Temperatura_C': temp_c,
        'Humedad_Relativa_pct': hr_pct,
        'Radiacion_Solar_MJ': rad_solar,
        'Salinidad_Suelo_dS_m': p_info['salinidad_ec'],
        'Corriente_12S_A': corriente_12s_prom_a,
        'Interferencia_EMI_uT': emi_level_ut,
        'NDVI_Simulado': ndvi_sim,
        'Altura_Canopia_m': altura_densa_m
    }

def ejecutar_simulacion_diaria_dupla():
    res_a = simular_parcela(PARCELA_A)
    res_b = simular_parcela(PARCELA_B)

    df_dupla = pd.DataFrame([res_a, res_b])
    log_file = 'simulation/historical_learning_log.csv'
    file_exists = os.path.isfile(log_file)

    if file_exists:
        df_dupla.to_csv(log_file, mode='a', header=False, index=False)
    else:
        df_dupla.to_csv(log_file, mode='w', header=True, index=False)

    print("="*85)
    print("   🤖 PERLACOLABS: SIMULACIÓN MULTIPARCELA Y CULTIVOS REGISTRADA")
    print("="*85)
    for r in [res_a, res_b]:
        p_nom = r['Parcela']
        p_cul = r['Cultivo']
        p_var = r['Variante']
        p_area = r['Area_ha']
        p_dos = r['Dosis_L_ha']
        p_sop = r['Volumen_Sopa_Total_L']
        p_vmd = r['VMD_Gota_um']
        p_tie = r['Tiempo_Vuelo_min']
        p_rec = r['Cambios_Bateria_12S']
        p_vie = r['Viento_kmh']
        p_cra = r['Crab_Angle_deg']
        p_emi = r['Interferencia_EMI_uT']
        print(f"   📍 {p_nom} | {p_cul} ({p_var})")
        print(f"      ├─ Área: {p_area} ha | Dosis: {p_dos:.2f} L/ha | Sopa Total: {p_sop:.1f} L")
        print(f"      ├─ Gota VMD: {p_vmd} µm | Tiempo: {p_tie:.1f} min | Recargas 12S: {p_rec}")
        print(f"      └─ Viento: {p_vie:.1f} km/h (Crab: {p_cra:.1f}°) | EMI: {p_emi:.1f} µT")
    print("="*85)

if __name__ == '__main__':
    ejecutar_simulacion_diaria_dupla()

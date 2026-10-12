# ==============================================================================
# PERLACOLABS - MOTOR DE SIMULACIÓN CON IA PREDICTIVA Y GENERADOR QGC (.PLAN)
# Autor: Angel Imer Lara Colorado — ELECTRÓNICA PERLACO
# ==============================================================================

import urllib.request
import json
import datetime
import os
import numpy as np
import pandas as pd

PARCELA_A = {'nombre': 'Parcela_A_UrsuloGalvan', 'lat': 19.4008, 'lon': -96.3533, 'cultivo': 'Caña de Azúcar', 'variante': 'CP 72-2086 (Caña Maura)', 'area_ha': 12.5, 'sopa': 'Herbicida Nicosulfurón + Coadyuvante Siliconado', 'salinidad_ec': 1.8}
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

def generar_qgc_plan(p_info, dir_viento_deg):
    heading_optimo = (dir_viento_deg + 90.0) % 360.0
    plan_data = {
        'fileType': 'Plan',
        'version': 1,
        'groundStation': 'QGroundControl / PERLACOLABS',
        'mission': {
            'cruiseSpeed': 5.0,
            'firmwareType': 12,
            'hoverSpeed': 3.0,
            'items': [
                {'autoContinue': True, 'command': 16, 'frame': 3, 'params': [0, 0, 0, None, p_info['lat'], p_info['lon'], 3.5]},
                {'autoContinue': True, 'command': 178, 'frame': 2, 'params': [1, 5.0, -1, 0, 0, 0, 0]}
            ],
            'plannedHomePosition': [p_info['lat'], p_info['lon'], 15.0],
            'vehicleType': 2
        },
        'meta_info': {
            'parcela': p_info['nombre'],
            'heading_optimo_deg': heading_optimo,
            'cultivo': p_info['cultivo']
        }
    }
    p_nom = p_info['nombre']
    out_path = f'mission/generated_plans/{p_nom}_mision.plan'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(plan_data, f, indent=2)
    return out_path, heading_optimo

def simular_parcela(p_info):
    now_utc = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    temp_c, viento_kmh, dir_deg, hr_pct, rad_solar = consultar_weather_api(p_info['lat'], p_info['lon'])

    viento_ms = viento_kmh / 3.6
    viento_transversal = viento_ms * 0.6
    crab_angle_deg = np.degrees(np.arcsin(np.clip(viento_transversal / 15.0, -0.8, 0.8)))

    delta_t = temp_c - (temp_c * (1 - hr_pct / 100.0) / 2.0)
    vmd_gota_um = 280.0 if (viento_ms > 4.0 or delta_t > 8.0) else 180.0

    dosis_nominal_l_ha = 10.0
    factor_vra = 1.0 + (max(0, viento_ms - 3.0) * 0.045) + ((temp_c / hr_pct) * 0.2)
    dosis_ajustada_l_ha = dosis_nominal_l_ha * factor_vra
    volumen_total_sopa_l = dosis_ajustada_l_ha * p_info['area_ha']

    vuelos_requeridos = int(np.ceil(volumen_total_sopa_l / 10.0))
    tiempo_vuelo_min = (p_info['area_ha'] * 2.5) + (vuelos_requeridos * 2.0)
    corriente_12s_prom_a = 160.0 + (viento_ms * 4.5)
    emi_level_ut = corriente_12s_prom_a * 0.42

    score_ventana = max(0.0, 100.0 - (viento_kmh * 2.5) - (delta_t * 3.0))
    plan_file, heading_opt = generar_qgc_plan(p_info, dir_deg)

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
        'Heading_Optimo_deg': heading_opt,
        'Score_Ventana_IA_pct': score_ventana,
        'Temperatura_C': temp_c,
        'Humedad_Relativa_pct': hr_pct,
        'Radiacion_Solar_MJ': rad_solar,
        'Salinidad_Suelo_dS_m': p_info['salinidad_ec'],
        'Corriente_12S_A': corriente_12s_prom_a,
        'Interferencia_EMI_uT': emi_level_ut
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
    print("   🤖 PERLACOLABS: SIMULACIÓN IA Y MISIONES QGC GENERADAS")
    print("="*85)
    for r in [res_a, res_b]:
        p_nom, p_cul, p_var = r['Parcela'], r['Cultivo'], r['Variante']
        p_area, p_dos, p_sop = r['Area_ha'], r['Dosis_L_ha'], r['Volumen_Sopa_Total_L']
        p_head, p_score = r['Heading_Optimo_deg'], r['Score_Ventana_IA_pct']
        print(f"   📍 {p_nom} | {p_cul} ({p_var})")
        print(f"      ├─ Área: {p_area} ha | Dosis VRA: {p_dos:.2f} L/ha | Sopa: {p_sop:.1f} L")
        print(f"      └─ Heading Óptimo: {p_head:.1f}° | Score Ventana IA: {p_score:.1f}%")
    print("="*85)

if __name__ == '__main__':
    ejecutar_simulacion_diaria_dupla()

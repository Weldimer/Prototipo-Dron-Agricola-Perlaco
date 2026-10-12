# ==============================================================================
# PERLACOLABS - MOTOR DE APRENDIZAJE DE CAÑA DE AZÚCAR Y DOSIFICACIÓN VRA
# Modelado Botánico: Variedades de Caña, Etapas de Crecimiento y Sopa Líquida
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

# Catálogo Prioritario: Caña de Azúcar en Úrsulo Galván + Cultivos Secundarios
CATALOGO_PARCELAS_URSULO_GALVAN = [
    {
        'id': 'PARC-001',
        'nombre': 'Cañaveral_A_UrsuloGalvan_CP72',
        'lat': 19.4008,
        'lon': -96.3533,
        'tipo_planta': 'Gramínea C4 Perenne',
        'variedad': 'Caña CP 72-2086 (Predominante)',
        'altura_m': 3.10,
        'ancho_copa_m': 1.25,
        'tipo_hoja': 'Lanceolada / Cutícula Cera Gruesa',
        'tipo_raiz': 'Fasciculada Profunda (0.8–1.2 m)',
        'etapa_crecimiento': 'Gran Crecimiento / Cierre de Dosel',
        'factor_reten_hoja': 1.30,
        'area_base_ha': 14.5,
        'ancho_m': 380.0,
        'largo_m': 381.5,
        'lai_base': 4.2
    },
    {
        'id': 'PARC-002',
        'nombre': 'Cañaveral_B_UrsuloGalvan_MEX69',
        'lat': 19.4120,
        'lon': -96.3610,
        'tipo_planta': 'Gramínea C4 Perenne',
        'variedad': 'Caña Mex 69-290 (Alta Biomasa)',
        'altura_m': 2.10,
        'ancho_copa_m': 0.95,
        'tipo_hoja': 'Lanceolada Erguida / Pubescente',
        'tipo_raiz': 'Fasciculada Media (0.6–0.9 m)',
        'etapa_crecimiento': 'Macollo y Elongación Temprana',
        'factor_reten_hoja': 1.15,
        'area_base_ha': 11.2,
        'ancho_m': 310.0,
        'largo_m': 361.2,
        'lai_base': 3.1
    },
    {
        'id': 'PARC-003',
        'nombre': 'Cañaveral_C_UrsuloGalvan_ITV92',
        'lat': 19.3950,
        'lon': -96.3480,
        'tipo_planta': 'Gramínea C4 Perenne',
        'variedad': 'Caña ITV 92-1424 (Precoz)',
        'altura_m': 3.45,
        'ancho_copa_m': 1.35,
        'tipo_hoja': 'Lanceolada Ancha Péndula',
        'tipo_raiz': 'Fasciculada Profunda (>1.2 m)',
        'etapa_crecimiento': 'Maduración / Acumulación de Sacarosa',
        'factor_reten_hoja': 1.40,
        'area_base_ha': 16.0,
        'ancho_m': 400.0,
        'largo_m': 400.0,
        'lai_base': 4.6
    },
    {
        'id': 'PARC-004',
        'nombre': 'Cañaveral_D_UrsuloGalvan_L95',
        'lat': 19.4050,
        'lon': -96.3400,
        'tipo_planta': 'Gramínea C4 Perenne',
        'variedad': 'Caña L 95-096 (Plantilla)',
        'altura_m': 1.15,
        'ancho_copa_m': 0.65,
        'tipo_hoja': 'Lanceolada Fina Tierna',
        'tipo_raiz': 'Brote Fasicular Somero (0.3–0.5 m)',
        'etapa_crecimiento': 'Brote Vegetativo / Plantilla Joven',
        'factor_reten_hoja': 1.05,
        'area_base_ha': 8.5,
        'ancho_m': 250.0,
        'largo_m': 340.0,
        'lai_base': 2.1
    },
    {
        'id': 'PARC-005',
        'nombre': 'Parcela_E_UrsuloGalvan_Limón',
        'lat': 19.4080,
        'lon': -96.3700,
        'tipo_planta': 'Arbórea Rutácea Perennifolia',
        'variedad': 'Citrus latifolia (Limón Persa)',
        'altura_m': 3.20,
        'ancho_copa_m': 3.10,
        'tipo_hoja': 'Coriácea Brillante',
        'tipo_raiz': 'Pivotante con Febriles (0.6–1.5 m)',
        'etapa_crecimiento': 'Floración y Amarre de Fruto',
        'factor_reten_hoja': 1.10,
        'area_base_ha': 7.8,
        'ancho_m': 260.0,
        'largo_m': 300.0,
        'lai_base': 2.4
    },
    {
        'id': 'PARC-006',
        'nombre': 'Parcela_F_UrsuloGalvan_Papaya',
        'lat': 19.3900,
        'lon': -96.3600,
        'tipo_planta': 'Arbustiva Herbácea Gigante',
        'variedad': 'Carica papaya (Maradol Roja)',
        'altura_m': 2.50,
        'ancho_copa_m': 1.85,
        'tipo_hoja': 'Palmatilobulada Ancha',
        'tipo_raiz': 'Somera Pivotante Cerdosa (0.4–0.8 m)',
        'etapa_crecimiento': 'Desarrollo de Fruto',
        'factor_reten_hoja': 1.35,
        'area_base_ha': 6.2,
        'ancho_m': 200.0,
        'largo_m': 310.0,
        'lai_base': 3.1
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

def calcular_sopa_liquida_vra(p, temp_c, viento_kmh, hr_pct, lai_dinamico):
    viento_ms = viento_kmh / 3.6
    dosis_base_l_ha = 10.0
    factor_lai = lai_dinamico / 3.0
    factor_hoja = p['factor_reten_hoja']
    
    correccion_viento = max(0.0, (viento_ms - 2.5) * 0.05)
    correccion_termica = (temp_c / hr_pct) * 0.12
    
    dosis_sopa_l_ha = round(dosis_base_l_ha * factor_lai * factor_hoja * (1.0 + correccion_viento + correccion_termica), 2)
    volumen_total_sopa_l = round(dosis_sopa_l_ha * p['area_base_ha'], 1)
    
    v_terminal_gota = 0.72
    distancia_deriva_m = viento_ms * (3.5 / v_terminal_gota)
    vmd_optimo_um = 280.0 if (viento_ms > 4.0 or (temp_c / hr_pct) > 0.45) else 210.0

    k_extincion = 0.5
    penetracion_follaje_pct = round(min(100.0, np.exp(-k_extincion * lai_dinamico) * 100.0 * 1.45), 1)

    return dosis_sopa_l_ha, volumen_total_sopa_l, vmd_optimo_um, distancia_deriva_m, penetracion_follaje_pct

def calcular_matriz_operativa(p, temp_c, viento_kmh, hr_pct, lai_actual, num_drones):
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
    
    precision_rtk_mm = round(random.uniform(8.0, 12.0), 1)
    dosis_sopa, vol_sopa, vmd, deriva_m, penetracion_pct = calcular_sopa_liquida_vra(p, temp_c, viento_kmh, hr_pct, lai_actual)

    return {
        'num_drones': num_drones,
        'area_sector_ha': round(area_por_dron_ha, 2),
        'pasadas_por_dron': pasadas_por_dron,
        'tiempo_operativo_min': round(tiempo_operativo_min, 1),
        'ahorro_tiempo_pct': round(ahorro_tiempo_pct, 1),
        'precision_rtk_mm': precision_rtk_mm,
        'dosis_sopa_l_ha': dosis_sopa,
        'volumen_total_sopa_l': vol_sopa,
        'vmd_optimo_um': vmd,
        'distancia_deriva_m': round(deriva_m, 2),
        'penetracion_follaje_pct': penetracion_pct
    }

def simular_mision(p, num_drones):
    now_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    
    lai_dinamico = round(p['lai_base'] + random.uniform(-0.15, 0.20), 2)
    area_dinamica_ha = round(p['area_base_ha'] + random.uniform(-0.05, 0.10), 2)
    area_dinamica_m2 = round(area_dinamica_ha * 10000.0, 1)

    temp_c, viento_kmh, dir_deg, hr_pct, fuente_api = consultar_multi_api_meteo(p['lat'], p['lon'])
    
    m = calcular_matriz_operativa(p, temp_c, viento_kmh, hr_pct, lai_dinamico, num_drones)
    heading_optimo = round((dir_deg + 90.0) % 360.0, 1)

    if num_drones == 1:
        estado = '🟢 MONODRÓN ÓPTIMO (1 UAV)' if viento_kmh <= 26.0 else '🟡 ADVERTENCIA VIENTO MONODRÓN'
        mitigacion = f'Sopa Líquida VRA: {m["dosis_sopa_l_ha"]} L/ha. RTK: ±{m["precision_rtk_mm"]} mm. VMD {m["vmd_optimo_um"]} µm.'
    else:
        estado = '🟢 ENJAMBRE ÓPTIMO (3 UAVs)' if viento_kmh <= 26.0 else '🟡 ADVERTENCIA VIENTO ENJAMBRE'
        mitigacion = f'Sopa Líquida VRA: {m["dosis_sopa_l_ha"]} L/ha. Mesh 915 MHz activa. Ahorro tiempo: {m["ahorro_tiempo_pct"]}%.'

    return {
        'Fecha_Hora_UTC': now_utc,
        'ID_Parcela': p['id'],
        'Parcela': p['nombre'],
        'Latitud': p['lat'],
        'Longitud': p['lon'],
        'Tipo_Planta': p['tipo_planta'],
        'Variedad': p['variedad'],
        'Altura_m': p['altura_m'],
        'Ancho_Copa_m': p['ancho_copa_m'],
        'Tipo_Hoja': p['tipo_hoja'],
        'Tipo_Raiz': p['tipo_raiz'],
        'Etapa_Crecimiento': p['etapa_crecimiento'],
        'Area_ha': area_dinamica_ha,
        'Area_m2': area_dinamica_m2,
        'LAI_Follaje': lai_dinamico,
        'Drones_Enjambre': num_drones,
        'Precision_RTK_mm': m['precision_rtk_mm'],
        'Sopa_Liquida_L_ha': m['dosis_sopa_l_ha'],
        'Volumen_Sopa_L': m['volumen_total_sopa_l'],
        'VMD_Gota_um': m['vmd_optimo_um'],
        'Pasadas_Por_Dron': m['pasadas_por_dron'],
        'Tiempo_Operativo_min': m['tiempo_operativo_min'],
        'Ahorro_Tiempo_pct': m['ahorro_tiempo_pct'],
        'Penetracion_Follaje_pct': m['penetracion_follaje_pct'],
        'Heading_Optimo_deg': heading_optimo,
        'Viento_kmh': round(viento_kmh, 1),
        'Fuente_API': fuente_api,
        'Estado_Operativo': estado,
        'Mitigacion_Aplicada': mitigacion
    }

def generar_reporte_markdown(df):
    df_rec = df.tail(12).iloc[::-1]
    md = [
        '# 📊 Reporte Botánico de Caña de Azúcar y Sopa Líquida VRA en Úrsulo Galván',
        '**ELECTRÓNICA PERLACO — STR-002 H3 v3.0** | *Centro de Control Cañero & MAVLink Swarm*',
        '',
        '### 📑 Matriz Agronómica: Variedades de Caña, Fenología, Sopa Líquida (L/ha) y RTK',
        '',
        '| Fecha UTC | Parcela | Variedad de Caña / Cultivo | Altura / Copa | Etapa Fenológica | Drones | Sopa Líquida VRA | RTK Error | Estado |',
        '| :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :--- |'
    ]
    for _, r in df_rec.iterrows():
        n_uav = f"{int(r['Drones_Enjambre'])} UAV" if int(r['Drones_Enjambre']) == 1 else f"{int(r['Drones_Enjambre'])} UAVs"
        alt_copa = f"{r['Altura_m']} m / Ø{r['Ancho_Copa_m']} m"
        sopa_str = f"<b>{r['Sopa_Liquida_L_ha']} L/ha</b> ({r['Volumen_Sopa_L']} L tot)"
        rtk_str = f"±{r['Precision_RTK_mm']} mm"
        linea = f"| {r['Fecha_Hora_UTC']} | {r['Parcela']} | {r['Variedad']} | {alt_copa} | {r['Etapa_Crecimiento']} | {n_uav} | {sopa_str} | {rtk_str} | {r['Estado_Operativo']} |"
        md.append(linea)
    
    md.extend([
        '',
        '---',
        '**ELECTRÓNICA PERLACO / PERLACOLABS** — *Úrsulo Galván, Veracruz, México*'
    ])
    with open('docs/reportes/resumen_aprendizaje_diario.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

def ejecutar_simulacion():
    parcelas = random.sample(CATALOGO_PARCELAS_URSULO_GALVAN, len(CATALOGO_PARCELAS_URSULO_GALVAN))
    
    sims_monodron = [simular_mision(parcelas[i], num_drones=1) for i in range(4)]
    sims_enjambre = [simular_mision(parcelas[i], num_drones=3) for i in range(4, 6)]
    
    df_new = pd.DataFrame(sims_monodron + sims_enjambre)
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
    df_tot['Sopa_Liquida_L_ha'] = pd.to_numeric(df_tot['Sopa_Liquida_L_ha'], errors='coerce').fillna(10.0)
    df_tot['Volumen_Sopa_L'] = pd.to_numeric(df_tot['Volumen_Sopa_L'], errors='coerce').fillna(100.0)
    df_tot['Precision_RTK_mm'] = pd.to_numeric(df_tot['Precision_RTK_mm'], errors='coerce').fillna(10.0)
    df_tot['Tiempo_Operativo_min'] = pd.to_numeric(df_tot['Tiempo_Operativo_min'], errors='coerce').fillna(15.0)

    df_tot.to_csv(log_file, index=False)
    generar_reporte_markdown(df_tot)
    print('✅ Simulación cañera completada: 4x Monodrón + 2x Enjambre en Úrsulo Galván.')

if __name__ == '__main__':
    ejecutar_simulacion()

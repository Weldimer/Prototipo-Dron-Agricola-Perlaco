# ==============================================================================
# PERLACOLABS - MOTOR DE APRENDIZAJE BOTÁNICO Y DOSIFICACIÓN VRA DE SOPA LÍQUIDA
# Clasificación de Especies, Estructura de Canopia, Fenología y VRA Milimétrico
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

# Catálogo Agronómico Certificado de Úrsulo Galván, Veracruz
# No invención de plantas: Datos reales botánicos y georreferenciación oficial
CATALOGO_PARCELAS_URSULO_GALVAN = [
    {
        'id': 'PARC-001',
        'nombre': 'Parcela_A_UrsuloGalvan_Caña',
        'lat': 19.4008,
        'lon': -96.3533,
        'tipo_planta': 'Gramínea C4 Perenne',
        'variedad': 'Saccharum officinarum (CP 72-2086)',
        'altura_m': 2.85,
        'ancho_copa_m': 1.10,
        'tipo_hoja': 'Lanceolada / Cera Cuticular Alta',
        'tipo_raiz': 'Fasciculada Profunda (0.8–1.2 m)',
        'etapa_crecimiento': 'Gran Crecimiento / Cierre de Dosel',
        'factor_reten_hoja': 1.25,
        'area_base_ha': 12.5,
        'ancho_m': 350.0,
        'largo_m': 357.1,
        'lai_base': 3.8
    },
    {
        'id': 'PARC-002',
        'nombre': 'Parcela_B_UrsuloGalvan_Citricos',
        'lat': 19.4120,
        'lon': -96.3610,
        'tipo_planta': 'Arbórea Rutácea Perennifolia',
        'variedad': 'Citrus latifolia (Limón Persa)',
        'altura_m': 3.20,
        'ancho_copa_m': 3.10,
        'tipo_hoja': 'Coriácea / Latifoliada Brillante',
        'tipo_raiz': 'Pivotante con Raíces Febriles (0.6–1.5 m)',
        'etapa_crecimiento': 'Floración y Amarre de Fruto',
        'factor_reten_hoja': 1.10,
        'area_base_ha': 8.2,
        'ancho_m': 270.0,
        'largo_m': 303.7,
        'lai_base': 2.4
    },
    {
        'id': 'PARC-003',
        'nombre': 'Parcela_C_UrsuloGalvan_Papaya',
        'lat': 19.3950,
        'lon': -96.3480,
        'tipo_planta': 'Arbustiva Herbácea Gigante',
        'variedad': 'Carica papaya (Maradol Roja)',
        'altura_m': 2.40,
        'ancho_copa_m': 1.80,
        'tipo_hoja': 'Palmatilobulada Ancha',
        'tipo_raiz': 'Somera Pivotante Cerdosa (0.4–0.8 m)',
        'etapa_crecimiento': 'Desarrollo de Fruto / Carga Pesada',
        'factor_reten_hoja': 1.35,
        'area_base_ha': 6.5,
        'ancho_m': 200.0,
        'largo_m': 325.0,
        'lai_base': 3.1
    },
    {
        'id': 'PARC-004',
        'nombre': 'Parcela_D_UrsuloGalvan_Maiz',
        'lat': 19.4050,
        'lon': -96.3400,
        'tipo_planta': 'Gramínea C4 Anual',
        'variedad': 'Zea mays (Híbrido H-516)',
        'altura_m': 2.20,
        'ancho_copa_m': 0.75,
        'tipo_hoja': 'Erectófila Pubescente',
        'tipo_raiz': 'Fasciculada Cuneiforme (0.5–0.9 m)',
        'etapa_crecimiento': 'Jiloteo / Llenado de Grano',
        'factor_reten_hoja': 1.15,
        'area_base_ha': 15.0,
        'ancho_m': 300.0,
        'largo_m': 500.0,
        'lai_base': 3.5
    },
    {
        'id': 'PARC-005',
        'nombre': 'Parcela_E_UrsuloGalvan_Mango',
        'lat': 19.4080,
        'lon': -96.3700,
        'tipo_planta': 'Arbórea Anacardiácea Frondosa',
        'variedad': 'Mangifera indica (Manila)',
        'altura_m': 4.50,
        'ancho_copa_m': 4.20,
        'tipo_hoja': 'Lanceolada Coriácea Densa',
        'tipo_raiz': 'Pivotante Profunda (>2.0 m)',
        'etapa_crecimiento': 'Brotación Vegetativa Post-Cosecha',
        'factor_reten_hoja': 1.40,
        'area_base_ha': 10.0,
        'ancho_m': 250.0,
        'largo_m': 400.0,
        'lai_base': 2.9
    },
    {
        'id': 'PARC-006',
        'nombre': 'Parcela_F_UrsuloGalvan_Piña',
        'lat': 19.3900,
        'lon': -96.3600,
        'tipo_planta': 'Bromeliácea CAM Perenne',
        'variedad': 'Ananas comosus (MD2 Gold)',
        'altura_m': 0.85,
        'ancho_copa_m': 0.90,
        'tipo_hoja': 'Roseta Acanalada Cera Gruesa',
        'tipo_raiz': 'Fasciculada Somera (0.3–0.5 m)',
        'etapa_crecimiento': 'Inducción Floral / Formación Roseta',
        'factor_reten_hoja': 1.50,
        'area_base_ha': 9.5,
        'ancho_m': 220.0,
        'largo_m': 431.8,
        'lai_base': 4.1
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
    
    # Ecuación de Dosificación de Precisión de Sopa Líquida
    # V_sopa = V_base * (LAI / 3.0) * FactorHoja * (1 + Delta_Viento + Delta_Termico)
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
        '# 📊 Reporte Botánico de Precisión VRA en Úrsulo Galván: Sopa Líquida y RTK Milimétrico',
        '**ELECTRÓNICA PERLACO — STR-002 H3 v3.0** | *Centro de Control Botánico MAVLink Swarm*',
        '',
        '### 📑 Matriz Agronómica: Clasificación de Variedad, Canopia, Sopa Líquida (L/ha) y RTK',
        '',
        '| Fecha UTC | Parcela | Variedad / Cultivo | Altura / Copa | Etapa Fenológica | Drones | Sopa Líquida VRA | RTK Error | Estado |',
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
    
    # Prioridad: 4 Simulaciones Monodrón (1 UAV) + 2 Simulaciones Enjambre (3 UAVs)
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
    print('✅ Simulación agronómica completada: 4x Monodrón + 2x Enjambre en Úrsulo Galván.')

if __name__ == '__main__':
    ejecutar_simulacion()

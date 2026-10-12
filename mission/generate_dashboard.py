# ==============================================================================
# PERLACOLABS - DASHBOARD WEB Y GENERADOR PLOTLY
# Autor: Angel Imer Lara Colorado - ELECTRÓNICA PERLACO
# ==============================================================================
import pandas as pd
import json
import os

log_file = 'simulation/historical_learning_log.csv'

if not os.path.exists(log_file) or os.path.getsize(log_file) < 50:
    import daily_cron_simulation as sim
    sim.ejecutar_simulacion()

df = pd.read_csv(log_file)

df['Drones_Enjambre'] = pd.to_numeric(df['Drones_Enjambre'], errors='coerce').fillna(1).astype(int)
df['Area_ha'] = pd.to_numeric(df['Area_ha'], errors='coerce').fillna(10.0)
df['Area_m2'] = pd.to_numeric(df['Area_m2'], errors='coerce').fillna(100000.0)
df['Precision_RTK_mm'] = pd.to_numeric(df['Precision_RTK_mm'], errors='coerce').fillna(10.0)
df['Tiempo_Enjambre_min'] = pd.to_numeric(df['Tiempo_Enjambre_min'], errors='coerce').fillna(13.2)
df['RSSI_dBm'] = pd.to_numeric(df['RSSI_dBm'], errors='coerce').fillna(-75.0)

ultimos = df.tail(12).iloc[::-1]

filas_html = ''
for _, r in ultimos.iterrows():
    st = str(r.get('Estado_Operativo', '🟢 ÓPTIMO'))
    c_badge = '#238636' if ('ÓPTIMO' in st or 'OPTIMO' in st) else ('#d29922' if 'ADVERTENCIA' in st else '#da3633')
    f_utc = str(r['Fecha_Hora_UTC'])
    parc = str(r['Parcela'])
    coords = f"{r.get('Latitud', 19.4008)}, {r.get('Longitud', -96.3533)}"
    area_str = f"<b>{r['Area_ha']} ha</b> ({r['Area_m2']:,.0f} m²)"
    rtk_str = f"<b style='color:#a371f7;'>±{r['Precision_RTK_mm']} mm</b>"
    n_drones = int(r['Drones_Enjambre'])
    badge_dron = f'<b style="color:#2ea043;">1 UAV (Monodrón)</b>' if n_drones == 1 else f'<b style="color:#58a6ff;">{n_drones} UAVs (Enjambre)</b>'
    dosis = round(float(r['Dosis_VRA_L_ha']), 2)
    t_real = round(float(r['Tiempo_Enjambre_min']), 1)
    
    filas_html += f'<tr><td>{f_utc}</td><td><b>{parc}</b></td><td>{coords}</td><td>{area_str}</td><td>{badge_dron}</td><td>{rtk_str}</td><td>{dosis} L/ha</td><td><b>{t_real} min</b></td><td><span style="background-color:{c_badge}; color:white; padding:3px 8px; border-radius:12px; font-size:11px;">{st}</span></td></tr>'

fechas_json = json.dumps(list(df['Fecha_Hora_UTC'].tail(18)))
tiempo_real_json = json.dumps([round(float(x), 1) for x in list(df['Tiempo_Enjambre_min'].tail(18))])
area_m2_json = json.dumps([round(float(x), 0) for x in list(df['Area_m2'].tail(18))])
rtk_mm_json = json.dumps([round(float(x), 1) for x in list(df['Precision_RTK_mm'].tail(18))])

html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>PERLACOLABS - Dashboard STR-002 H3 v3.0</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background-color: #0d1117; color: #c9d1d9; margin: 0; padding: 20px; }}
        .header {{ text-align: center; border-bottom: 1px solid #30363d; padding-bottom: 15px; margin-bottom: 20px; }}
        .header h1 {{ color: #58a6ff; margin: 0; }}
        .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px; }}
        .card {{ background-color: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 15px; }}
        table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
        th {{ background-color: #21262d; color: #8b949e; padding: 8px; text-align: left; }}
        td {{ padding: 8px; border-bottom: 1px solid #21262d; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🚁 ELECTRÓNICA PERLACO - STR-002 H3 v3.0</h1>
        <p><b>Centro de Misiones Autónomas, RTK Milimétrico y Operaciones (4x Monodrón + 2x Enjambre)</b></p>
    </div>
    
    <div class="grid">
        <div class="card"><div id="chart_m2"></div></div>
        <div class="card"><div id="chart_rtk"></div></div>
    </div>
    
    <div class="card">
        <h3>📑 Registros de Misiones: Latitud, Longitud, Área (m²) y Precisión RTK (mm)</h3>
        <table>
            <thead>
                <tr><th>Fecha UTC</th><th>Parcela</th><th>Coordenadas Lat, Lon</th><th>Área Total</th><th>Configuración</th><th>Precisión RTK</th><th>Dosis VRA</th><th>Tiempo Real</th><th>Estado</th></tr>
            </thead>
            <tbody>{filas_html}</tbody>
        </table>
    </div>

    <script>
        var trace1 = {{ x: {fechas_json}, y: {area_m2_json}, name: 'Área Total Trabajada (m²)', type: 'bar', marker: {{color: '#2ea043'}} }};
        Plotly.newPlot('chart_m2', [trace1], {{ title: 'Área Total de Parcela Traza/Trabajada (m²)', paper_bgcolor: '#161b22', plot_bgcolor: '#161b22', font: {{color: '#c9d1d9'}} }});

        var trace2 = {{ x: {fechas_json}, y: {rtk_mm_json}, name: 'Error RTK (mm RMS)', type: 'scatter', mode: 'lines+markers', line: {{color: '#a371f7'}} }};
        Plotly.newPlot('chart_rtk', [trace2], {{ title: 'Precisión Milimétrica de Navegación RTK Moving Baseline (mm RMS)', paper_bgcolor: '#161b22', plot_bgcolor: '#161b22', font: {{color: '#c9d1d9'}}, yaxis: {{title: 'Error (mm)'}} }});
    </script>
</body>
</html>'''

with open('docs/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print('✅ Páginas HTML de Dashboard actualizadas.')

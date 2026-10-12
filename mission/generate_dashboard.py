# ==============================================================================
# PERLACOLABS - DASHBOARD WEB Y GENERADOR PLOTLY PARA ENJAMBRES
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

df['Drones_Enjambre'] = pd.to_numeric(df['Drones_Enjambre'], errors='coerce').fillna(3).astype(int)
df['Tiempo_Monodron_min'] = pd.to_numeric(df['Tiempo_Monodron_min'], errors='coerce').fillna(35.0)
df['Tiempo_Enjambre_min'] = pd.to_numeric(df['Tiempo_Enjambre_min'], errors='coerce').fillna(13.2)
df['Ahorro_Tiempo_pct'] = pd.to_numeric(df['Ahorro_Tiempo_pct'], errors='coerce').fillna(62.3)
df['LAI_Follaje'] = pd.to_numeric(df['LAI_Follaje'], errors='coerce').fillna(3.0)
df['Dosis_VRA_L_ha'] = pd.to_numeric(df['Dosis_VRA_L_ha'], errors='coerce').fillna(10.5)
df['Pasadas_Por_Dron'] = pd.to_numeric(df['Pasadas_Por_Dron'], errors='coerce').fillna(20).astype(int)
df['Deriva_Eolica_m'] = pd.to_numeric(df['Deriva_Eolica_m'], errors='coerce').fillna(6.5)
df['Penetracion_Follaje_pct'] = pd.to_numeric(df['Penetracion_Follaje_pct'], errors='coerce').fillna(40.0)
df['Cobertura_Efectiva_pct'] = pd.to_numeric(df['Cobertura_Efectiva_pct'], errors='coerce').fillna(55.0)

ultimos = df.tail(10).iloc[::-1]

filas_html = ''
for _, r in ultimos.iterrows():
    st = str(r.get('Estado_Operativo', '🟢 ENJAMBRE ÓPTIMO'))
    c_badge = '#238636' if ('ÓPTIMO' in st or 'OPTIMO' in st) else ('#d29922' if 'ADVERTENCIA' in st else '#da3633')
    f_utc = str(r['Fecha_Hora_UTC'])
    parc = str(r['Parcela'])
    cult = str(r['Cultivo'])
    n_drones = int(r['Drones_Enjambre'])
    dosis = round(float(r['Dosis_VRA_L_ha']), 2)
    t_mono = round(float(r['Tiempo_Monodron_min']), 1)
    t_swarm = round(float(r['Tiempo_Enjambre_min']), 1)
    ahorro = round(float(r['Ahorro_Tiempo_pct']), 1)
    filas_html += f'<tr><td>{f_utc}</td><td><b>{parc}</b></td><td>{cult}</td><td><b style="color:#58a6ff;">{n_drones} UAVs</b></td><td>{dosis} L/ha</td><td>{t_mono} min</td><td><b style="color:#3fb950;">{t_swarm} min</b></td><td><b>{ahorro}%</b></td><td><span style="background-color:{c_badge}; color:white; padding:3px 8px; border-radius:12px; font-size:11px;">{st}</span></td></tr>'

fechas_json = json.dumps(list(df['Fecha_Hora_UTC'].tail(15)))
tiempo_mono_json = json.dumps([round(float(x), 1) for x in list(df['Tiempo_Monodron_min'].tail(15))])
tiempo_swarm_json = json.dumps([round(float(x), 1) for x in list(df['Tiempo_Enjambre_min'].tail(15))])
ahorro_json = json.dumps([round(float(x), 1) for x in list(df['Ahorro_Tiempo_pct'].tail(15))])

html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>PERLACOLABS - Dashboard Swarm STR-002 H3 v3.0</title>
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
        <h1>🐝 ELECTRÓNICA PERLACO - ARQUITECTURA DE ENJAMBRE STR-002 H3 v3.0</h1>
        <p><b>Centro de Misiones Autónomas Multi-UAV, MAVLink Swarm & Partición Espacial</b></p>
    </div>
    
    <div class="grid">
        <div class="card"><div id="chart_tiempos"></div></div>
        <div class="card"><div id="chart_ahorro"></div></div>
    </div>
    
    <div class="card">
        <h3>📑 Registro de Operaciones en Enjambre (Monodron vs Multi-UAV)</h3>
        <table>
            <thead>
                <tr><th>Fecha UTC</th><th>Parcela</th><th>Cultivo</th><th>Enjambre</th><th>Dosis VRA</th><th>Tiempo Mono</th><th>Tiempo Swarm</th><th>Ahorro %</th><th>Estado</th></tr>
            </thead>
            <tbody>{filas_html}</tbody>
        </table>
    </div>

    <script>
        var trace1 = {{ x: {fechas_json}, y: {tiempo_mono_json}, name: 'Tiempo Monodron (min)', type: 'scatter', mode: 'lines+markers', line: {{color: '#f85149'}} }};
        var trace2 = {{ x: {fechas_json}, y: {tiempo_swarm_json}, name: 'Tiempo Enjambre (min)', type: 'scatter', mode: 'lines+markers', line: {{color: '#2ea043'}} }};
        Plotly.newPlot('chart_tiempos', [trace1, trace2], {{ title: 'Comparativa Tiempo de Misión: Monodron vs Enjambre (min)', paper_bgcolor: '#161b22', plot_bgcolor: '#161b22', font: {{color: '#c9d1d9'}} }});

        var trace3 = {{ x: {fechas_json}, y: {ahorro_json}, name: 'Ahorro de Tiempo (%)', type: 'bar', marker: {{color: '#58a6ff'}} }};
        Plotly.newPlot('chart_ahorro', [trace3], {{ title: 'Eficiencia de Operación y Ahorro de Tiempo (%)', paper_bgcolor: '#161b22', plot_bgcolor: '#161b22', font: {{color: '#c9d1d9'}}, yaxis: {{title: 'Ahorro %'}} }});
    </script>
</body>
</html>'''

with open('docs/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print('✅ Páginas HTML de Dashboard Swarm (index.html y dashboard.html) generadas correctamente.')

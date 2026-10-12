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

# Limpiar cualquier texto corrupto residual
df = df[~df.astype(str).apply(lambda r: r.str.contains('yaya', case=False)).any(axis=1)].copy()

# Convertir tipos explícitamente para asegurar arreglos válidos para Plotly
df['LAI_Follaje'] = pd.to_numeric(df['LAI_Follaje'], errors='coerce').fillna(3.0)
df['Dosis_VRA_L_ha'] = pd.to_numeric(df['Dosis_VRA_L_ha'], errors='coerce').fillna(10.5)
df['Pasadas_Vuelo'] = pd.to_numeric(df['Pasadas_Vuelo'], errors='coerce').fillna(60).astype(int)
df['Deriva_Eolica_m'] = pd.to_numeric(df['Deriva_Eolica_m'], errors='coerce').fillna(6.5)
df['Penetracion_Follaje_pct'] = pd.to_numeric(df['Penetracion_Follaje_pct'], errors='coerce').fillna(40.0)
df['Cobertura_Efectiva_pct'] = pd.to_numeric(df['Cobertura_Efectiva_pct'], errors='coerce').fillna(55.0)
df['Viento_kmh'] = pd.to_numeric(df['Viento_kmh'], errors='coerce').fillna(16.0)

ultimos = df.tail(10).iloc[::-1]

filas_html = ''
for _, r in ultimos.iterrows():
    st = str(r.get('Estado_Operativo', '🟢 ÓPTIMO'))
    c_badge = '#238636' if ('ÓPTIMO' in st or 'OPTIMO' in st) else ('#d29922' if 'ADVERTENCIA' in st else '#da3633')
    lai_val = round(float(r['LAI_Follaje']), 1)
    f_utc = str(r['Fecha_Hora_UTC'])
    parc = str(r['Parcela'])
    cult = str(r['Cultivo'])
    dosis = round(float(r['Dosis_VRA_L_ha']), 2)
    pasadas = int(r['Pasadas_Vuelo'])
    deriva = round(float(r['Deriva_Eolica_m']), 2)
    penetracion = round(float(r['Penetracion_Follaje_pct']), 1)
    filas_html += f'<tr><td>{f_utc}</td><td><b>{parc}</b></td><td>{cult} (LAI {lai_val})</td><td>{dosis} L/ha</td><td>{pasadas} pasadas</td><td>{deriva} m</td><td><b>{penetracion}%</b></td><td><span style="background-color:{c_badge}; color:white; padding:3px 8px; border-radius:12px; font-size:11px;">{st}</span></td></tr>'

fechas_json = json.dumps(list(df['Fecha_Hora_UTC'].tail(15)))
penetracion_json = json.dumps([round(float(x), 1) for x in list(df['Penetracion_Follaje_pct'].tail(15))])
cobertura_json = json.dumps([round(float(x), 1) for x in list(df['Cobertura_Efectiva_pct'].tail(15))])
viento_json = json.dumps([round(float(x), 1) for x in list(df['Viento_kmh'].tail(15))])
deriva_json = json.dumps([round(float(x), 2) for x in list(df['Deriva_Eolica_m'].tail(15))])

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
        <p><b>Centro de Misiones Autónomas, Simulación Geomática y Penetración Folio-Atmosférica</b></p>
    </div>
    
    <div class="grid">
        <div class="card"><div id="chart_cobertura"></div></div>
        <div class="card"><div id="chart_deriva"></div></div>
    </div>
    
    <div class="card">
        <h3>📑 Histórico Geométrico y Registros de Misión</h3>
        <table>
            <thead>
                <tr><th>Fecha UTC</th><th>Parcela</th><th>Cultivo / LAI</th><th>Dosis VRA</th><th>Pasadas</th><th>Deriva</th><th>Penetración Follaje</th><th>Estado</th></tr>
            </thead>
            <tbody>{filas_html}</tbody>
        </table>
    </div>

    <script>
        var trace1 = {{ x: {fechas_json}, y: {penetracion_json}, name: 'Penetración Follaje %', type: 'scatter', mode: 'lines+markers', line: {{color: '#2ea043'}} }};
        var trace2 = {{ x: {fechas_json}, y: {cobertura_json}, name: 'Cobertura Efectiva %', type: 'scatter', mode: 'lines+markers', line: {{color: '#58a6ff'}} }};
        Plotly.newPlot('chart_cobertura', [trace1, trace2], {{ title: 'Penetración Folio-Atmosférica vs Cobertura Efectiva (%)', paper_bgcolor: '#161b22', plot_bgcolor: '#161b22', font: {{color: '#c9d1d9'}} }});

        var trace3 = {{ x: {viento_json}, y: {deriva_json}, mode: 'markers', marker: {{size: 12, color: '#f85149'}}, type: 'scatter' }};
        Plotly.newPlot('chart_deriva', [trace3], {{ title: 'Deriva Eólica de Gota (m) en Función del Viento (km/h)', paper_bgcolor: '#161b22', plot_bgcolor: '#161b22', font: {{color: '#c9d1d9'}}, xaxis: {{title: 'Viento (km/h)'}}, yaxis: {{title: 'Deriva (m)'}} }});
    </script>
</body>
</html>'''

with open('docs/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print('✅ Páginas HTML de Dashboard (index.html y dashboard.html) generadas correctamente con datos.')

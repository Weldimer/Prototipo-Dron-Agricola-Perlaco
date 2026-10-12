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
df['Tiempo_Monodron_min'] = pd.to_numeric(df['Tiempo_Monodron_min'], errors='coerce').fillna(35.0)
df['Tiempo_Enjambre_min'] = pd.to_numeric(df['Tiempo_Enjambre_min'], errors='coerce').fillna(13.2)
df['Ahorro_Tiempo_pct'] = pd.to_numeric(df['Ahorro_Tiempo_pct'], errors='coerce').fillna(0.0)
df['RSSI_dBm'] = pd.to_numeric(df['RSSI_dBm'], errors='coerce').fillna(-75.0)
df['SNR_dB'] = pd.to_numeric(df['SNR_dB'], errors='coerce').fillna(30.0)

ultimos = df.tail(10).iloc[::-1]

filas_html = ''
for _, r in ultimos.iterrows():
    st = str(r.get('Estado_Operativo', '🟢 ÓPTIMO'))
    c_badge = '#238636' if ('ÓPTIMO' in st or 'OPTIMO' in st) else ('#d29922' if 'ADVERTENCIA' in st else '#da3633')
    f_utc = str(r['Fecha_Hora_UTC'])
    parc = str(r['Parcela'])
    cult = str(r['Cultivo'])
    n_drones = int(r['Drones_Enjambre'])
    badge_dron = f'<b style="color:#a371f7;">1 UAV (Monodron)</b>' if n_drones == 1 else f'<b style="color:#58a6ff;">{n_drones} UAVs (Enjambre)</b>'
    dosis = round(float(r['Dosis_VRA_L_ha']), 2)
    t_real = round(float(r['Tiempo_Enjambre_min']), 1)
    rssi = round(float(r['RSSI_dBm']), 1)
    snr = round(float(r['SNR_dB']), 1)
    filas_html += f'<tr><td>{f_utc}</td><td><b>{parc}</b></td><td>{cult}</td><td>{badge_dron}</td><td>{dosis} L/ha</td><td><b style="color:#3fb950;">{t_real} min</b></td><td>{rssi} dBm</td><td><b>{snr} dB</b></td><td><span style="background-color:{c_badge}; color:white; padding:3px 8px; border-radius:12px; font-size:11px;">{st}</span></td></tr>'

fechas_json = json.dumps(list(df['Fecha_Hora_UTC'].tail(15)))
tiempo_real_json = json.dumps([round(float(x), 1) for x in list(df['Tiempo_Enjambre_min'].tail(15))])
rssi_json = json.dumps([round(float(x), 1) for x in list(df['RSSI_dBm'].tail(15))])
snr_json = json.dumps([round(float(x), 1) for x in list(df['SNR_dB'].tail(15))])

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
        <p><b>Centro de Misiones Autónomas, Telemetría RF 915 MHz Off-Grid y Enjambres</b></p>
    </div>
    
    <div class="grid">
        <div class="card"><div id="chart_tiempos"></div></div>
        <div class="card"><div id="chart_rf"></div></div>
    </div>
    
    <div class="card">
        <h3>📑 Histórico de Misiones (2 Monodron + 1 Enjambre)</h3>
        <table>
            <thead>
                <tr><th>Fecha UTC</th><th>Parcela</th><th>Cultivo</th><th>Configuración</th><th>Dosis VRA</th><th>Tiempo Real</th><th>RSSI (dBm)</th><th>SNR (dB)</th><th>Estado</th></tr>
            </thead>
            <tbody>{filas_html}</tbody>
        </table>
    </div>

    <script>
        var trace1 = {{ x: {fechas_json}, y: {tiempo_real_json}, name: 'Tiempo de Vuelo Real (min)', type: 'scatter', mode: 'lines+markers', line: {{color: '#2ea043'}} }};
        Plotly.newPlot('chart_tiempos', [trace1], {{ title: 'Duración Real de Misiones Ejecutadas (min)', paper_bgcolor: '#161b22', plot_bgcolor: '#161b22', font: {{color: '#c9d1d9'}} }});

        var trace2 = {{ x: {fechas_json}, y: {rssi_json}, name: 'Potencia RSSI (dBm)', type: 'scatter', mode: 'lines+markers', line: {{color: '#58a6ff'}} }};
        var trace3 = {{ x: {fechas_json}, y: {snr_json}, name: 'Relación SNR (dB)', type: 'scatter', mode: 'lines+markers', line: {{color: '#a371f7'}} }};
        Plotly.newPlot('chart_rf', [trace2, trace3], {{ title: 'Calidad de Enlace RF 915 MHz Off-Grid (RSSI / SNR)', paper_bgcolor: '#161b22', plot_bgcolor: '#161b22', font: {{color: '#c9d1d9'}} }});
    </script>
</body>
</html>'''

with open('docs/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print('✅ Páginas HTML de Dashboard actualizadas.')

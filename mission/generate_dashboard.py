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
df['Sopa_Liquida_L_ha'] = pd.to_numeric(df['Sopa_Liquida_L_ha'], errors='coerce').fillna(10.0)
df['Precision_RTK_mm'] = pd.to_numeric(df['Precision_RTK_mm'], errors='coerce').fillna(10.0)
df['Tiempo_Operativo_min'] = pd.to_numeric(df['Tiempo_Operativo_min'], errors='coerce').fillna(15.0)

ultimos = df.tail(12).iloc[::-1]

filas_html = ''
for _, r in ultimos.iterrows():
    st = str(r.get('Estado_Operativo', '🟢 ÓPTIMO'))
    c_badge = '#238636' if ('ÓPTIMO' in st or 'OPTIMO' in st) else ('#d29922' if 'ADVERTENCIA' in st else '#da3633')
    f_utc = str(r['Fecha_Hora_UTC'])
    parc = str(r['Parcela'])
    var_str = str(r.get('Variedad', 'Cultivo Regional'))
    alt_copa = f"{r.get('Altura_m', 2.5)} m / Ø{r.get('Ancho_Copa_m', 1.5)} m"
    sopa_str = f"<b style='color:#3fb950;'>{r['Sopa_Liquida_L_ha']} L/ha</b>"
    rtk_str = f"<b style='color:#a371f7;'>±{r['Precision_RTK_mm']} mm</b>"
    n_drones = int(r['Drones_Enjambre'])
    badge_dron = f'<b style="color:#2ea043;">1 UAV (Monodrón)</b>' if n_drones == 1 else f'<b style="color:#58a6ff;">{n_drones} UAVs (Enjambre)</b>'
    t_real = round(float(r['Tiempo_Operativo_min']), 1)
    
    filas_html += f'<tr><td>{f_utc}</td><td><b>{parc}</b></td><td>{var_str}</td><td>{alt_copa}</td><td>{badge_dron}</td><td>{sopa_str}</td><td>{rtk_str}</td><td><b>{t_real} min</b></td><td><span style="background-color:{c_badge}; color:white; padding:3px 8px; border-radius:12px; font-size:11px;">{st}</span></td></tr>'

fechas_json = json.dumps(list(df['Fecha_Hora_UTC'].tail(18)))
sopa_json = json.dumps([round(float(x), 2) for x in list(df['Sopa_Liquida_L_ha'].tail(18))])
rtk_mm_json = json.dumps([round(float(x), 1) for x in list(df['Precision_RTK_mm'].tail(18))])

html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>PERLACOLABS - Dashboard Botánico STR-002 H3 v3.0</title>
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
        <p><b>Centro de Misiones Botánicas: Dosificación VRA de Sopa Líquida y RTK Milimétrico</b></p>
    </div>
    
    <div class="grid">
        <div class="card"><div id="chart_sopa"></div></div>
        <div class="card"><div id="chart_rtk"></div></div>
    </div>
    
    <div class="card">
        <h3>📑 Registros Botánicos de Misión: Variedad, Estructura de Canopia, Sopa Líquida y RTK</h3>
        <table>
            <thead>
                <tr><th>Fecha UTC</th><th>Parcela</th><th>Variedad Certificada</th><th>Altura / Copa</th><th>Configuración</th><th>Sopa Líquida VRA</th><th>Precisión RTK</th><th>Tiempo Real</th><th>Estado</th></tr>
            </thead>
            <tbody>{filas_html}</tbody>
        </table>
    </div>

    <script>
        var trace1 = {{ x: {fechas_json}, y: {sopa_json}, name: 'Dosificación Sopa Líquida (L/ha)', type: 'bar', marker: {{color: '#2ea043'}} }};
        Plotly.newPlot('chart_sopa', [trace1], {{ title: 'Dosificación VRA de Sopa Líquida según Estructura Botánica (L/ha)', paper_bgcolor: '#161b22', plot_bgcolor: '#161b22', font: {{color: '#c9d1d9'}}, yaxis: {{title: 'Dosis (L/ha)'}} }});

        var trace2 = {{ x: {fechas_json}, y: {rtk_mm_json}, name: 'Error RTK (mm RMS)', type: 'scatter', mode: 'lines+markers', line: {{color: '#a371f7'}} }};
        Plotly.newPlot('chart_rtk', [trace2], {{ title: 'Navegación RTK Moving Baseline Milimétrica (mm RMS)', paper_bgcolor: '#161b22', plot_bgcolor: '#161b22', font: {{color: '#c9d1d9'}}, yaxis: {{title: 'Error (mm)'}} }});
    </script>
</body>
</html>'''

with open('docs/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print('✅ Páginas HTML de Dashboard actualizadas con dosificación VRA de Sopa Líquida.')

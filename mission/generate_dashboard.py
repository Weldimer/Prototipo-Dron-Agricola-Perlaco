# ==============================================================================
# PERLACOLABS - DASHBOARD WEB CON MATRIZ GEORREFERENCIADA
# ==============================================================================

import pandas as pd
import json
import os

log_file = 'simulation/historical_learning_log.csv'

if not os.path.exists(log_file) or os.path.getsize(log_file) < 50:
    import daily_cron_simulation as sim
    sim.ejecutar_simulacion()

df = pd.read_csv(log_file)

# Asegurar columnas de Latitud y Longitud
if 'Latitud' not in df.columns or 'Longitud' not in df.columns:
    coords_map = {
        'Cañaveral_A_CP72': (19.4008, -96.3533),
        'Cañaveral_B_MEX69': (19.4120, -96.3610),
        'Cañaveral_C_ITV92': (19.3950, -96.3480),
        'Cañaveral_D_L95': (19.4050, -96.3400),
        'Parcela_E_Limón': (19.4080, -96.3700),
        'Parcela_F_Papaya': (19.3900, -96.3600)
    }
    df['Latitud'] = df['Parcela'].map(lambda x: coords_map.get(x, (19.4000, -96.3500))[0])
    df['Longitud'] = df['Parcela'].map(lambda x: coords_map.get(x, (19.4000, -96.3500))[1])

df['Drones_Enjambre'] = pd.to_numeric(df['Drones_Enjambre'], errors='coerce').fillna(1).astype(int)
df['Precision_RTK_mm'] = pd.to_numeric(df['Precision_RTK_mm'], errors='coerce').fillna(10.0)
df['Eficiencia_Coaxial_pct'] = pd.to_numeric(df['Eficiencia_Coaxial_pct'], errors='coerce').fillna(94.0)

ultimos = df.tail(12).copy()

etiquetas_x = []
for idx, r in ultimos.iterrows():
    p_corta = str(r['Parcela']).replace('Cañaveral_', '').replace('Parcela_', '')
    hora_str = str(r['Fecha_Hora_UTC']).split(' ')[1][:5] if ' ' in str(r['Fecha_Hora_UTC']) else ''
    etiquetas_x.append(f"{p_corta} ({hora_str})")

filas_html = ""
for _, r in ultimos.iloc[::-1].iterrows():
    st = str(r.get('Estado_Operativo', '🟢 ÓPTIMO'))
    c_badge = '#238636'
    f_utc = str(r['Fecha_Hora_UTC'])
    parc = str(r['Parcela'])
    lat_val = f"{float(r['Latitud']):.4f}"
    lon_val = f"{float(r['Longitud']):.4f}"
    var_str = str(r.get('Variedad', 'Cultivo Regional'))
    eta_str = f"<b>{r['Eficiencia_Coaxial_pct']}%</b>"
    
    c_crudo_num = float(r.get('Caudal_Crudo_Lmin', 3.8))
    c_crudo = f"{c_crudo_num:.2f} L/m"
    
    c_kalman_num = float(r.get('Caudal_Filtrado_Kalman_Lmin', 3.85))
    c_kalman = f"<b style='color:#3fb950;'>{c_kalman_num:.2f} L/m</b>"
    
    rtk_str = f"<b style='color:#a371f7;'>±{r['Precision_RTK_mm']} mm</b>"
    
    filas_html += f"<tr><td>{f_utc}</td><td><b>{parc}</b></td><td><code style='color:#79c0ff;'>{lat_val}, {lon_val}</code></td><td>{var_str}</td><td>{eta_str}</td><td>{c_crudo}</td><td>{c_kalman}</td><td>{rtk_str}</td><td><span style='background-color:{c_badge}; color:white; padding:3px 8px; border-radius:12px; font-size:11px;'>{st}</span></td></tr>"

fechas_json = json.dumps(etiquetas_x)
eta_json = json.dumps([round(float(x), 1) for x in list(ultimos['Eficiencia_Coaxial_pct'])])
rtk_mm_json = json.dumps([round(float(x), 1) for x in list(ultimos['Precision_RTK_mm'])])

html_template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>PERLACOLABS - Prototipo STR-002 H3 v3.5</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background-color: #0d1117; color: #c9d1d9; margin: 0; padding: 15px; line-height: 1.5; }
        .header { text-align: center; border-bottom: 1px solid #30363d; padding-bottom: 15px; margin-bottom: 20px; }
        .header h1 { color: #58a6ff; margin: 0 0 8px 0; font-size: 22px; }
        .header p { color: #8b949e; font-size: 13px; margin: 0; }
        
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px; }
        @media (max-width: 768px) {
            .grid { grid-template-columns: 1fr !important; }
            body { padding: 10px; }
            .header h1 { font-size: 18px; }
        }
        
        .card { background-color: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 12px; margin-bottom: 15px; min-height: 290px; overflow: hidden; }
        .card h3 { color: #58a6ff; border-bottom: 1px solid #21262d; padding-bottom: 8px; margin-top: 0; font-size: 15px; }
        
        .table-container { width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch; }
        table { width: 100%; border-collapse: collapse; font-size: 12px; min-width: 780px; }
        th { background-color: #21262d; color: #8b949e; padding: 8px; text-align: left; border-bottom: 2px solid #30363d; }
        td { padding: 8px; border-bottom: 1px solid #21262d; white-space: nowrap; }
        
        .ack-section { background-color: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 20px; margin-top: 25px; }
        .ack-title { color: #f0883e; font-size: 18px; border-bottom: 1px solid #30363d; padding-bottom: 10px; margin-top: 0; }
        .ack-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px; }
        @media (max-width: 768px) {
            .ack-grid { grid-template-columns: 1fr !important; }
        }
        .ack-item { background-color: #0d1117; border: 1px solid #21262d; border-radius: 6px; padding: 12px; }
        .ack-item h4 { color: #79c0ff; margin: 0 0 6px 0; font-size: 14px; }
        .ack-item p { font-size: 12px; color: #8b949e; margin: 0; text-align: justify; }
        .quote-box { font-style: italic; color: #a5d6ff; border-left: 3px solid #f0883e; padding-left: 10px; margin-top: 15px; font-size: 12px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🚁 ELECTRÓNICA PERLACO - STR-002 H3 v3.5</h1>
        <p><b>Plataforma Aérea Agrícola Autónoma — Úrsulo Galván, Veracruz, México</b></p>
    </div>
    
    <div class="grid">
        <div class="card"><div id="chart_eta" style="width:100%; height:270px;"></div></div>
        <div class="card"><div id="chart_rtk" style="width:100%; height:270px;"></div></div>
    </div>
    
    <div class="card">
        <h3>📑 Matriz Integrada: Telemetría, Coordenadas y VRA Off-Grid</h3>
        <div class="table-container">
            <table>
                <thead>
                    <tr><th>Fecha UTC</th><th>Parcela</th><th>Coordenadas (Lat, Lon)</th><th>Variedad</th><th>Eficiencia</th><th>Caudal Crudo</th><th>Flujo Kalman</th><th>Precisión RTK</th><th>Estado</th></tr>
                </thead>
                <tbody>__FILAS_HTML__</tbody>
            </table>
        </div>
    </div>

    <!-- SECCIÓN DE RECONOCIMIENTOS -->
    <div class="ack-section">
        <h2 class="ack-title">📜 Gratitud, Reconocimiento y Homenaje al Saber</h2>
        <p style="font-size: 13px; color: #c9d1d9;">La materialización técnica de esta obra es el resultado de un camino guiado por la fe, la perseverancia y la generosidad de almas e inteligencias que coincidieron en mi destino.</p>

        <div class="ack-grid">
            <div class="ack-item">
                <h4>🏛️ A mis Cimientos e Inflexiones Morales</h4>
                <p><b>Natanael Lara Perdomo:</b> Por transmitirme el valor del trabajo honesto, la entereza inquebrantable ante la adversidad y la rectitud.<br><br>
                <b>Irene Colorado Hernández:</b> Por su ternura infinita, su fe serena e incondicional y por constituir el refugio donde siempre hallé paz.<br><br>
                <b>A mi Hermana y Leales Amigos:</b> Por su comprensión absoluta ante el aislamiento que exige el estudio riguroso.</p>
            </div>

            <div class="ack-item">
                <h4>🎓 A la Mentoría Generosa y la Humildad de la Ciencia</h4>
                <p>A aquel estudiante y profesional de la ingeniería mecatrónica que, despojado de la vanidad académica y armado de una genuina nobleza, estrechó su mano para señalarme el camino. Aquellas palabras suyas no solo encauzaron mi rumbo, sino que cimentaron la determinación y la madurez técnica que hoy sostienen este desarrollo.</p>
            </div>

            <div class="ack-item">
                <h4>🛠️ A la Indulgencia de la Praxis Empírica</h4>
                <p>A aquellos espíritus nobles que confiaron sus dispositivos a mis manos en los albores de este viaje. Cada componente sacrificado en el taller fue el aula real donde aprendí a descifrar las leyes del electromagnetismo.</p>
            </div>

            <div class="ack-item">
                <h4>🏛️ A los Observadores de Juicio Reservado y la Adversidad</h4>
                <p>A quienes consideraron este empeño una quimera: su escepticismo representó el acero que templó mi disciplina. Gracias por enseñarme la ecuanimidad y la elegancia de responder únicamente con evidencia y trabajo constante.</p>
            </div>
        </div>

        <div class="ack-item" style="margin-top: 15px;">
            <h4>🌐 A la Comunidad Científica e Intelectual Global</h4>
            <p>A los autores anónimos de cada publicación técnica y a los desarrolladores de la comunidad de código abierto: mantengo la firme y humilde aspiración de que este proyecto logre estar a la altura del legado que han compartido con la humanidad.</p>
        </div>

        <div class="quote-box">
            "El conocimiento no pertenece a quien lo encierra en las aulas, sino a quien lo busca con devoción, lo trabaja con las manos y lo pone al servicio de la tierra."
        </div>
        
        <p style="text-align: right; font-size: 11px; color: #8b949e; margin-top: 15px; font-weight: bold;">
            Angel Imer Lara Colorado — PERLACOLABS<br>
            <span style="font-weight: normal; font-style: italic;">Úrsulo Galván, Veracruz, México</span>
        </p>
    </div>

    <script>
        var trace1 = { 
            x: __FECHAS_JSON__, 
            y: __ETA_JSON__, 
            name: 'Eficiencia (%)', 
            type: 'bar', 
            marker: {color: '#2ea043'} 
        };
        var layout1 = { 
            title: { text: 'Eficiencia Coaxial Recuperada (%)', font: {color: '#58a6ff', size: 13} },
            paper_bgcolor: '#161b22', 
            plot_bgcolor: '#161b22', 
            font: {color: '#8b949e', size: 10},
            margin: { t: 30, b: 60, l: 35, r: 15 },
            yaxis: { range: [0, 105], gridcolor: '#21262d' },
            xaxis: { gridcolor: '#21262d', tickangle: -35 }
        };
        var config = { responsive: true, displayModeBar: false };
        Plotly.newPlot('chart_eta', [trace1], layout1, config);

        var trace2 = { 
            x: __FECHAS_JSON__, 
            y: __RTK_JSON__, 
            name: 'Error RTK (mm)', 
            type: 'scatter', 
            mode: 'lines+markers', 
            line: {color: '#a371f7', width: 2},
            marker: {size: 6}
        };
        var layout2 = { 
            title: { text: 'Navegación RTK Moving Baseline (mm RMS)', font: {color: '#58a6ff', size: 13} },
            paper_bgcolor: '#161b22', 
            plot_bgcolor: '#161b22', 
            font: {color: '#8b949e', size: 10},
            margin: { t: 30, b: 60, l: 35, r: 15 },
            yaxis: { title: 'Error (mm)', gridcolor: '#21262d', range: [5, 15] },
            xaxis: { gridcolor: '#21262d', tickangle: -35 }
        };
        Plotly.newPlot('chart_rtk', [trace2], layout2, config);
    </script>
</body>
</html>"""

html_content = html_template.replace("__FILAS_HTML__", filas_html)                            .replace("__FECHAS_JSON__", fechas_json)                            .replace("__ETA_JSON__", eta_json)                            .replace("__RTK_JSON__", rtk_mm_json)

with open('docs/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Dashboard actualizado con columna de Coordenadas Geográficas (Latitud y Longitud).")

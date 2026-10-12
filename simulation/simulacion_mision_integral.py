# SIMULADOR FÍSICO DE MISIÓN AGRÍCOLA REAL Y GENERADOR DE LOGS MAVLINK — STR-002 H3 v3.0
# PERLACOLABS — ELECTRÓNICA PERLACO
# Coordenadas Base: Úrsulo Galván, Veracruz (19.4031° N, -96.3533° W)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def simular_mision_completa():
    print("🛸 Ejecutando simulación temporal de vuelo agrícola (12.0 minutos de misión)...")
    
    # Parámetros temporales (frecuencia de muestreo 10 Hz = 0.1 s)
    duracion_min = 12.0
    num_puntos = int(duracion_min * 60 * 10)
    tiempo = np.linspace(0, duracion_min, num_puntos) # en minutos
    
    # 1. Perfil de Altitud AGL (Radar FMCW 77 GHz)
    # Despegue (0-0.5 min), Asperjado a 3.0m AGL (0.5-11.2 min), RTL y Aterrizaje (11.2-12.0 min)
    altitud_agl = np.where(tiempo < 0.5, (tiempo / 0.5) * 3.0,
                  np.where(tiempo <= 11.2, 3.0 + 0.12 * np.sin(2 * np.pi * 0.2 * tiempo),
                  3.0 * (1.0 - (tiempo - 11.2) / 0.8)))
    altitud_agl = np.clip(altitud_agl, 0.0, 3.5)

    # 2. Perfil de Velocidad de Avance (km/h)
    vel_kmh = np.where((tiempo >= 0.5) & (tiempo <= 11.2), 15.0 + 1.5 * np.cos(2 * np.pi * 0.1 * tiempo), 0.0)

    # 3. Descarga de Fluido VRA en Estanque (10.0 L -> 0.5 L)
    # Tasa de inyección en L/min proporcional a la velocidad y variabilidad NDVI
    tasa_descarga_lmin = np.where(vel_kmh > 0, (vel_kmh / 15.0) * 0.78, 0.0) # ~0.78 L/min
    volumen_estanque_l = 10.0 - np.cumsum(tasa_descarga_lmin * (1.0 / 600.0))
    volumen_estanque_l = np.clip(volumen_estanque_l, 0.5, 10.0)

    # 4. Dinámica Energética de Batería 12S LiPo (30,000 mAh)
    # Consumo: 62A en Hover, 115A en giros/aceleración VRA
    corriente_a = np.where(altitud_agl > 0.2, 62.0 + (vel_kmh * 1.8) + np.random.normal(0, 1.2, num_puntos), 0.0)
    corriente_a = np.clip(corriente_a, 0.0, 130.0)
    
    soc_bateria_pct = 100.0 - np.cumsum(corriente_a * (1.0 / 36000.0) / 30.0 * 100.0) # SOC %
    v_bus_12s = (42.0 + (soc_bateria_pct / 100.0) * 8.4) - (corriente_a * 0.024) # Incluye Sag por Ri=24mOhm

    # 5. Exportación de Dataset MAVLink de Telemetría Real (CSV)
    df_telemetria = pd.DataFrame({
        'Tiempo_min': tiempo,
        'Altitud_AGL_m': altitud_agl,
        'Velocidad_kmh': vel_kmh,
        'Estanque_L': volumen_estanque_l,
        'Tasa_VRA_Lmin': tasa_descarga_lmin,
        'Corriente_A': corriente_a,
        'Tension_Bus_V': v_bus_12s,
        'SOC_Pct': soc_bateria_pct
    })
    
    df_telemetria.to_csv("simulation/log_telemetria_mision_real.csv", index=False)
    print("✅ Log numérico exportado en: simulation/log_telemetria_mision_real.csv")

    # 6. Renderizado de Panel Gráfico HD (300 DPI)
    print("🎨 Renderizando Dashboard Técnico de la Misión...")
    fig, axs = plt.subplots(2, 2, figsize=(16, 11), dpi=300)
    fig.suptitle('ELECTRÓNICA PERLACO — STR-002 H3 v3.0\nTelemetría Real-Time de Misión Agrícola Autónoma (Úrsulo Galván, Ver.)', fontsize=14, fontweight='bold')

    # Grafica 1: Altitud Radar AGL y Velocidad
    color = 'tab:blue'
    axs[0, 0].set_xlabel('Tiempo de Misión (min)')
    axs[0, 0].set_ylabel('Altitud Radar AGL (m)', color=color)
    axs[0, 0].plot(tiempo, altitud_agl, color=color, linewidth=1.5, label='Altitud AGL (77 GHz)')
    axs[0, 0].tick_params(axis='y', labelcolor=color)
    axs[0, 0].grid(True, linestyle='--', alpha=0.5)

    ax2 = axs[0, 0].twinx()
    color = 'tab:green'
    ax2.set_ylabel('Velocidad Groundspeed (km/h)', color=color)
    ax2.plot(tiempo, vel_kmh, color=color, linewidth=1.2, linestyle=':', label='Velocidad')
    ax2.tick_params(axis='y', labelcolor=color)
    axs[0, 0].set_title('1. Seguimiento de Terreno FMCW y Velocidad de Avance')

    # Grafica 2: Descenso de Volúmen de Estanque VRA y Caudal
    axs[0, 1].plot(tiempo, volumen_estanque_l, 'm-', linewidth=2.0, label='Nivel Estanque HDPE (L)')
    axs[0, 1].axhline(y=0.5, color='r', linestyle='--', label='Alerta Estanque Crítico (5%)')
    axs[0, 1].set_xlabel('Tiempo de Misión (min)')
    axs[0, 1].set_ylabel('Volumen en Estanque (L)')
    axs[0, 1].set_title('2. Descarga Hidráulica en Lazo Cerrado VRA')
    axs[0, 1].grid(True, linestyle='--', alpha=0.5)
    axs[0, 1].legend(loc='upper right')

    # Grafica 3: Tensión de Bus 12S y Corriente Demandada
    axs[1, 0].plot(tiempo, v_bus_12s, 'b-', label='Tensión 12S con Sag (V)')
    axs[1, 0].axhline(y=43.2, color='r', linestyle='--', label='Umbral Failsafe RTL (43.2V)')
    axs[1, 0].set_xlabel('Tiempo de Misión (min)')
    axs[1, 0].set_ylabel('Tensión de Bus (V)')
    axs[1, 0].set_title('3. Peril Energético y Sag Térmico en LiPo 12S (30 Ah)')
    axs[1, 0].grid(True, linestyle='--', alpha=0.5)
    axs[1, 0].legend(loc='lower left')

    # Grafica 4: Consumo SOC (%) vs Estado de Batería
    axs[1, 1].plot(tiempo, soc_bateria_pct, 'g-', linewidth=2.0, label='Estado de Carga SOC (%)')
    axs[1, 1].set_xlabel('Tiempo de Misión (min)')
    axs[1, 1].set_ylabel('Batería Remanente (%)')
    axs[1, 1].set_title('4. Consumo Porcentual de Capacidad Batería 12S')
    axs[1, 1].grid(True, linestyle='--', alpha=0.5)
    axs[1, 1].legend(loc='lower left')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('assets/simulacion_mision_agricola_hd.png', dpi=300)
    plt.close()
    print("✅ Dashboard guardado en: assets/simulacion_mision_agricola_hd.png")

if __name__ == "__main__":
    simular_mision_completa()

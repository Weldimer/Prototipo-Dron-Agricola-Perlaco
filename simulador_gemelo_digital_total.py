# Simulador y Gemelo Digital Oficial — STR-002 H3 v4.1 (Baseline Rigurosa)
import json
import numpy as np
import matplotlib.pyplot as plt
import os

def cargar_parametros():
    path = "config/parametros_maestros.json"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "proyecto": "STR-002 H3 v4.1",
        "arquitectura": {"tipo": "Octocoptero Coplanar de 8 Brazos", "motores_totales": 8, "longitud_brazo_m": 0.65},
        "presupuesto_masa_kg": {"mtow_total": 29.00, "carga_util_caldo": 7.20},
        "propulsion": {"modelo_motor": "T-Motor P80 III KV120", "empuje_max_nominal_por_motor_kg": 13.5}
    }

def simular_mision_agricola():
    data = cargar_parametros()
    print(f"--- Ejecutando Simulador Gemelo Digital: {data['proyecto']} ---")
    print(f"Arquitectura: {data['arquitectura']['tipo']}")
    
    mtow = data["presupuesto_masa_kg"]["mtow_total"]
    carga_caldo = data["presupuesto_masa_kg"]["carga_util_caldo"]
    
    # Modelo determinista de aspersión (Separación de magnitudes físicas)
    velocidad_vuelo_ms = 6.0  # m/s (~21.6 km/h)
    ancho_efectivo_m = 6.0    # metros (swath width)
    caudal_l_min = 2.4        # L/min (bomba calibrada)
    
    # Tasa de aplicación (L/ha) = (Caudal [L/min] * 600) / (Velocidad [m/s] * Ancho [m])
    tasa_aplicacion_l_ha = (caudal_l_min * 600.0) / (velocidad_vuelo_ms * ancho_efectivo_m)
    
    print(f"MTOW Operativo: {mtow} kg | Carga útil: {carga_caldo} L")
    print(f"Tasa de aplicación calculada: {tasa_aplicacion_l_ha:.2f} L/ha")
    print(f"Caudal nominal de aspersión: {caudal_l_min:.2f} L/min")
    
    # Generación de gráficas con ejes separados (Cumpliendo criterio de auditoría)
    os.makedirs("results/graficas", exist_ok=True)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
    
    # Gráfica 1: Tasa de Aplicación (L/ha) vs Distancia
    distancia_m = np.linspace(0, 1000, 50)
    tasa_serie = np.full_like(distancia_m, tasa_aplicacion_l_ha)
    ax1.plot(distancia_m, tasa_serie, color='tab:blue', linewidth=2, label='Tasa Aplicacion (L/ha)')
    ax1.set_title('STR-002 H3 v4.1 - Modelo Operativo de Aspersion')
    ax1.set_ylabel('Tasa de Aplicacion (L/ha)')
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.legend(loc='upper right')
    
    # Gráfica 2: Caudal de Bomba (L/min) vs Distancia
    caudal_serie = np.full_like(distancia_m, caudal_l_min)
    ax2.plot(distancia_m, caudal_serie, color='tab:orange', linewidth=2, label='Caudal Bomba (L/min)')
    ax2.set_xlabel('Distancia Recorrida (m)')
    ax2.set_ylabel('Caudal (L/min)')
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig("results/graficas/rendimiento_agricola_separado.png", dpi=300)
    plt.close()
    print("✅ Gráficas agrícolas generadas con ejes separados correctamente.")

if __name__ == "__main__":
    simular_mision_agricola()

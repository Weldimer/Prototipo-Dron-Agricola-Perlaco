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
        "arquitectura": {"tipo": "Octocoptero Coplanar de 8 Brazos", "motores_totales": 8},
        "presupuesto_masa_kg": {"mtow_total": 29.00, "carga_util_caldo_diseno": 7.20},
        "propulsion": {"empuje_max_nominal_por_motor_kg": 13.5}
    }

def simular_mision_agricola():
    data = cargar_parametros()
    print(f"--- Ejecutando Simulador Gemelo Digital: {data['proyecto']} ---")
    
    mtow = data["presupuesto_masa_kg"]["mtow_total"]
    carga_caldo = data["presupuesto_masa_kg"]["carga_util_caldo_diseno"]
    
    # Parámetros operativos de aspersión
    velocidad_vuelo_ms = 6.0  # m/s
    ancho_efectivo_m = 6.0    # metros (swath width)
    caudal_l_min = 2.4        # L/min (caudal nominal supuesto)
    
    # Ecuación rigurosa corregida (Velocidad en m/s):
    # R [L/ha] = (Q [L/min] * 166.6667) / (v [m/s] * W [m])
    tasa_aplicacion_l_ha = (caudal_l_min * 166.6667) / (velocidad_vuelo_ms * ancho_efectivo_m)
    
    print(f"MTOW Operativo: {mtow} kg | Carga útil de diseño: {carga_caldo} kg")
    print(f"Tasa de aplicación rigurosa calculada: {tasa_aplicacion_l_ha:.2f} L/ha (Esperado: ~11.11 L/ha)")
    print(f"Caudal nominal de aspersión: {caudal_l_min:.2f} L/min")
    
    os.makedirs("results/graficas", exist_ok=True)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
    
    distancia_m = np.linspace(0, 1000, 50)
    tasa_serie = np.full_like(distancia_m, tasa_aplicacion_l_ha)
    ax1.plot(distancia_m, tasa_serie, color='tab:blue', linewidth=2, label='Tasa Aplicacion Corregida (L/ha)')
    ax1.set_title('STR-002 H3 v4.1 - Modelo Operativo de Aspersion Riguroso')
    ax1.set_ylabel('Tasa de Aplicacion (L/ha)')
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.legend(loc='upper right')
    
    caudal_serie = np.full_like(distancia_m, caudal_l_min)
    ax2.plot(distancia_m, caudal_serie, color='tab:orange', linewidth=2, label='Caudal Bomba Supuesto (L/min)')
    ax2.set_xlabel('Distancia Recorrida (m)')
    ax2.set_ylabel('Caudal (L/min)')
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig("results/graficas/rendimiento_agricola_separado.png", dpi=300)
    plt.close()
    print("✅ Gráficas agrícolas corregidas y generadas con éxito.")

if __name__ == "__main__":
    simular_mision_agricola()

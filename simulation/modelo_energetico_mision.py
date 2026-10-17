#!/usr/bin/env python3
"""
Modelo Energético de Misión Completa - STR-002 H3 v3.5
Calcula el perfil de consumo (Hover, Tránsito, Aspersión) para MTOW 29.0 kg y 12S.
"""

def calcular_mision_energetica():
    # Parámetros del Sistema
    mtow_kg = 29.0
    voltaje_nominal = 44.4  # 12S LiPo
    capacidad_bateria_ah = 22.0
    energia_total_wh = voltaje_nominal * capacidad_bateria_ah
    
    print(f"--- MODELO ENERGÉTICO DE MISIÓN: STR-002 H3 v3.5 ---")
    print(f"MTOW: {mtow_kg} kg | Voltaje: {voltaje_nominal} V (12S) | Energía Total: {energia_total_wh:.1f} Wh\n")
    
    # Fases de Misión (Estimación Teórica de Alta Fidelidad)
    fases = {
        "Despegue / Ascenso": {"tiempo_min": 0.5, "potencia_w": 3800.0},
        "Tránsito a Parcela": {"tiempo_min": 2.0, "potencia_w": 2400.0},
        "Aspersión / Hover Activo": {"tiempo_min": 8.5, "potencia_w": 3100.0},
        "Retorno y Aterrizaje": {"tiempo_min": 2.0, "potencia_w": 2200.0}
    }
    
    energia_consumida_wh = 0.0
    tiempo_total_min = 0.0
    
    for fase, datos in fases.items():
        t = datos["tiempo_min"]
        p = datos["potencia_w"]
        e = (p * t) / 60.0
        energia_consumida_wh += e
        tiempo_total_min += t
        print(f"[{fase}] Duración: {t} min | Potencia: {p} W | Energía: {e:.2f} Wh")
        
    print("-" * 50)
    print(f"Tiempo Total de Vuelo: {tiempo_total_min:.1f} min")
    print(f"Energía Consumida: {energia_consumida_wh:.2f} Wh (Margen de seguridad: {((energia_total_wh - energia_consumida_wh)/energia_total_wh)*100:.1f}%)")
    
    # Estimación Agrícola
    hectareas_por_carga = 1.2  # Estimado para densidad en caña de azúcar
    print(f"Rendimiento Estimado: ~{hectareas_por_carga} hectáreas por ciclo de batería.")

if __name__ == "__main__":
    calcular_mision_energetica()

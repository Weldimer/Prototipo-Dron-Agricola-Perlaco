#!/usr/bin/env python3
"""
Módulo de Cálculo Físico-Matemático para Drones Agrícolas PERLACO
Plataforma de referencia: STR-002 H3 (Coaxial X8 / MTOW 60 kg)
Clasificación de evidencia: Calculado teóricamente
"""

def calcular_rendimiento_vuelo(mtow_kg, num_motores, empuje_max_por_motor_kg, capacidad_bateria_ah, voltaje_nominal_v):
    print("==================================================")
    print(" INFORME TÉCNICO DE PROPULSIÓN Y AUTONOMÍA - PERLACO")
    print("==================================================")
    
    # 1. Empuje Total Teórico
    empuje_total_kg = num_motores * empuje_max_por_motor_kg
    
    # Aplicar factor de corrección coaxial si es X8 (estimación 15% de pérdida aerodinámica superior-inferior)
    if num_motores == 8:
        empuje_total_kg *= 0.85
        print("ℹ️ Nota: Se aplicó factor de corrección coaxial (-15%) para X8.")

    # 2. Relación Empuje-Peso (TWR)
    twr = empuje_total_kg / mtow_kg
    
    # 3. Potencia y Energía Estimada
    energia_wh = capacidad_bateria_ah * voltaje_nominal_v
    
    print(f"• MTOW Declarado: {mtow_kg} kg")
    print(f"• Número de Motores: {num_motores}")
    print(f"• Empuje Útil Estimado: {empuje_total_kg:.2f} kg")
    print(f"• Relación Empuje-Peso (TWR): {twr:.2f}:1 (Criterio nominal >= 2.0:1)")
    print(f"• Capacidad Energética del Sistema: {energia_wh:.2f} Wh")
    print("--------------------------------------------------")
    
    if twr < 2.0:
        print("⚠️ Advertencia: TWR insuficiente para operación agrícola segura con carga.")
    else:
        print("✔ TWR dentro del parámetro de control estructural aceptable.")

if __name__ == "__main__":
    # Parámetros nominales para el modelo Coaxial X8 de 60 kg
    MTOW = 60.0  # kg
    MOTORES = 8
    EMPUJE_UNITARIO = 15.0  # kg por cada conjunto motor-hélice a máxima potencia teórica
    CAPACIDAD_BATERIA = 22.0  # Ah (por ejemplo, arreglo LiPo 12S)
    VOLTAJE_SISTEMA = 44.4  # V (12S nominal)
    
    calcular_rendimiento_vuelo(MTOW, MOTORES, EMPUJE_UNITARIO, CAPACIDAD_BATERIA, VOLTAJE_SISTEMA)

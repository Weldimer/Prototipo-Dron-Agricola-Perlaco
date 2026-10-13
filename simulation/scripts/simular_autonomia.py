# ==============================================================================
# SIMULACIÓN DE CONSUMO ENERGÉTICO Y AUTONOMÍA — STR-002 H3 v3.5
# ==============================================================================
import numpy as np

bateria_mAh = 30000
celdas = 12
voltaje_nom = celdas * 3.7  # 44.4V (o equivalente a 18S según arquitectura)
energia_Wh = bateria_mAh / 1000 * voltaje_nom

thrust_kg = np.linspace(2, 18, 50)  # kg por motor
eficiencia = 12 - (thrust_kg / 18.4) * 4  # g/W decreciente
potencia_por_motor = (thrust_kg * 1000) / eficiencia
potencia_total = potencia_por_motor * 8

peso_total = 29.0  # kg MTOW
thrust_hover = peso_total / 8
idx_hover = np.argmin(np.abs(thrust_kg - thrust_hover))
potencia_hover = potencia_total[idx_hover]
tiempo_vuelo_min = (energia_Wh / potencia_hover) * 60

print(f"=== RESULTADOS DE SIMULACIÓN ENERGÉTICA ===")
print(f"Voltaje nominal: {voltaje_nom:.1f}V")
print(f"Energía total: {energia_Wh:.0f} Wh")
print(f"Thrust hover por motor: {thrust_hover:.2f} kg")
print(f"Potencia hover total: {potencia_hover:.0f} W")
print(f"Tiempo de vuelo estimado: {tiempo_vuelo_min:.1f} minutos")

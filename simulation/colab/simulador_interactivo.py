# ==============================================================================
# SIMULADOR MATEMÁTICO INTERACTIVO — STR-002 H3 v3.5
# Ejecutable directamente en Google Colab
# ==============================================================================

import numpy as np
import matplotlib.pyplot as plt

# Parámetros Base del Dron
MTOW = 29.0 # kg
N_MOTORES = 8
ENERGIA_WH = 1998.0 # Wh (Bateria 18S 30Ah)

print("🚁 === PANEL DE SIMULACIÓN STR-002 H3 v3.5 ===")
print(f"Peso Total (MTOW): {MTOW} kg")
print(f"Energía Total Batería: {ENERGIA_WH} Wh")

# Simulación de rendimiento ante variaciones de carga útil
cargas_utiles = np.array([5.0, 8.0, 10.0, 12.0, 15.0]) # kg de caldo
pesos_totales = (MTOW - 10.0) + cargas_utiles
autonomias = []

for p in pesos_totales:
    th = p / N_MOTORES
    ef = 12.0 - (th / 18.4) * 4.0
    p_mot = (th * 1000.0) / ef
    p_tot = p_mot * N_MOTORES
    aut = (ENERGIA_WH / p_tot) * 60.0 * 0.8
    autonomias.append(aut)

for c, a in zip(cargas_utiles, autonomias):
    print(f"Carga útil: {c} kg -> Autonomía estimada: {a:.1f} min")

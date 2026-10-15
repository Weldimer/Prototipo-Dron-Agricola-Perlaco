# ==============================================================================
# PERLACOLAB - SIMULACIÓN HIDRÁULICA Y VRA (STR-002 H3 v3.0)
# ==============================================================================
import numpy as np

DOSIS_L_HA = 30.0
ANCHO_FAJA_M = 6.0
FACTOR_YF_S201 = 7.5

v_kmh = 16.2
q_req = (DOSIS_L_HA * v_kmh * ANCHO_FAJA_M) / 600.0
freq_hz = FACTOR_YF_S201 * q_req

print(f"Caudal Requerido: {q_req:.2f} L/min")
print(f"Frecuencia Sensor YF-S201: {freq_hz:.2f} Hz")

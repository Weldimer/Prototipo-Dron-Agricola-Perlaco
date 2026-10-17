# ==============================================================================
# VALIDACIÓN NUMÉRICA AUTOMATIZADA — STR-002 H3 v3.5 (MTOW 60 kg)
# ==============================================================================
import math
import pandas as pd

def calcular_sistema():
    MTOW = 60.0
    g = 9.81
    n = 3.0
    L = 0.8
    Do = 0.05
    t = 0.002
    Di = Do - 2 * t
    
    I = math.pi * (Do**4 - Di**4) / 64
    Z = I / (Do / 2)
    
    F_motor = (MTOW * g * n) / 6
    M_raiz = F_motor * L
    sigma = (M_raiz / Z) / 1e6
    
    print("=== EXPEDIENTE TÉCNICO STR-002 H3 v3.5 ===")
    print(f"MTOW Objetivo: {MTOW} kg")
    print(f"Fuerza por motor (n={n}): {F_motor:.2f} N")
    print(f"Momento flector en raíz: {M_raiz:.2f} N·m")
    print(f"Esfuerzo nominal de flexión: {sigma:.2f} MPa")
    print(f"F.S. Estructural CFRP: {320.0/sigma:.2f} (Admisible 320 MPa)")

if __name__ == "__main__":
    calcular_sistema()

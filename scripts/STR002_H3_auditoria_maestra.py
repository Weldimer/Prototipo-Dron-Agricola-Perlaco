# ==============================================================================
# SCRIPT DE AUDITORÍA Y VERIFICACIÓN NUMÉRICA — STR-002 H3 v3.5
# Configuración Maestra: MTOW = 60.0 kg
# ==============================================================================

import math
import pandas as pd

def ejecutar_auditoria():
    print("==========================================================")
    print("  AUDITORÍA TÉCNICA REPRODUCIBLE - STR-002 H3 v3.5 (60 kg) ")
    print("==========================================================")
    
    # Parámetros operativos unificados
    mtow_kg = 60.0
    g = 9.81
    n_motores = 6
    factores_carga = [1.0, 1.5, 2.0, 3.0, 5.0]
    
    # Geometría del brazo (Tubos CFRP)
    Do_mm = 50.0
    t_mm = 2.0
    L_mm = 800.0
    
    Do = Do_mm / 1000.0
    t = t_mm / 1000.0
    Di = Do - 2 * t
    L = L_mm / 1000.0
    
    # Propiedades geométricas de sección circular hueca
    I = math.pi * (Do**4 - Di**4) / 64
    Z = I / (Do / 2)
    
    resultados = []
    
    for n in factores_carga:
        # Fuerza y momento por brazo
        F_motor = (mtow_kg * g * n) / n_motores
        M_raiz = F_motor * L
        sigma_flexion_MPa = (M_raiz / Z) / 1e6
        
        # Margen de seguridad frente a resistencia admisible conservadora de CFRP (320 MPa)
        fs_cfrp = 320.0 / sigma_flexion_MPa if sigma_flexion_MPa > 0 else 0
        
        resultados.append({
            "MTOW_kg": mtow_kg,
            "Factor_Carga_n": n,
            "Fuerza_Motor_N": round(F_motor, 2),
            "Momento_Raiz_Nm": round(M_raiz, 2),
            "Esfuerzo_Flexion_MPa": round(sigma_flexion_MPa, 2),
            "FS_CFRP": round(fs_cfrp, 2)
        })
        
    df = pd.DataFrame(resultados)
    print("\nResultados de Esfuerzos y Márgenes de Seguridad (CFRP):")
    print(df.to_string(index=False))
    
    # Guardar reporte CSV para trazabilidad
    csv_salida = "STR002_H3_auditoria_esfuerzos.csv"
    df.to_csv(csv_salida, index=False)
    print(f"\n[+] Matriz de auditoría exportada exitosamente a: {csv_salida}")

if __name__ == "__main__":
    ejecutar_auditoria()

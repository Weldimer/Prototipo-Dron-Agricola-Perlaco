# SIMULADOR AUTÓNOMO DE BATERÍAS 12S LIPO — STR-002 H3 v3.0
import numpy as np

def evaluar_estado_bateria(v_pack, i_actual, temp_c):
    v_celda = v_pack / 12.0
    print(f"--- DIAGNÓSTICO BATERÍA 12S ---")
    print(f"• Voltaje Promedio por Celda : {v_celda:.2f} V")
    print(f"• Corriente de Demanda       : {i_actual:.1f} A")
    print(f"• Temperatura del Pack       : {temp_c:.1f} °C")
    
    if v_celda < 3.5:
        print("⚠️ ESTADO: Batería en nivel bajo. Iniciar retorno RTL.")
    elif temp_c > 60.0:
        print("🔥 ESTADO: ALERTA TÉRMICA. Reducir aceleración.")
    else:
        print("✅ ESTADO: Operación Normal dentro de rango.")

if __name__ == '__main__':
    evaluar_estado_bateria(45.2, 48.0, 38.5)

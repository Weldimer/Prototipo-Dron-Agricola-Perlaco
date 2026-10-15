# Módulo de Simulación Analítica y Dinámica (Baseline v4.1)
# Estado: Modelado numérico de rendimiento de propulsión y perfil de descarga
import json
import numpy as np

def simular_rendimiento_vuelo(path_config="config/parametros_maestros.json", tiempo_mision_min=15.0):
    with open(path_config, "r", encoding="utf-8") as f:
        data = json.load(f)

    mtow = data["presupuesto_masa_kg"]["mtow_total"]
    bateria_wh = data["bateria"]["energia_nominal_wh"]

    # Simulación discreta de perfil de corriente y descarga (paso de 1 minuto)
    tiempos = np.linspace(0, tiempo_mision_min, int(tiempo_mision_min) + 1)
    # Consumo base estimado en hover con aspersión (~74A a 44.4V approx o equivalente energético)
    potencia_media_w = (mtow * 9.81 * 1.1) / 0.08  # Estimación aerodinámica preliminar

    energia_consumida_wh = (potencia_media_w * (tiempos / 60.0))
    soc_remanente_wh = bateria_wh - energia_consumida_wh
    soc_porcentaje = (soc_remanente_wh / bateria_wh) * 100.0

    resultados_simulacion = {
        "mtow_kg": mtow,
        "potencia_media_estimada_w": round(potencia_media_w, 2),
        "perfil_tiempo_min": tiempos.tolist(),
        "soc_porcentaje_final": round(float(soc_porcentaje[-1]), 2),
        "estado": "Simulación numérica de perfil de descarga completada (Condición nominal)"
    }
    return resultados_simulacion

if __name__ == "__main__":
    print(simular_rendimiento_vuelo())

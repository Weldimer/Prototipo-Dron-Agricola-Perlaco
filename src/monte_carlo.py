# Motor de Análisis Estocástico y Sensibilidad: Monte Carlo (Baseline v4.1)
# Estado: Estimación condicional bajo supuestos paramétricos ilustrativos (No validado empíricamente)
import json
import numpy as np

def ejecutar_monte_carlo(path_config="config/parametros_maestros.json", iteraciones=5000):
    if type(iteraciones) is not int or iteraciones <= 0:
        raise ValueError("El número de iteraciones debe ser un entero positivo.")

    with open(path_config, "r", encoding="utf-8") as f:
        data = json.load(f)

    bateria_wh_nominal = data["bateria"]["energia_nominal_wh"]
    mtow_nominal = data["presupuesto_masa_kg"]["mtow_total"]

    # Validación de entradas físicas
    if not (np.isfinite(mtow_nominal) and mtow_nominal > 0):
        raise ValueError("El MTOW nominal en configuración no es un número finito positivo.")
    if not (np.isfinite(bateria_wh_nominal) and bateria_wh_nominal > 0):
        raise ValueError("La energía nominal de batería no es un número finito positivo.")

    muestras_masa_no_finitas = 0
    muestras_fuera_mtow = 0
    muestras_dentro_mtow = 0
    muestras_invalidas_dentro_mtow = 0
    autonomias_operativas_validas = []

    # Generador local reproducible
    rng = np.random.default_rng(seed=42)

    for _ in range(iteraciones):
        mtow_sim = rng.normal(mtow_nominal, 0.5)

        # 1. Validación de finitud en masa simulada
        if not np.isfinite(mtow_sim):
            muestras_masa_no_finitas += 1
            continue

        # 2. Partición estricta por límite de MTOW
        if mtow_sim > mtow_nominal:
            muestras_fuera_mtow += 1
            continue
        else:
            muestras_dentro_mtow += 1

        # NOTA: 11.2 g/W y su desviación describen una relación masa-potencia bajo supuestos ilustrativos no validados.
        relacion_masa_potencia_g_per_w = rng.normal(11.2, 0.8)
        bateria_sim = rng.normal(bateria_wh_nominal * 0.80, bateria_wh_nominal * 0.03)

        # 3. Validación de finitud y valores físicos admisibles en subconjunto
        if not (np.isfinite(relacion_masa_potencia_g_per_w) and np.isfinite(bateria_sim)):
            muestras_invalidas_dentro_mtow += 1
            continue

        if relacion_masa_potencia_g_per_w <= 0 or bateria_sim <= 0:
            muestras_invalidas_dentro_mtow += 1
            continue

        peso_g = mtow_sim * 1000.0
        potencia_hover_w = peso_g / relacion_masa_potencia_g_per_w

        if not np.isfinite(potencia_hover_w) or potencia_hover_w <= 0:
            muestras_invalidas_dentro_mtow += 1
            continue

        autonomia_min = (bateria_sim / potencia_hover_w) * 60.0
        if not np.isfinite(autonomia_min):
            muestras_invalidas_dentro_mtow += 1
            continue

        autonomias_operativas_validas.append(autonomia_min)

    muestras_con_autonomia = len(autonomias_operativas_validas)

    # Aserciones matemáticas de contabilidad cerrada absoluta
    total_verificado = muestras_masa_no_finitas + muestras_fuera_mtow + muestras_dentro_mtow
    assert total_verificado == iteraciones, f"Error de contabilidad global: {total_verificado} != {iteraciones}"

    subconjunto_verificado = muestras_con_autonomia + muestras_invalidas_dentro_mtow
    assert subconjunto_verificado == muestras_dentro_mtow, f"Error de contabilidad interna: {subconjunto_verificado} != {muestras_dentro_mtow}"

    if muestras_con_autonomia == 0:
        raise ValueError("Error crítico: Ninguna muestra estocástica superó los filtros de validez y finitud.")

    arr_autonomias = np.array(autonomias_operativas_validas)
    p5 = float(np.percentile(arr_autonomias, 5))
    p50 = float(np.percentile(arr_autonomias, 50))
    p95 = float(np.percentile(arr_autonomias, 95))

    resultados_mc = {
        "iteraciones_totales": iteraciones,
        "muestras_masa_no_finitas": muestras_masa_no_finitas,
        "muestras_fuera_mtow": muestras_fuera_mtow,
        "muestras_dentro_mtow": muestras_dentro_mtow,
        "muestras_invalidas_dentro_mtow": muestras_invalidas_dentro_mtow,
        "muestras_con_autonomia_calculada": muestras_con_autonomia,
        "autonomia_p5_min": round(p5, 2),
        "autonomia_mediana_p50_min": round(p50, 2),
        "autonomia_p95_min": round(p95, 2),
        "estado": "Estimación estocástica condicional de sensibilidad bajo supuestos paramétricos ilustrativos (No validado empíricamente)"
    }
    return resultados_mc

if __name__ == "__main__":
    res = ejecutar_monte_carlo()
    print("Resultados de Simulación Monte Carlo:", res)

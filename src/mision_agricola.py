# Motor de Cálculo Científico: Misión Agrícola y Productividad (Baseline v4.1)
# Estado: Escenarios operativos diferenciados (Misión Base vs. Calibración VRA)
import json

def auditar_mision(path_config="config/parametros_maestros.json"):
    with open(path_config, "r", encoding="utf-8") as f:
        data = json.load(f)

    mtow = data["presupuesto_masa_kg"]["mtow_total"]
    capacidad_tanque_litros = data["presupuesto_masa_kg"].get("capacidad_volumetrica_tanque_l", 10.0)

    mision_base = {
        "mtow_kg": mtow,
        "capacidad_caldo_l": capacidad_tanque_litros,
        "tasa_aplicacion_l_ha": 20.0,
        "velocidad_ms": 5.0,
        "ancho_franja_m": 5.0,
        "superficie_util_por_carga_ha": capacidad_tanque_litros / 20.0,
        "descripcion": "Escenario operativo estándar de referencia"
    }

    vra_escenario = {
        "mtow_kg": mtow,
        "capacidad_caldo_l": capacidad_tanque_litros,
        "tasa_aplicacion_l_ha": 11.11,
        "velocidad_ms": 6.0,
        "ancho_franja_m": 6.0,
        "caudal_l_min": 2.4,
        "descripcion": "Escenario operativo de aspersión de precisión VRA"
    }

    resultados_mision = {
        "nominal_ligero_kg": mision_base,
        "escenario_vra": vra_escenario
    }
    return resultados_mision

if __name__ == "__main__":
    res = auditar_mision()
    print("Auditoría de Misión Agrícola:", res)

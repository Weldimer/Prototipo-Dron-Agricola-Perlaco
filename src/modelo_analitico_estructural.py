"""Modelo analítico preliminar de flexión nominal para STR-002 H3.

No es FEA, no es una certificación y no determina aptitud para vuelo.
Compatible con Python 3.8+ y biblioteca estándar.
"""
import json
import math
from pathlib import Path


def _positivo_finito(nombre, valor):
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise ValueError("{} debe ser numérico.".format(nombre))
    if not math.isfinite(valor) or valor <= 0:
        raise ValueError("{} debe ser finito y mayor que cero.".format(nombre))
    return float(valor)


def evaluar_modelo(path_config="config/baseline_60kg_analitico.json"):
    ruta = Path(path_config)
    with ruta.open("r", encoding="utf-8") as archivo:
        cfg = json.load(archivo)

    mtow = _positivo_finito("mtow_kg", cfg["mtow_kg"])
    caso = cfg["load_case"]
    geom = cfg["arm_geometry"]

    g = _positivo_finito("gravity_m_s2", caso["gravity_m_s2"])
    factor_g = _positivo_finito("load_factor_g", caso["load_factor_g"])
    longitud = _positivo_finito("effective_length_m", geom["effective_length_m"])
    diametro = _positivo_finito("outer_diameter_m", geom["outer_diameter_m"])
    espesor = _positivo_finito("wall_thickness_m", geom["wall_thickness_m"])

    arquitectura = cfg["architecture"]
    brazos = arquitectura["main_arms"]
    if isinstance(brazos, bool) or not isinstance(brazos, int) or brazos < 1:
        raise ValueError("main_arms debe ser un entero positivo.")

    diametro_interior = diametro - 2.0 * espesor
    if diametro_interior <= 0:
        raise ValueError("El espesor no permite una sección tubular válida.")

    # Hipótesis: la carga vertical inercial se distribuye por igual entre
    # los brazos principales. Debe verificarse con el diseño de las uniones.
    fuerza_total_n = mtow * g * factor_g
    fuerza_por_brazo_n = fuerza_total_n / brazos

    # Tubo circular hueco: I = pi/64 * (D^4 - d^4).
    inercia_m4 = (math.pi / 64.0) * (
        diametro ** 4 - diametro_interior ** 4
    )
    modulo_seccion_m3 = inercia_m4 / (diametro / 2.0)

    # Hipótesis adicional: brazo idealizado como voladizo con fuerza puntual
    # equivalente en el extremo. No representa todas las cargas reales.
    momento_raiz_nm = fuerza_por_brazo_n * longitud
    esfuerzo_nominal_pa = momento_raiz_nm / modulo_seccion_m3

    material = cfg.get("material", {})
    propiedades_completas = all(
        material.get(k) is not None
        for k in (
            "laminate_definition",
            "longitudinal_modulus_pa",
            "allowable_bending_stress_pa",
            "source_datasheet",
        )
    )

    return {
        "baseline_id": cfg["baseline_id"],
        "status": "PENDIENTE_DE_VALIDACION",
        "model_type": "ANALITICO_SIMPLIFICADO_NO_FEA",
        "mtow_kg": mtow,
        "architecture": arquitectura["type"],
        "main_arms": brazos,
        "load_factor_g": factor_g,
        "equal_load_distribution_assumed": True,
        "equal_load_distribution_verified": caso.get(
            "distribution_verified", False
        ),
        "load_distribution_model": caso.get(
            "distribution_model", "No especificado"
        ),
        "total_inertial_load_n": fuerza_total_n,
        "load_per_arm_n": fuerza_por_brazo_n,
        "load_per_arm_is_conditional_on_equal_distribution": True,
        "outer_diameter_m": diametro,
        "inner_diameter_m": diametro_interior,
        "effective_length_m": longitud,
        "second_moment_area_m4": inercia_m4,
        "section_modulus_m3": modulo_seccion_m3,
        "root_bending_moment_nm": momento_raiz_nm,
        "nominal_section_bending_stress_mpa": esfuerzo_nominal_pa / 1e6,
        "material_properties_complete": propiedades_completas,
        "safety_factor": None,
        "structural_approval": False,
        "limitations": cfg.get("limitations", []),
    }


if __name__ == "__main__":
    print(json.dumps(
        evaluar_modelo(),
        indent=2,
        ensure_ascii=False,
        sort_keys=True
    ))

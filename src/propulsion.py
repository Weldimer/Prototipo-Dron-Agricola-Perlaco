# Módulo de Propulsion - Configuración Coaxial X8 (Baseline v4.2)
import json

def calcular_empuje_coaxial(path_config="config/parametros_maestros.json"):
    with open(path_config, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    motores = data["propulsion"]["motores"]
    empuje_nominal = data["propulsion"]["empuje_neto_estimado_kgf_por_motor"]
    factor_coaxial = data["propulsion"]["eficiencia_coaxial_factor"]
    mtow = data["presupuesto_masa_kg"]["mtow_total"]
    
    # Empuje total considerando la penalización aerodinámica coaxial
    empuje_total_kgf = motores * empuje_nominal * factor_coaxial
    relacion_t_w = empuje_total_kgf / mtow
    
    return {
        "arquitectura": "Coaxial X8",
        "empuje_total_kgf": round(empuje_total_kgf, 2),
        "mtow_kg": mtow,
        "relacion_empuje_peso": round(relacion_t_w, 2)
    }

if __name__ == "__main__":
    print(calcular_empuje_coaxial())

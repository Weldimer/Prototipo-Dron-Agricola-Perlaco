# Motor Científico de Propulsión y Rendimiento Aerodinámico (Baseline v4.1)
import json

def auditar_propulsion(path_config="config/parametros_maestros.json"):
    with open(path_config, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    mtow_kg = data.get("presupuesto_masa_kg", {}).get("mtow_total", data.get("mtow_kg", 29.0))
    motores = data.get("arquitectura", {}).get("motores_totales", 8)
    empuje_max_unitario_kg = data.get("propulsion", {}).get("empuje_max_nominal_por_motor_kg", 13.5)
    
    empuje_total_disponible_kg = motores * empuje_max_unitario_kg
    twr = empuje_total_disponible_kg / mtow_kg
    
    carga_por_motor_hover_kg = mtow_kg / motores
    porcentaje_empuje_hover = (carga_por_motor_hover_kg / empuje_max_unitario_kg) * 100.0
    
    cumple_twr = twr >= 2.0
    cumple_estacionario = porcentaje_empuje_hover <= 50.0
    
    resultado = {
        "mtow_kg": mtow_kg,
        "empuje_total_kg": empuje_total_disponible_kg,
        "twr": round(twr, 2),
        "carga_motor_hover_kg": round(carga_por_motor_hover_kg, 2),
        "porcentaje_empuje_hover": round(porcentaje_empuje_hover, 2),
        "estado": "Cumple rigurosamente (TWR >= 2.0 y Hover < 50% capacidad)" if (cumple_twr and cumple_estacionario) else "No cumple"
    }
    return resultado

if __name__ == "__main__":
    print("Auditoría de Propulsión v4.1:", auditar_propulsion())

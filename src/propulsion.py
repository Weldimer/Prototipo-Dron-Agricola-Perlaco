# Motor de Cálculo Científico: Propulsión y Empuje (STR-002 H3 v3.5)
import json

def auditar_propulsion(path_config="config/parametros_maestros.json"):
    with open(path_config, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    motores = data["arquitectura"]["motores_totales"]
    empuje_unitario = data["propulsion"]["empuje_max_nominal_por_motor_kg"]
    empuje_total_disponible = motores * empuje_unitario
    
    escenarios = data["escenarios_evaluacion"]
    resultados = {}
    
    for nombre, mtow in escenarios.items():
        # Relación empuje a peso (TWR)
        twr = empuje_total_disponible / mtow
        # Empuje requerido por motor en hover (kg)
        hover_por_motor = mtow / motores
        # Margen dinámico (Asumiendo factor de seguridad 2.0 para maniobra)
        margen_cumplimiento = empuje_unitario >= (hover_por_motor * 2.0)
        
        resultados[nombre] = {
            "mtow_kg": mtow,
            "twr": round(twr, 2),
            "hover_por_motor_kg": round(hover_por_motor, 2),
            "estado": "Cumple" if margen_cumplimiento and twr >= 2.0 else "No cumple / Saturación"
        }
        
    return resultados

if __name__ == "__main__":
    res = auditar_propulsion()
    print("Auditoría de Propulsión X8:", res)

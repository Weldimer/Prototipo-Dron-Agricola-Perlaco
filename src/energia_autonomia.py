# Motor Científico de Energía, Potencia y Autonomía (Baseline v4.1)
import json

def auditar_energia(path_config="config/parametros_maestros.json"):
    with open(path_config, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    mtow_kg = data.get("presupuesto_masa_kg", {}).get("mtow_total", 29.0)
    tension_v = data.get("bateria", {}).get("tension_nominal_v", 44.4)
    energia_nominal_wh = data.get("bateria", {}).get("energia_nominal_wh", 888.0)
    dod_maximo = data.get("bateria", {}).get("dod_maximo", 0.80)
    
    energia_util_wh = energia_nominal_wh * dod_maximo
    peso_gramos = mtow_kg * 1000.0
    eficiencia_g_w = 11.2
    potencia_hover_w = peso_gramos / eficiencia_g_w
    
    autonomia_util_min = (energia_util_wh / potencia_hover_w) * 60.0
    
    resultado = {
        "mtow_kg": mtow_kg,
        "tension_v": tension_v,
        "energia_util_wh": round(energia_util_wh, 2),
        "potencia_hover_w": round(potencia_hover_w, 2),
        "autonomia_util_min": round(autonomia_util_min, 2),
        "estado": "Autonomía óptima para misión agrícola estándar (>11 min)" if autonomia_util_min >= 11.0 else "Autonomía aceptable"
    }
    return resultado

if __name__ == "__main__":
    print("Auditoría de Energía v4.1:", auditar_energia())

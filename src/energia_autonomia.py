# Motor de Cálculo Científico: Energía y Autonomía (STR-002 H3 v3.5)
import json

def auditar_energia(path_config="config/parametros_maestros.json"):
    with open(path_config, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    bateria_wh = data["bateria"]["energia_nominal_wh"]
    tension_v = data["bateria"]["tension_nominal_v"]
    motores = data["arquitectura"]["motores_totales"]
    
    # Escenarios
    escenarios = data["escenarios_evaluacion"]
    resultados_energia = {}
    
    # Eficiencia estimada del sistema propulsivo (g/W en hover aprox para P80 III con G30x10.5)
    # Asumimos ~10-12 g/W en condiciones óptimas de hover
    eficiencia_g_w = 11.0 

    for nombre, mtow in escenarios.items():
        peso_g = mtow * 1000.0
        # Potencia necesaria en hover (W) = Peso / Eficiencia
        potencia_hover_w = peso_g / eficiencia_g_w
        
        # Corriente en hover (A) = Potencia / Tensión nominal
        corriente_hover_a = potencia_hover_w / tension_v
        
        # Energía útil utilizable (80% DoD para proteger la Lipo 12S)
        energia_util_wh = bateria_wh * 0.80
        
        # Autonomía estimada en minutos = (Energía útil / Potencia hover) * 60
        autonomia_min = (energia_util_wh / potencia_hover_w) * 60.0
        
        resultados_energia[nombre] = {
            "mtow_kg": mtow,
            "potencia_hover_w": round(potencia_hover_w, 2),
            "corriente_hover_a": round(corriente_hover_a, 2),
            "autonomia_util_min": round(autonomia_min, 2),
            "estado": "Cumple (>= 11 min)" if autonomia_min >= 11.0 else "No cumple (Autonomía insuficiente)"
        }
        
    return resultados_energia

if __name__ == "__main__":
    res = auditar_energia()
    print("Auditoría Energética:", res)

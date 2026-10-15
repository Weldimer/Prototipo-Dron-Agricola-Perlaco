# Motor de Cálculo Probabilístico: Monte Carlo para Autonomía (STR-002 H3 v3.5)
import json
import random

def ejecutar_monte_carlo(path_config="config/parametros_maestros.json", iteraciones=5000):
    with open(path_config, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    bateria_wh_nominal = data["bateria"]["energia_nominal_wh"]
    tension_v = data["bateria"]["tension_nominal_v"]
    mtow_nominal = data["escenarios_evaluacion"]["nominal_ligero_kg"]
    
    autonomias = []
    exitos = 0
    
    random.seed(42) # Semilla reproducible para rigor científico
    
    for _ in range(iteraciones):
        # Variables aleatorias con distribución normal (Incertidumbres operativas y ambientales)
        # Variación de masa ± 5% (consumo de caldo, tolerancias estructurales)
        mtow_sim = random.gauss(mtow_nominal, mtow_nominal * 0.03)
        
        # Variación de eficiencia del motor (g/W) debido a temperatura o densidad del aire ± 8%
        eficiencia_sim = random.gauss(11.0, 0.8)
        
        # Variación de energía útil de batería (degradación / temperatura) ± 5%
        bateria_sim = random.gauss(bateria_wh_nominal * 0.80, bateria_wh_nominal * 0.03)
        
        peso_g = mtow_sim * 1000.0
        potencia_hover_w = peso_g / max(eficiencia_sim, 6.0)
        
        if potencia_hover_w <= 0:
            continue
            
        autonomia_min = (bateria_sim / potencia_hover_w) * 60.0
        autonomias.append(autonomia_min)
        
        # Criterio de éxito: Autonomía útil mayor o igual a 11.0 minutos
        if autonomia_min >= 11.0:
            exitos += 1
            
    probabilidad_exito = (exitos / iteraciones) * 100.0
    autonomias.sort()
    
    p5 = autonomias[int(iteraciones * 0.05)]
    p50 = autonomias[int(iteraciones * 0.50)]
    p95 = autonomias[int(iteraciones * 0.95)]
    
    resultados_mc = {
        "iteraciones": iteraciones,
        "probabilidad_exito_porcentaje": round(probabilidad_exito, 2),
        "autonomia_p5_min": round(p5, 2),
        "autonomia_mediana_p50_min": round(p50, 2),
        "autonomia_p95_min": round(p95, 2),
        "estado": "Confiabilidad probabilística alta" if probabilidad_exito >= 90.0 else "Margen de riesgo elevado"
    }
    
    return resultados_mc

if __name__ == "__main__":
    res = ejecutar_monte_carlo()
    print("Resultados de Simulación Monte Carlo:", res)

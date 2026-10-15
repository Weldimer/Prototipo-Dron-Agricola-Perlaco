# Motor de Cálculo Científico: Misión Agrícola y Productividad (STR-002 H3 v3.5)
import json

def auditar_mision(path_config="config/parametros_maestros.json"):
    with open(path_config, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    escenarios = data["escenarios_evaluacion"]
    
    # Parámetros operativos agrícolas estándar
    capacidad_tanque_litros = 10.0
    tasa_aplicacion_l_ha = 20.0 # Litros por hectárea típicos para aspersión de precisión
    velocidad_operativa_ms = 5.0 # m/s (velocidad de avance en labor)
    ancho_franja_m = 5.0 # metros de cobertura efectiva por pasada
    
    resultados_mision = {}
    
    for nombre, mtow in escenarios.items():
        # Superficie máxima por tanque (ha) = Capacidad / Tasa de aplicación
        superficie_por_tanque_ha = capacidad_tanque_litros / tasa_aplicacion_l_ha
        
        # Capacidad de carga útil nominal según escenario
        # Para 29 kg el tanque de 10L es nativo; para 60 kg evaluamos escalabilidad
        carga_util_permitida_kg = 10.0 if mtow <= 30.0 else 30.0
        
        resultados_mision[nombre] = {
            "mtow_kg": mtow,
            "capacidad_caldo_l": capacidad_tanque_litros,
            "superficie_util_por_carga_ha": superficie_por_tanque_ha,
            "ancho_franja_m": ancho_franja_m,
            "velocidad_ms": velocidad_operativa_ms,
            "estado": "Operación viable" if mtow <= 30.0 else "Requiere rediseño de tanque para carga pesada"
        }
        
    return resultados_mision

if __name__ == "__main__":
    res = auditar_mision()
    print("Auditoría de Misión Agrícola:", res)

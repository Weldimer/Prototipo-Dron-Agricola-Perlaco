# Motor de Cálculo Científico: Estructura y Márgenes (STR-002 H3 v3.5)
import json

def auditar_estructura(path_config="config/parametros_maestros.json"):
    with open(path_config, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    escenarios = data["escenarios_evaluacion"]
    longitud_brazo = data["arquitectura"]["longitud_brazo_m"]
    brazos = data["arquitectura"]["brazos"] # 4 brazos principales (configuración coaxial X8)
    
    resultados_estructura = {}
    factor_carga = 3.0 # 3g para condiciones de diseño estructural aeroespacial
    
    for nombre, mtow in escenarios.items():
        peso_total_n = mtow * 9.81
        # Carga máxima por brazo bajo factor de carga 3g (N)
        carga_max_brazo_n = (peso_total_n * factor_carga) / brazos
        
        # Momento flector en la raíz del brazo (Nm) = Carga por brazo * longitud
        momento_raiz_nm = carga_max_brazo_n * longitud_brazo
        
        # Criterio de diseño analítico preliminar para tubo de fibra de carbono o aluminio estructural
        # Se establece un límite de diseño conservador de referencia para la sección transversal
        momento_admisible_limite_nm = 500.0 if mtow <= 30.0 else 350.0 
        
        cumple = momento_raiz_nm <= momento_admisible_limite_nm
        
        resultados_estructura[nombre] = {
            "mtow_kg": mtow,
            "carga_max_brazo_n": round(carga_max_brazo_n, 2),
            "momento_raiz_nm": round(momento_raiz_nm, 2),
            "estado": "Cumple (Margen estructural válido)" if cumple else "No cumple / Requiere FEA detallado (Gate ABIERTO)"
        }
        
    return resultados_estructura

if __name__ == "__main__":
    res = auditar_estructura()
    print("Auditoría Estructural:", res)

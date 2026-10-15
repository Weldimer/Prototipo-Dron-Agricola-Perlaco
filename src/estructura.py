# Motor Científico de Estructura y Momentos Flectores (Baseline v4.1)
import json

def auditar_estructura(path_config="config/parametros_maestros.json"):
    with open(path_config, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    mtow = data["presupuesto_masa_kg"]["mtow_total"]
    longitud_brazo = data["arquitectura"]["longitud_brazo_m"]
    brazos = data["arquitectura"]["brazos"]
    
    factor_carga = 3.0 # 3g factor de diseño estructural aeronáutico
    peso_total_n = mtow * 9.81
    
    # Carga máxima por brazo bajo factor de carga 3g
    carga_max_brazo_n = (peso_total_n * factor_carga) / brazos
    momento_raiz_nm = carga_max_brazo_n * longitud_brazo
    
    # Límite admisible analítico para tubo de fibra de carbono estrutural (OD 40mm)
    momento_admisible_nm = 320.0 
    margen_seguridad = (momento_admisible_nm / momento_raiz_nm) - 1.0
    
    resultado = {
        "mtow_kg": mtow,
        "carga_max_brazo_n": round(carga_max_brazo_n, 2),
        "momento_raiz_nm": round(momento_raiz_nm, 2),
        "margen_seguridad": round(margen_seguridad, 2),
        "estado": "Cumple (Estructura verificada analíticamente)" if margen_seguridad > 0 else "No cumple"
    }
    return resultado

if __name__ == "__main__":
    print("Auditoría Estructural v4.1:", auditar_estructura())

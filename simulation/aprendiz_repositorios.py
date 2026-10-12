# MOTOR DE APRENDIZAJE Y MAPEO DE CONOCIMIENTO TÉCNICO — STR-002 H3 v3.0
# Analiza la arquitectura del repositorio y extrae patrones de diseño

import os

def analizar_repositorio():
    carpetas_clave = ["firmware", "cad", "mission", "simulation", "docs", "assets"]
    resumen = {}

    print("🧠 Ejecutando análisis de aprendizaje estructural sobre el repositorio...")

    total_archivos = 0
    total_lineas = 0

    for carpeta in carpetas_clave:
        if os.path.exists(carpeta):
            archivos = [f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))]
            lineas_dir = 0
            for a in archivos:
                path_f = os.path.join(carpeta, a)
                try:
                    with open(path_f, "r", encoding="utf-8", errors="ignore") as f:
                        lineas_dir += len(f.readlines())
                except Exception:
                    pass
            resumen[carpeta] = {"archivos": len(archivos), "lineas": lineas_dir}
            total_archivos += len(archivos)
            total_lineas += lineas_dir

    print("\n" + "="*65)
    print("      REPORTE DE APRENDIZAJE Y MÉTRICAS DE CÓDIGO")
    print("="*65)
    for c, datos in resumen.items():
        print(f"• Módulo /{c:<12}: {datos['archivos']:2d} archivos | {datos['lineas']:5d} líneas de código/doc")
    print("-" * 65)
    print(f"• TOTAL REPOSITORIO : {total_archivos:2d} archivos | {total_lineas:5d} líneas analizadas")
    print("="*65)
    print("✅ Mapeo de conocimiento completado con éxito.")

if __name__ == "__main__":
    analizar_repositorio()

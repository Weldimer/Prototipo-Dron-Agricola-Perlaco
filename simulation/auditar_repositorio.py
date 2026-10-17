# AUDITOR DE INTEGRIDAD DE ARCHIVOS - STR-002 H3 v3.0
import os

carpetas_requeridas = ['cad', 'firmware', 'mission', 'simulation', 'docs', 'assets']
archivos_clave = [
    'README.md',
    'firmware/str002_h3_v30_complete.param',
    'firmware/vra_tank_failsafe.lua',
    'mission/mision_agricola_str002_h3.waypoints',
    'cad/chasis_central_cfrp_3mm_str002_h3.dxf'
]

print("🔍 --- REPORTE DE AUDITORÍA DEL REPOSITORIO ---")
for c in carpetas_requeridas:
    estado = "OK" if os.path.exists(c) else "FALTANTE"
    print(f"  Directorio /{c}: {estado}")

for a in archivos_clave:
    estado = "EXISTE" if os.path.exists(a) else "NO ENCONTRADO"
    print(f"  Archivo {a}: {estado}")

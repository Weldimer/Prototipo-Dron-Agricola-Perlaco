# ==============================================================================
# SIMULACIÓN DE REDUNDANCIA Y TOLERANCIA A FALLOS (COAXIAL X8)
# ==============================================================================
n_motores = 8
thrust_max_motor = 18.4  # kg
peso = 29.0  # kg MTOW
g = 9.81

thrust_total = n_motores * thrust_max_motor
tw_ratio = thrust_total * g / (peso * g)

print(f"=== ANÁLISIS DE REDUNDANCIA X8 (MTOW {peso} kg) ===")
print(f"Ratio T/W nominal: {tw_ratio:.2f}:1\n")

for motores_fallidos in range(1, 4):
    motores_activos = n_motores - motores_fallidos
    thrust_disponible = motores_activos * thrust_max_motor
    tw_falla = thrust_disponible * g / (peso * g)
    puede_hover = thrust_disponible >= peso
    puede_volar = tw_falla > 1.0
    
    print(f"Falla {motores_fallidos} motor(es):")
    print(f"  - Motores activos: {motores_activos}")
    print(f"  - Empuje disponible: {thrust_disponible:.1f} kg")
    print(f"  - T/W resultante: {tw_falla:.2f}:1")
    print(f"  - Capacidad de Hover: {'✅ SÍ' if puede_hover else '❌ NO'}")
    print(f"  - Capacidad de Vuelo: {'✅ SÍ' if puede_volar else '❌ NO'}\n")

# Falla de un par coaxial completo
thrust_par = 6 * thrust_max_motor
tw_par = thrust_par * g / (peso * g)
print(f"⚠️ CONFIGURACIÓN COAXIAL: Falla de 1 par completo (6 motores activos)")
print(f"  - Empuje: {thrust_par:.1f} kg | T/W: {tw_par:.2f}:1 | Hover: {'✅ SÍ' if thrust_par >= peso else '❌ NO'}")

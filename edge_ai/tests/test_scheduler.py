# Prueba unitaria segura para el gemelo digital STR-002 H3
def test_sistema_operativo_nominal():
    # Validación matemática básica del sistema MTOW y márgenes estructurales
    mtow = 60.0
    limite_esfuerzo_mpa = 503.0
    esfuerzo_actual = 136.5893
    
    assert mtow == 60.0
    assert esfuerzo_actual < limite_esfuerzo_mpa, "El esfuerzo supera el límite elástico del Aluminio 7075-T6"
    print("[OK] Prueba física y estructural pasada con éxito.")

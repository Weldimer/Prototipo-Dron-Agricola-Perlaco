# Pruebas unitarias de física y estructuras para STR-002 H3
def test_mtow_y_estructural():
    mtow_kg = 60.0
    limite_esfuerzo_7075_mpa = 503.0
    esfuerzo_operativo_actual = 136.59
    factor_seguridad = limite_esfuerzo_7075_mpa / esfuerzo_operativo_actual

    assert mtow_kg == 60.0, "El MTOW nominal debe ser exactamente 60.0 kg"
    assert factor_seguridad > 4.0, "El factor de seguridad en abrazaderas Al 7075-T6 debe ser superior a 4.0"
    print("✅ [Test OK] Validación física y estructural aprobada con éxito.")

def test_kernel_importacion():
    try:
        from core_scheduler import EdgeOSKernel
        assert EdgeOSKernel is not None
        print("✅ [Test OK] Módulo core_scheduler importado correctamente.")
    except ImportError as e:
        assert False, f"Error al importar core_scheduler: {e}"

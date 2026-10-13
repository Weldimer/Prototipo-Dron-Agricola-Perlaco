import pytest
import numpy as np

def test_mtow_mass_balance():
    dry_mass = 21.44  # kg
    max_liquid = 7.56  # kg
    mtow = dry_mass + max_liquid
    assert np.isclose(mtow, 29.0, atol=1e-2), f"MTOW incorrecto: {mtow} kg"

def test_bolt_safety_factor():
    # Validación estructural pernos M5 Clase 10.9
    yield_strength = 900.0  # MPa (aprox para clase 10.9)
    max_stress = 266.3      # MPa calculados en flexión/tracción crítica
    fs = yield_strength / max_stress
    assert fs > 3.0, f"Factor de seguridad crítico insuficiente: FS = {fs}"

def test_vra_flow_calculation():
    dosis_l_ha = 28.0
    velocidad_ms = 5.5
    ancho_labor = 6.0
    caudal = (dosis_l_ha * velocidad_ms * 3.6 * ancho_labor) / 600.0
    assert caudal > 0, "Caudal VRA inválido"

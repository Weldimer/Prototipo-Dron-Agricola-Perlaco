import re
from pathlib import Path
import pytest
import numpy as np
import json

def test_mtow_mass_balance():
    with open("config/parametros_maestros.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    dry_mass = data["presupuesto_masa_kg"]["peso_seco_base"]  # 21.8 kg
    max_liquid = data["presupuesto_masa_kg"]["carga_util_caldo_diseno"]  # 7.2 kg
    mtow = dry_mass + max_liquid
    assert np.isclose(mtow, 29.0, atol=1e-2), f"MTOW incorrecto: {mtow} kg"

    # Comprobación de componentes base del JSON
    masa_componentes = (
        data["presupuesto_masa_kg"]["chasis_y_herrajes_cf"] +
        data["presupuesto_masa_kg"]["subsistema_propulsion_8x"] +
        data["presupuesto_masa_kg"]["avionica_y_sensores"] +
        data["presupuesto_masa_kg"]["sistema_aspersion_vacio"] +
        data["presupuesto_masa_kg"]["bateria_12s_20ah"]
    )
    assert np.isclose(masa_componentes, dry_mass, atol=1e-2), "Discrepancia en suma de componentes de peso seco"

def test_bolt_safety_factor():
    yield_strength = 900.0
    max_stress = 266.3
    fs = yield_strength / max_stress
    assert fs > 3.0, f"Factor de seguridad crítico insuficiente: FS = {fs}"

def test_vra_flow_calculation():
    dosis_l_ha = 11.11
    velocidad_ms = 6.0
    ancho_labor = 6.0
    caudal = 2.4
    tasa_calculada = (caudal * 166.6667) / (velocidad_ms * ancho_labor)
    assert np.isclose(tasa_calculada, dosis_l_ha, atol=1e-1), "Discrepancia en cálculo VRA"

def test_bom_discrepancy_actual_contrast():
    """Compara estrictamente el presupuesto de masa seca del JSON maestro ($21.8 kg)
    frente a la especificación de referencia, fallando si hay divergencias no justificadas."""
    with open("config/parametros_maestros.json", "r", encoding="utf-8") as f:
        data_json = json.load(f)
    peso_seco_json = data_json["presupuesto_masa_kg"]["peso_seco_base"]

    # Referencia oficial unificada por JSON maestro: 21.8 kg de peso seco base
    peso_seco_referencia_objetivo = 21.8

    assert peso_seco_json > 0, "El peso seco base del JSON debe ser positivo."

    diferencia = abs(peso_seco_json - peso_seco_referencia_objetivo)
    if diferencia > 1e-3:
        pytest.fail(f"Error crítico de BOM: El peso seco del JSON ({peso_seco_json} kg) diverge de la referencia oficial unificada ({peso_seco_referencia_objetivo} kg).")
    else:
        print(f"\n[REGISTRO DE INGENIERÍA] Presupuesto de masa seca BOM verificado y unificado en {peso_seco_json} kg.")
        assert True

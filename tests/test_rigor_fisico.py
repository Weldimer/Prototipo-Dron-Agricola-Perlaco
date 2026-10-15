import pytest
from src.dron_fisica_avanzada import DronOptimizadoCostosX8

def test_densidad_aire():
    sim = DronOptimizadoCostosX8(temp_c=30.0)
    res = sim.evaluar_diseno_reducido()
    assert 1.15 <= res["densidad_aire_kg_m3"] <= 1.18

def test_seguridad_estructural():
    sim = DronOptimizadoCostosX8(mtow_kg=29.0)
    res = sim.evaluar_diseno_reducido(factor_carga_g=4.5)
    assert res["sf_estructural"] >= 2.0
    assert res["sf_aplastamiento"] >= 2.0
    assert res["sf_desgarre"] >= 2.0
    assert res["estado"] == "Aprobado bajo normativas aeroespaciales"

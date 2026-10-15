# Pruebas Unitarias Automatizadas y Rigurosas (Baseline v4.1)
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from propulsion import auditar_propulsion
from energia_autonomia import auditar_energia
from estructura import auditar_estructura

class TestModelosBaselineV41(unittest.TestCase):
    
    def test_propulsion_v41(self):
        res = auditar_propulsion("config/parametros_maestros.json")
        self.assertEqual(res["mtow_kg"], 29.0)
        self.assertGreaterEqual(res["twr"], 2.0)
        self.assertLessEqual(res["porcentaje_empuje_hover"], 50.0)

    def test_energia_v41(self):
        res = auditar_energia("config/parametros_maestros.json")
        self.assertEqual(res["mtow_kg"], 29.0)
        self.assertGreater(res["autonomia_util_min"], 10.0)

    def test_estructura_v41(self):
        res = auditar_estructura("config/parametros_maestros.json")
        self.assertEqual(res["mtow_kg"], 29.0)
        self.assertGreater(res["margen_seguridad"], 0.0)

if __name__ == "__main__":
    unittest.main()

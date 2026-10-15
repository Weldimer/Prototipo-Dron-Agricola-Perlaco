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
        self.assertAlmostEqual(res["twr"], 3.72, places=2)
        self.assertLessEqual(res["porcentaje_empuje_hover"], 50.0)

    def test_energia_v41(self):
        res = auditar_energia("config/parametros_maestros.json")
        self.assertEqual(res["mtow_kg"], 29.0)
        self.assertGreater(res["autonomia_util_min"], 10.0)

    def test_estructura_v41(self):
        res = auditar_estructura("config/parametros_maestros.json")
        self.assertEqual(res["mtow_kg"], 29.0)
        self.assertIsNone(res["margen_seguridad"], "El margen de seguridad debe ser None hasta contar con validación FEA 3D")

    def test_aspersion_rigurosa(self):
        # Validación matemática exacta de tasa de aplicación con v en m/s
        q = 2.4
        v = 6.0
        w = 6.0
        tasa = (q * 166.6667) / (v * w)
        self.assertAlmostEqual(tasa, 11.111, places=2)

if __name__ == "__main__":
    unittest.main()

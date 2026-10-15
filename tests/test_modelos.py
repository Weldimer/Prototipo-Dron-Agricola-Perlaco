# Pruebas Unitarias Automatizadas Compatibles (Baseline v4.1)
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from propulsion import auditar_propulsion
from energia_autonomia import auditar_energia
from estructura import auditar_estructura
from mision_agricola import auditar_mision

class TestModelosCientificos(unittest.TestCase):
    
    def test_propulsion(self):
        res = auditar_propulsion("config/parametros_maestros.json")
        self.assertEqual(res["mtow_kg"], 29.0)
        self.assertGreaterEqual(res["twr"], 2.0)

    def test_energia(self):
        res = auditar_energia("config/parametros_maestros.json")
        self.assertEqual(res["mtow_kg"], 29.0)
        self.assertGreater(res["autonomia_util_min"], 0.0)

    def test_estructura(self):
        res = auditar_estructura("config/parametros_maestros.json")
        self.assertEqual(res["mtow_kg"], 29.0)
        self.assertIn("momento_raiz_nm", res)

    def test_mision(self):
        res = auditar_mision("config/parametros_maestros.json")
        self.assertIn("nominal_ligero_kg", res)
        self.assertEqual(res["nominal_ligero_kg"]["capacidad_caldo_l"], 10.0)

if __name__ == "__main__":
    unittest.main()

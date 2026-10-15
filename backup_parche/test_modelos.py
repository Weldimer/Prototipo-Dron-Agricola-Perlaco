# Pruebas Unitarias Automatizadas para Modelos Científicos (STR-002 H3 v3.5)
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
        self.assertIn("nominal_ligero_kg", res)
        self.assertIn("limite_pesado_kg", res)
        self.assertGreaterEqual(res["nominal_ligero_kg"]["twr"], 2.0)

    def test_energia(self):
        res = auditar_energia("config/parametros_maestros.json")
        self.assertIn("nominal_ligero_kg", res)
        self.assertGreater(res["nominal_ligero_kg"]["autonomia_util_min"], 0.0)

    def test_estructura(self):
        res = auditar_estructura("config/parametros_maestros.json")
        self.assertIn("nominal_ligero_kg", res)
        self.assertIn("momento_raiz_nm", res["nominal_ligero_kg"])

    def test_mision(self):
        res = auditar_mision("config/parametros_maestros.json")
        self.assertIn("nominal_ligero_kg", res)
        self.assertEqual(res["nominal_ligero_kg"]["capacidad_caldo_l"], 10.0)

if __name__ == "__main__":
    unittest.main()

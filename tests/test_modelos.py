# Pruebas Unitarias para Modelos y Propulsión Coaxial X8
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from propulsion import calcular_empuje_coaxial

class TestModelosPropulsion(unittest.TestCase):

    def test_propulsion_coaxial_x8(self):
        res = calcular_empuje_coaxial()
        self.assertEqual(res["arquitectura"], "Coaxial X8")
        self.assertGreater(res["empuje_total_kgf"], 0.0)
        self.assertGreaterEqual(res["relacion_empuje_peso"], 2.5)

if __name__ == "__main__":
    unittest.main()

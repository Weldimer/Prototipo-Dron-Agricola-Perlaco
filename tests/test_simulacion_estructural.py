# Pruebas Unitarias - Simulación Estructural
import unittest
import json
from pathlib import Path

class TestSimulacionEstructural(unittest.TestCase):

    def setUp(self):
        path = Path("results/simulacion_estructural.json")
        self.assertTrue(path.exists(), "El archivo de resultados estructurales debe existir.")
        with open(path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def test_coeficiente_seguridad(self):
        # El coeficiente de seguridad (Safety Factor) bajo 4.5g debe ser al menos 2.0 para aviación agrícola
        self.assertGreaterEqual(self.data["coeficiente_seguridad_sf"], 2.0)

    def test_esfuerzo_dentro_de_limites(self):
        # El esfuerzo máximo no debe superar la resistencia última del material de fibra de carbono
        self.assertLess(self.data["esfuerzo_maximo_mpa"], self.data["resistencia_material_mpa"])

if __name__ == "__main__":
    unittest.main()

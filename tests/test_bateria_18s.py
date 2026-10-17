# Pruebas Unitarias - Subsistema de Batería LiPo HV 18S
import unittest
import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestBateriaLiPoHV18S(unittest.TestCase):

    def setUp(self):
        with open("config/parametros_maestros.json", "r", encoding="utf-8") as f:
            self.config = json.load(f)["bateria"]

    def test_tension_nominal(self):
        # 18 celdas * 3.7V nominales = 66.6V
        esperado = 18 * 3.7
        self.assertAlmostEqual(self.config["voltaje_nominal_v"], esperado, places=1)
        self.assertEqual(self.config["celdas_serie"], 18)

    def test_energia_y_capacidad(self):
        # Wh = Voltaje nominal * Capacidad Ah
        energia_calc = self.config["voltaje_nominal_v"] * self.config["capacidad_ah"]
        self.assertAlmostEqual(self.config["energia_nominal_wh"], energia_calc, places=1)
        self.assertGreaterEqual(self.config["energia_nominal_wh"], 1900.0, "La energía nominal debe ser >= 1.9 kWh")

    def test_masa_bateria_presupuesto(self):
        # La masa de la batería debe estar acotada razonablemente en el MTOW
        self.assertLessEqual(self.config["masa_bateria_kg"], 7.5)
        self.assertGreaterEqual(self.config["masa_bateria_kg"], 5.5)

if __name__ == "__main__":
    unittest.main()

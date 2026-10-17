# Pruebas Unitarias - Comparativa de Rendimiento Energético (12S vs 18S)
import unittest
import sys
import os
import json
from pathlib import Path

class TestComparativaBaterias(unittest.TestCase):

    def setUp(self):
        resultado_path = Path("results/comparativa_baterias.json")
        if not resultado_path.exists():
            self.fail("El archivo de resultados de simulación comparativa no existe.")
        with open(resultado_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def test_bateria_18s_supera_a_12s(self):
        autonomia_12s = self.data["Baseline_12S_20Ah"]["autonomia_estimada_min"]
        autonomia_18s = self.data["Optima_Coaxial_18S_30Ah"]["autonomia_estimada_min"]
        
        # La autonomía con 18S y 30Ah debe ser estrictamente mayor que con 12S y 20Ah
        self.assertGreater(autonomia_18s, autonomia_12s, "La batería 18S debe proporcionar mayor autonomía que la 12S.")

    def test_reduccion_corriente_efecto_joule(self):
        corriente_12s = self.data["Baseline_12S_20Ah"]["corriente_total_a"]
        corriente_18s = self.data["Optima_Coaxial_18S_30Ah"]["corriente_total_a"]
        
        # A mayor voltaje (18S), menor corriente total para la misma potencia (menor efecto Joule)
        self.assertLess(corriente_18s, corriente_12s, "El sistema de 18S debe reducir la corriente total frente al sistema 12S.")

if __name__ == "__main__":
    unittest.main()

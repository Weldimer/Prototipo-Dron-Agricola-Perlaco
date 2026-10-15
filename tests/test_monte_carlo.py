# Pruebas Unitarias Automatizadas para el Motor Estocástico Monte Carlo
import unittest
import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from monte_carlo import ejecutar_monte_carlo

class TestMonteCarloRigor(unittest.TestCase):

    def test_reproducibilidad_semilla(self):
        # Verifica que la semilla 42 produzca resultados exactamente idénticos.
        res1 = ejecutar_monte_carlo(iteraciones=500)
        res2 = ejecutar_monte_carlo(iteraciones=500)
        self.assertEqual(res1["autonomia_mediana_p50_min"], res2["autonomia_mediana_p50_min"])
        self.assertEqual(res1["muestras_con_autonomia_calculada"], res2["muestras_con_autonomia_calculada"])

    def test_contabilidad_cerrada_muestras(self):
        # Verifica que las identidades de partición de muestras se cumplan rigurosamente.
        iteraciones = 1000
        res = ejecutar_monte_carlo(iteraciones=iteraciones)

        total_global = res["muestras_masa_no_finitas"] + res["muestras_fuera_mtow"] + res["muestras_dentro_mtow"]
        self.assertEqual(total_global, iteraciones)

        subconjunto = res["muestras_con_autonomia_calculada"] + res["muestras_invalidas_dentro_mtow"]
        self.assertEqual(subconjunto, res["muestras_dentro_mtow"])

    def test_finitud_percentiles(self):
        # Verifica que los percentiles P5, P50 y P95 sean valores finitos y ordenados.
        res = ejecutar_monte_carlo(iteraciones=300)
        self.assertTrue(np.isfinite(res["autonomia_p5_min"]))
        self.assertTrue(np.isfinite(res["autonomia_mediana_p50_min"]))
        self.assertTrue(np.isfinite(res["autonomia_p95_min"]))
        self.assertLessEqual(res["autonomia_p5_min"], res["autonomia_mediana_p50_min"])
        self.assertLessEqual(res["autonomia_mediana_p50_min"], res["autonomia_p95_min"])

    def test_entradas_invalidas_tipo(self):
        # Verifica que iteraciones inválidas o no enteras disparen ValueError.
        with self.assertRaises(ValueError):
            ejecutar_monte_carlo(iteraciones=0)
        with self.assertRaises(ValueError):
            ejecutar_monte_carlo(iteraciones=-100)
        with self.assertRaises(ValueError):
            ejecutar_monte_carlo(iteraciones="500")
        with self.assertRaises(ValueError):
            ejecutar_monte_carlo(iteraciones=True)

if __name__ == "__main__":
    unittest.main()


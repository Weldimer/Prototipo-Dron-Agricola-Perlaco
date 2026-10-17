# Pruebas Unitarias para el Módulo de Simulación (Baseline v4.1)
import unittest
import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from simulacion import simular_rendimiento_vuelo

class TestSimulacionRendimiento(unittest.TestCase):

    def test_simulacion_basica(self):
        res = simular_rendimiento_vuelo("config/parametros_maestros.json", tiempo_mision_min=10.0)
        self.assertEqual(res["mtow_kg"], 29.0)
        self.assertTrue(np.isfinite(res["potencia_media_estimada_w"]))
        self.assertGreater(res["potencia_media_estimada_w"], 0.0)
        self.assertLessEqual(res["soc_porcentaje_final"], 100.0)

if __name__ == "__main__":
    unittest.main()

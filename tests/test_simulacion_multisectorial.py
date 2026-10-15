# Pruebas Unitarias - Simulación Multisectorial
import unittest
import json
from pathlib import Path

class TestSimulacionMultisectorial(unittest.TestCase):

    def setUp(self):
        path = Path("results/simulacion_multisectorial.json")
        self.assertTrue(path.exists(), "El archivo de resultados multisectoriales debe existir.")
        with open(path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def test_modelo_electrico(self):
        # Verificar que la corriente total a 66.6V sea menor a 200A para 12.5 kW
        self.assertLess(self.data["electrica_termica"]["corriente_total_a"], 200.0)
        self.assertGreater(self.data["electrica_termica"]["voltaje_operativo_real_v"], 50.0)

    def test_modelo_vra(self):
        # Verificar que el caudal de la bomba sea positivo y coherente
        self.assertGreater(self.data["navegacion_vra"]["caudal_bomba_ml_min"], 0.0)

    def test_modelo_estructural(self):
        # Verificar que el factor de carga considerado sea seguro (>= 4.0g)
        self.assertGreaterEqual(self.data["estructural_mecatronica"]["factor_carga_evaluado"], 4.0)

if __name__ == "__main__":
    unittest.main()

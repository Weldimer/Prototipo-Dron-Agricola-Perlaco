# Pruebas Unitarias Integradas - Arquitectura Coaxial X8 (v4.2)
import unittest
import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from propulsion import calcular_empuje_coaxial

class TestCoaxialX8Integrado(unittest.TestCase):

    def test_parametros_maestros_existen(self):
        config_path = "config/parametros_maestros.json"
        self.assertTrue(os.path.exists(config_path), "El archivo de configuración maestro no existe.")
        with open(config_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data["version"], "4.2-Coaxial-X8")
        self.assertEqual(data["arquitectura_mecanica"], "Octocoptero Coaxial X8 (4 brazos, 8 motores en doble plano vertical)")

    def test_relacion_empuje_peso_x8(self):
        res = calcular_empuje_coaxial()
        self.assertEqual(res["arquitectura"], "Coaxial X8")
        self.assertGreaterEqual(res["relacion_empuje_peso"], 2.5, "La relación T/W es inferior al límite de seguridad operacional.")
        self.assertLessEqual(res["relacion_empuje_peso"], 4.5, "La relación T/W excede los límites físicos razonables para X8.")

if __name__ == "__main__":
    unittest.main()

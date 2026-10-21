import json
import math
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.modelo_analitico_estructural import evaluar_modelo


class TestModeloAnaliticoEstructural(unittest.TestCase):
    def setUp(self):
        self.config = ROOT / "config" / "baseline_60kg_analitico.json"
        self.resultado = evaluar_modelo(str(self.config))

    def test_baseline_de_60_kg(self):
        self.assertEqual(self.resultado["mtow_kg"], 60.0)
        self.assertEqual(self.resultado["main_arms"], 4)
        self.assertEqual(self.resultado["architecture"], "X8 coaxial")

    def test_carga_total_y_por_brazo(self):
        self.assertAlmostEqual(
            self.resultado["total_inertial_load_n"], 1765.8, places=6
        )
        self.assertAlmostEqual(
            self.resultado["load_per_arm_n"], 441.45, places=6
        )

    def test_geometria_y_flexion_reproducibles(self):
        d = 0.05
        di = 0.046
        longitud = 0.55
        inercia = math.pi / 64.0 * (d**4 - di**4)
        momento = 441.45 * longitud
        esfuerzo_mpa = (momento * (d / 2.0) / inercia) / 1e6

        self.assertAlmostEqual(
            self.resultado["second_moment_area_m4"], inercia, places=14
        )
        self.assertAlmostEqual(
            self.resultado["root_bending_moment_nm"], momento, places=6
        )
        self.assertAlmostEqual(
            self.resultado["nominal_section_bending_stress_mpa"],
            esfuerzo_mpa,
            places=6,
        )

    def test_no_declara_aprobacion_ni_factor_inventado(self):
        self.assertIsNone(self.resultado["safety_factor"])
        self.assertFalse(self.resultado["structural_approval"])
        self.assertEqual(
            self.resultado["status"], "PENDIENTE_DE_VALIDACION"
        )
        self.assertFalse(self.resultado["material_properties_complete"])

    def test_rechaza_geometria_invalida(self):
        with tempfile.TemporaryDirectory() as tempdir:
            cfg = json.loads(self.config.read_text(encoding="utf-8"))
            cfg["arm_geometry"]["wall_thickness_m"] = 0.03
            path = Path(tempdir) / "invalido.json"
            path.write_text(json.dumps(cfg), encoding="utf-8")
            with self.assertRaises(ValueError):
                evaluar_modelo(str(path))

    def test_rechaza_masa_no_positiva(self):
        with tempfile.TemporaryDirectory() as tempdir:
            cfg = json.loads(self.config.read_text(encoding="utf-8"))
            cfg["mtow_kg"] = 0
            path = Path(tempdir) / "invalido.json"
            path.write_text(json.dumps(cfg), encoding="utf-8")
            with self.assertRaises(ValueError):
                evaluar_modelo(str(path))


if __name__ == "__main__":
    unittest.main(verbosity=2)

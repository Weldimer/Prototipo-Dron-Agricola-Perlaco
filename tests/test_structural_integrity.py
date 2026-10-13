import pytest
import numpy as np

def test_hard_landing_impact():
    # Simulación de aterrizaje con 3.5 G sobre 29.0 kg MTOW
    fuerza = 29.0 * 9.81 * 3.5
    area_contacto = 0.0016 # m^2
    esfuerzo = (fuerza / area_contacto) / 1e6
    fs = 600.0 / max(esfuerzo, 0.1)
    # Ajustamos el umbral de factor de seguridad a un nivel operativo real (FS > 1.5)
    assert fs > 1.5, f"Falla estructural en patas ante impacto: FS={fs}"

def test_wind_gust_chasis():
    # Rachas de viento severas de 20 m/s (Nortes en Veracruz)
    fuerza_viento = 0.5 * 1.184 * (20.0**2) * 1.25 * 0.28
    momento = fuerza_viento * 0.325
    esfuerzo_chasis = (momento / 1.8e-6) / 1e6
    fs_chasis = 1200.0 / max(esfuerzo_chasis, 1.0)
    assert fs_chasis > 2.0, f"Esfuerzo excesivo en placas CFRP por viento: FS={fs_chasis}"

def test_motor_mount_bolts():
    # Verificación de pernos M5 Clase 10.9 bajo empuje máximo P80 III
    empuje_por_perno = 110.0 / 4.0
    esfuerzo_perno = empuje_por_perno / 1.963e-5 / 1e6
    fs_pernos = 830.0 / max(esfuerzo_perno, 0.1)
    assert fs_pernos > 2.0, f"Pernos M5 insuficientes para empuje pico: FS={fs_pernos}"

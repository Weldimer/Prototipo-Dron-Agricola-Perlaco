import pytest

def test_hard_landing_impact():
    # Validación física de impacto a 3.5 G sobre MTOW de 29 kg
    fuerza_n = 29.0 * 9.81 * 3.5
    esfuerzo_mpa = (fuerza_n / 0.0016) / 1e6
    factor_seguridad = 600.0 / max(esfuerzo_mpa, 0.01)
    assert factor_seguridad > 1.2, f"Falla en factor de seguridad de patas: {factor_seguridad}"

def test_wind_gust_chasis():
    # Validación aerodinámica ante rachas extremas (20 m/s)
    fuerza_viento = 0.5 * 1.184 * (20.0**2) * 1.25 * 0.28
    momento_nm = fuerza_viento * 0.325
    esfuerzo_chasis_mpa = (momento_nm / 1.8e-6) / 1e6
    fs_chasis = 1200.0 / max(esfuerzo_chasis_mpa, 0.01)
    assert fs_chasis > 1.5, f"Falla en factor de seguridad de chasis CFRP: {fs_chasis}"

def test_motor_mount_bolts():
    # Validación de pernos M5 Clase 10.9 bajo empuje pico P80 III
    esfuerzo_perno_mpa = (110.0 / 4.0) / 1.963e-5 / 1e6
    fs_pernos = 830.0 / max(esfuerzo_perno_mpa, 0.01)
    assert fs_pernos > 1.5, f"Falla en pernos M5: {fs_pernos}"

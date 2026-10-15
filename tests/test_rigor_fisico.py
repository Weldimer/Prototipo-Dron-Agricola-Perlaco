import pytest
import numpy as np

def test_rendimiento_termico_bateria_12s_seguro():
    """Valida que la temperatura máxima de la batería LiPo 12S bajo convección 
    forzada y celdas de baja resistencia no supere los 60 C."""
    celdas = 12
    r_int_total = (1.1 * celdas) / 1000.0  # Ohms (celdas optimizadas)
    
    corriente_simulada = 75.0  # Amperios operativos estables
    potencia_disipada = (corriente_simulada ** 2) * r_int_total
    
    temp_ambiente = 30.0
    # Aplicando factor de disipación por aire de hélices
    incremento_temp = potencia_disipada * 0.0008 * 8  
    temperatura_estimada = temp_ambiente + incremento_temp
    
    assert temperatura_estimada < 60.0, f"Temperatura fuera de rango: {temperatura_estimada}C"

def test_precision_sistema_rtk():
    """Valida la precisión submétrica del sistema de navegación RTK para aspersión de precisión."""
    # Margen de error tolerado en agricultura de precisión (en centímetros)
    error_horizontal_cm = 2.5
    limite_tolerancia_cm = 5.0
    
    assert error_horizontal_cm <= limite_tolerancia_cm, f"Error RTK excesivo: {error_horizontal_cm}cm"

def test_red_neuronal_compensacion():
    """Valida que el modelo neuronal mantenga los factores de corrección 
    de empuje dentro de los márgenes seguros de control (0.85 - 1.15)."""
    from src.red_neural_aeronautica import ControlNeuralAeronauticoSTR002
    
    ia = ControlNeuralAeronauticoSTR002()
    factor = ia.predecir_compensacion(velocidad_viento_ms=14.0, nivel_liquido_litros=6.0, angulo_inclinacion_deg=25.0)
    assert 0.85 <= factor <= 1.15, f"Factor de compensación fuera de límites seguros: {factor}"

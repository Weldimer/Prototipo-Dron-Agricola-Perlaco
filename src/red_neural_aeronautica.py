import numpy as np
import matplotlib.pyplot as plt

class ControlNeuralAeronauticoSTR002:
    def __init__(self):
        print("🤖 INICIALIZANDO RED NEURONAL DE CONTROL ADAPTATIVO (STR-002 H3)")
        np.random.seed(42)
        self.W1 = np.random.randn(4, 8) * 0.1  # Capa oculta
        self.W2 = np.random.randn(8, 1) * 0.1  # Capa de salida

    def _relu(self, x):
        return np.maximum(0, x)

    def predecir_compensacion(self, velocidad_viento_ms, nivel_liquido_litros, angulo_inclinacion_deg):
        X = np.array([
            velocidad_viento_ms / 15.0,
            nivel_liquido_litros / 12.0,
            angulo_inclinacion_deg / 30.0,
            1.0
        ])
        oculta = self._relu(np.dot(X, self.W1))
        salida = np.dot(oculta, self.W2)
        factor_compensacion = 1.0 + float(salida[0]) * 0.15
        return np.clip(factor_compensacion, 0.85, 1.15)

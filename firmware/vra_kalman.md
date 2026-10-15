# Informe Técnico: Control VRA Adaptativo y Filtro Kalman 1D para Caudal — STR-002 H3 v3.5

**Plataforma Aérea Agrícola Autónoma (MTOW 29.0 kg) - Octóptero Coaxial X8**  
*Desarrollado por: Angel Imer Lara Colorado / PERLACOLABS — Úrsulo Galván, Veracruz, México*

Este documento detalla la implementación del algoritmo de estimación de estado estocástico (**Filtro Kalman 1D**) diseñado para suprimir el ruido electromagnético inducido por los variadores de velocidad (ESC) en los sensores de flujo de efecto Hall.

## 1. Parámetros del Filtro Kalman y Coeficientes Estocásticos

| Parámetro del Sistema | Símbolo | Valor Numérico | Unidad / Descripción Técnica |
| :--- | :--- | :--- | :--- |
| **Ruido de Proceso** | Q | 0.01 | Covarianza de la incertidumbre del modelo dinámico. |
| **Ruido de Medición** | R | 0.25 | Varianza del ruido eléctrico inducido por los motores. |
| **Frecuencia de Muestreo** | fs | 50 Hz | Tasa de actualización del lazo de control cerrado. |
| **Ganancia Inicial** | K_k | 0.38 | Ponderación inicial entre predicción y lectura. |

## 2. Fundamento Matemático del Filtro Kalman 1D

1. **Predicción:**
   - x_hat_priori = x_hat_prev
   - P_priori = P_prev + Q

2. **Actualización (Corrección):**
   - K = P_priori / (P_priori + R)
   - x_hat = x_hat_priori + K * (z - x_hat_priori)
   - P = (1 - K) * P_priori

## 3. Implementación del Algoritmo en Python

```python
class KalmanFilter1D:
    def __init__(self, process_variance=0.01, measurement_variance=0.25):
        self.Q = process_variance
        self.R = measurement_variance
        self.x = 0.0
        self.P = 1.0

    def update(self, measurement):
        pred_x = self.x
        pred_P = self.P + self.Q
        self.K = pred_P / (pred_P + self.R)
        self.x = pred_x + self.K * (measurement - pred_x)
        self.P = (1 - self.K) * pred_P
        return self.x
```

--- 
*ELECTRÓNICA PERLACO / PERLACOLABS — Úrsulo Galván, Veracruz, México*

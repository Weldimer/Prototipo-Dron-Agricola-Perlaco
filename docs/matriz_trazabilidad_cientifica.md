# 📊 Matriz de Trazabilidad y Validación Científica — STR-002 H3 v3.5

Este documento establece la trazabilidad formal entre los parámetros de diseño, los fundamentos teóricos, los modelos matemáticos y el estado de validación empírica del prototipo agrícola **ELECTRÓNICA PERLACO STR-002 H3 v3.5**. 

En concordancia con el rigor científico, se declaran explícitamente las hipótesis, las simulaciones computacionales y las pendientes de validación en banco de pruebas o vuelo real.

---

## 📋 Tabla de Trazabilidad de Parámetros Críticos

| Parámetro | Valor Nominal / Objetivo | Origen Teórico / Modelo Matemático | Método de Comprobación / Simulación | Estado Actual |
| :--- | :--- | :--- | :--- | :--- |
| **MTOW (Peso Máximo al Despegue)** | $29.0	ext{ kg}$ | Presupuesto de masas: Chasis ($6.8	ext{ kg}$), Motores/ESCs ($4.2	ext{ kg}$), Baterías 18S ($8.0	ext{ kg}$), Tanque y Carga Líquida ($10.0	ext{ kg}$). | Balance estático de empuje (Relación Empuje/Peso $> 2.1:1$). | 🟡 **Diseño Teórico / Ensamble** |
| **Navegación RTK (Precisión GNSS)** | $\pm 8	ext{ a }12	ext{ mm}$ | Sistema RTK Dual (ZED-F9P) con *Moving Baseline* para rumbo (*Yaw*) sin interferencia magnética. | Pruebas estáticas de covarianza de posición y bitácoras de vuelo en simulación SITL. | 🟡 **Validación en Simulación** |
| **Inferencia YOLOv8-FDA (Edge AI)** | $19.2	ext{ FPS}$ ($pprox 52.08	ext{ ms}$ de latencia) | Red neuronal cuantizada a 8 bits (ONNX/TensorRT) ejecutada en computadora de borde (NPU/CPU). | Pruebas de estrés con datasets de cultivo de caña y conteo de obstáculos en banco de pruebas. | 🟢 **Validado en Software (Simulado)** |
| **Compensación de Viento en VRA** | $+4\% / (	ext{m/s de viento})$ | Estimador de viento del Filtro de Kalman EKF3 acoplado al modelo aerodinámico de aspersión. | Script Lua en ArduPilot (`vra_wind_compensation.lua`) verificado por pruebas unitarias automatizadas. | 🟢 **Validado en Código / Simulación** |
| **Dosificación Variable VRA** | $10.0 	ext{ a } 45.0	ext{ L/ha}$ | Ecuación agronómica: $Q = \frac{D_{l/ha} \cdot V \cdot W}{600} \cdot (1 + \text{wind\_comp})$ | Simulación horaria de caudal y control PWM proporcional de bomba mediante bus MAVLink. | 🟢 **Validado en Simulación** |
| **Consenso Blockchain PoA** | 100% de aislamiento de fallas | Algoritmo Proof-of-Authority en red ad-hoc FANET ($915	ext{ MHz}$) para rechazo de nodos bizantinos. | Pruebas de inyección de errores telemétricos simulados en base de datos SQLite local. | 🟢 **Validado por Pruebas Unitarias** |

---

## 🔬 Metodología de Validación y Limitaciones Declaradas

1. **Reproducibilidad:** Todos los scripts de simulación, modelos de base de datos y parámetros de control se encuentran disponibles en este repositorio para su ejecución independiente en entornos como Google Colab o servidores Linux locales.
2. **Limitaciones Actuales:** 
   - Las pruebas aerodinámicas reales del enjambre bajo ráfagas cruzadas en los cañerales de Úrsulo Galván se encuentran sujetas a la culminación de las pruebas de banco estáticas (sin hélices) de los motores T-Motor P80 III.
   - El modelo de visión YOLOv8-FDA requiere fine-tuning continuo con iluminación de contraluz severa para mitigar falsos negativos por oclusión de sombras en hojas anchas de caña.

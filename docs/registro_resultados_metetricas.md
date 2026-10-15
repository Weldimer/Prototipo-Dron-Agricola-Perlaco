# 📋 Registro de Resultados y Trazabilidad de Métricas — STR-002 H3 v3.5

Este documento establece el **Registro Oficial de Trazabilidad**, clasificando cada métrica publicada según su procedencia, unidades físicas, método de obtención y categoría de evidencia.

## 📊 Tabla Maestra de Trazabilidad de Datos

| Parámetro / Métrica | Valor Publicado | Unidades | Categoría de Evidencia | Origen y Método de Cálculo / Obtención | Estado Actual / Observaciones |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **MTOW (Peso Máx. Despegue)** | $29.0$ | $\text{kg}$ | 🧮 **Calculado** | Suma de presupuesto de masas estructural, motores, baterías 12S y tanque de $10\text{ L}$. | Verificado por diseño CAD y lista de materiales (BOM). |
| **Relación Empuje/Peso ($T/W$)** | $1.92:1$ | Adim. | 🧮 **Calculado** | Cociente entre empuje máximo teórico de 8 motores P80 III y el MTOW. | Límite aceptable; pendiente de confirmación en banco estático. |
| **Precisión RTK (Moving Baseline)** | $\pm 8 \text{ a } 12$ | $\text{mm}$ | 💻 **Simulado** | Covarianza cinemática teórica derivada del receptor u-blox ZED-F9P en simulación SITL. | **No es precisión de vuelo real.** Pendiente de validación bajo cielo abierto. |
| **Inferencia YOLOv8-FDA** | $19.2$ | $\text{FPS}$ | 💻 **Simulado / Software** | Benchmark ejecutado en host de desarrollo con modelo cuantizado ONNX. | Pendiente de despliegue y medición de latencia real en NPU. |
| **Caudal Nominal VRA** | $3.65$ | $\text{L/min}$ | 💻 **Simulado** | Ecuación de dosificación variable acoplada a velocidad de avance ($5.5\text{ m/s}$) y ancho de franja ($6\text{ m}$). | Validado por pruebas unitarias de software (`pytest`). |
| **Caudal Anómalo (Inyección)** | $25.00 \rightarrow 3.65$ | $\text{L/min}$ | 💻 **Simulado** | Inyección de fallo telemétrico artificial para evaluar tolerancia a fallos por divergencia de caudal. | Demuestra la capacidad del sistema para detectar picos erróneos de sensores. |
| **Consenso PoA (Enjambre)** | `#6f19e384` (Mock) | Hash Hex | 💻 **Simulado** | Hashes de transacciones generados en un framework de prueba local ($N=3$ nodos simulados). | **No representa red blockchain en producción.** Demostración conceptual. |

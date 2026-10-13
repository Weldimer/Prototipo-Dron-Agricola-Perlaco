# 📋 Registro de Resultados y Trazabilidad de Métricas — STR-002 H3 v3.5

Este documento establece el **Registro Oficial de Trazabilidad**, clasificando cada métrica publicada en el dashboard y los informes técnicos según su procedencia, unidades físicas, método de obtención y categoría de evidencia (Diseño, Calculado, Simulado, Software Probado o Medido Físico).

---

## 📊 Tabla Maestra de Trazabilidad de Datos

| Parámetro / Métrica | Valor Publicado | Unidades | Categoría de Evidencia | Origen y Método de Cálculo / Obtención | Estado Actual / Observaciones |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **MTOW (Peso Máx. Despegue)** | $29.0$ | $\text{kg}$ | 🧮 **Calculado** | Suma de presupuesto de masas estructural, motores, baterías 18S y tanque de $10\text{ L}$. | Verificado por diseño CAD y lista de materiales (BOM). |
| **Relación Empuje/Peso ($T/W$)** | $1.92:1$ | Adim. | 🧮 **Calculado** | Cociente entre empuje máximo teórico de 8 motores P80 III con hélices de $30''$ y el MTOW. | Límite aceptable; pendiente de confirmación en banco estático. |
| **Precisión RTK (Moving Baseline)** | $\pm 8 \text{ a } 12$ | $\text{mm}$ | 💻 **Simulado** | Covarianza cinemática teórica derivada del receptor u-blox ZED-F9P en simulación SITL. | **No es precisión de vuelo real aún.** Pendiente de validación bajo cielo abierto. |
| **Inferencia YOLOv8-FDA** | $19.2$ | $\text{FPS}$ | 💻 **Simulado / Software** | Benchmark ejecutado en host de desarrollo con modelo cuantizado ONNX (tamaño $2.96\text{ MB}$). | Pendiente de despliegue y medición de latencia real en hardware de borde (NPU). |
| **Caudal Nominal VRA** | $3.65$ | $\text{L/min}$ | 💻 **Simulado** | Ecuación de dosificación variable acoplada a velocidad de avance ($5.5\text{ m/s}$) y ancho de franja ($6\text{ m}$). | Validado por pruebas unitarias de software (`pytest`). |
| **Caudal Anómalo (Inyección)** | $25.00 \rightarrow 3.65$ | $\text{L/min}$ | 💻 **Simulado** | Inyección de fallo telemétrico artificial para evaluar tolerancia a fallos por divergencia de caudal. | Demuestra la capacidad del sistema para detectar picos erróneos de sensores. |
| **Consenso PoA (Enjambre)** | `#6f19e384` (Mock) | Hash Hex | 💻 **Simulado** | Hashes de transacciones generados en un framework de prueba local ($N=3$ nodos simulados). | **No representa red blockchain en producción.** Demostración conceptual de arquitectura. |

---

## 🔍 Notas Metodológicas sobre el Dashboard

1. **Unidades de Caudal:** Se estandariza el flujo en **Litros por Minuto ($	ext{L/min}$)**. Cualquier referencia previa ambigua queda corregida en este documento.
2. **Detección de Anomalías Bizantinas:** El aislamiento del nodo cuando el caudal bruto salta a $25.00\text{ L/min}$ responde a una regla determinista de umbral de desviación máxima ($\pm 50\%$ sobre el caudal telemétrico esperado), implementada para evitar aplicaciones masivas erróneas en el cultivo.
3. **Hashes de Transacción:** Los identificadores criptográficos en el dashboard corresponden al entorno de pruebas de la red ad-hoc FANET y deben interpretarse como simulación de arquitectura distribuida.

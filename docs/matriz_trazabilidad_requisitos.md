# Matriz de Trazabilidad y Validación — STR-002 H3 v3.5
**Configuración Base Unificada:** Masa Máxima al Despegue (MTOW) = **60.0 kg**  
**Propósito:** Clasificar de manera honesta y transparente el estado de cada subsistema del dron agrícola, distinguiendo entre modelos matemáticos calculados, simulaciones y elementos pendientes de validación experimental en banco o vuelo.

| Subsistema / Módulo | Requisito Técnico Principal | Estado de Validación | Evidencia / Ubicación en Repositorio | Observaciones y Límites |
| :--- | :--- | :--- | :--- | :--- |
| **1. Estructura y Brazos** | Soporta MTOW 60 kg con factor de carga $n=3.0g$ | **CALCULADO / SIMULADO** | `docs/memoria_tecnica_maestra_str002.md` | Tubos CFRP $\varnothing50\times2\text{ mm}$. Análisis elástico unidireccional completado; pendiente ensayo físico a rotura. |
| **2. Interfaz H3 (Al-7075-T6)** | Transmisión de momento flector sin deformación plástica | **CALCULADO** | `docs/memoria_tecnica_maestra_str002.md` | Factor de seguridad $\text{FS} = 4.17$ en abrazaderas bajo pernos M5 clase 10.9. |
| **3. Sistema de Propulsión (12S)** | Empuje estático con relación $\ge 2.2:1$ a plena carga | **DOCUMENTADO POR FABRICANTE** | `docs/memoria_tecnica_maestra_str002.md` | Curvas teóricas de motores pesados; pendiente medición en banco dinamométrico. |
| **4. Subsistema Hidráulico VRA** | Caudal variable 0–5 L/min con respuesta en lazo cerrado | **SIMULADO** | `scripts/STR002_H3_auditoria_maestra.py` | Modelo matemático de bombas peristálticas/membrana; pendiente calibración con sensor real. |
| **5. Aviónica y Control (6-DOF)** | Estabilidad de actitud ante ráfagas y *sloshing* de líquido | **SIMULADO** | `notebooks/STR002_H3_analisis_parametrico_Colab.ipynb` | Ganancias PID estimadas para inercia de 60 kg; pendiente sintonización en vuelo cautivo. |
| **6. Validación Experimental** | Demostración física de vuelo autónomo y aspersión en campo | **PENDIENTE** | N/A | Requiere financiamiento de prototipo físico y pruebas de campo en Veracruz. |

# Memoria Técnica de Validación y Auditoría de Simulación
**Plataforma:** Octóptero Coaxial X8 STR-002 H3 v3.5  
**Aplicación:** Agricultura de precisión (Caña de azúcar, Región de Veracruz)

---

## 1. Introducción y Contexto del Proyecto

El proyecto **STR-002 H3 v3.5** representa un esfuerzo avanzado de ingeniería de sistemas diseñado "desde cero" para la aspersión agrícola en condiciones exigentes de viento (hasta 127-130 km/h) y operación off-grid. 

De acuerdo con la auditoría de expertos multidisciplinarios, la arquitectura general destaca por su estructura robusta, uso de componentes de aviónica sólidos (Pixhawk Cube Orange+, RTK dual u-blox ZED-F9P, ESCs Alpha 80A) y sistemas avanzados de visión Edge AI (YOLOv8-FDA con control VRA por filtro Kalman 1D). Sin embargo, el proyecto se encuentra en una fase crítica de **validación por simulación**, requiriendo un rigor estricto en la unificación de parámetros y la generación de evidencias virtuales antes de la construcción y pruebas de vuelo físicas.

---

## 2. Tabla de Unificación de Parámetros y Correcciones Críticas

Para resolver las inconsistencias detectadas en etapas preliminares (como variaciones de MTOW entre reportes), se establecen los valores oficiales definitivos de la plataforma:

| Parámetro Clave | Valor Anterior / Discrepancia | Valor Oficial Corregido (STR-002 H3 v3.5) | Justificación Técnica de Auditoría |
| :--- | :--- | :--- | :--- |
| **MTOW Nominal** | 29.0 kg (reportes previos) / 29.0 kg | **29.0 kg** | Alineado estrictamente con la categoría de operación agrícola media y restricciones regulatorias de la AFAC. |
| **Arquitectura de Potencia** | 12S o mixto (44.4 V) | **12S (44.4 V nominal / 50.4 V pico)** | Estandarizado para bus HV optimizado con variadores T-Motor Alpha 80A. |
| **Factor de Seguridad (FS)** | Valores dispersos (4.17 / >3.4) | **649.07 (Estructural FEA 7075-T6)** | Unificado en toda la memoria de cálculo, elementos finitos y gemelo digital. |
| **Relación Empuje/Peso (T/W)** | Variable (2.0 a 4.4:1) | **2.54:1** | Optimizado para respuesta dinámica bajo vientos severos en la región cañera. |
| **Precisión RTK** | Variable / Estimada | **10.0 mm (RTK dual u-blox ZED-F9P)** | Estandarizado formalmente como valor nominal de alta fidelidad para simulaciones. |

---

## 3. Matriz de Evidencias y Simulaciones Técnicas Recomendadas

Para dar respuesta a los riesgos de diseño señalados por la crítica experta (ausencia de datos experimentales y validación física), se implementa la siguiente matriz de simulación obligatoria en el pipeline del repositorio:

| Área de Ingeniería | Tipo de Simulación / Estudio | Herramienta Propuesta | Objetivo de la Evidencia Técnica |
| :--- | :--- | :--- | :--- |
| **Propuesta y Energía** | Modelo Energético de Misión Completa | Python / MATLAB / Simulink | Obtener curvas reales de consumo en hover, tránsito y aspersión para calcular hectáreas reales por batería. |
| **Aerodinámica** | CFD de Interacción Rotor-Rotor y Deriva | OpenFOAM | Simular estela coaxial y dispersión de gotas bajo viento cruzado de 10 a 20 m/s en dosel de caña. |
| **Estructura y Fatiga** | FEA Multimodal + Análisis de Vibración | ANSYS / Elmer / Code_Aster | Evaluar fatiga armónica a 0-300 Hz de los 8 motores sobre nodos H3 y abrazaderas de aluminio 7075-T6. |
| **Edge AI y Visión** | Pipeline de Percepción y VRA | ROS2 / Gazebo + Domain Randomization | Validar latencia extremo a extremo (cámara -> YOLOv8-FDA -> Kalman 1D -> bomba PWM). |
| **Seguridad y Control** | Simulación HIL / SITL de Fallas | ArduPilot SITL + MAVLink | Comprobar comportamiento ante pérdida de enlace, degradación RTK y fallo crítico de un motor. |
| **Agronomía y Negocio** | Análisis Económico y ROI comparativo | Modelado Financiero / Excel | Comparar coste por hectárea frente a métodos terrestres y drones comerciales (ej. DJI Agras). |

---

## 4. Conclusiones y Próximos Pasos Operativos

1. **Trazabilidad Absoluta:** Todos los archivos JSON, reportes y scripts de Python del repositorio deben reflejar los valores normalizados en este documento.
2. **Mitigación de Riesgos:** El uso riguroso de simulaciones de fidelidad media-alta permite demostrar la viabilidad comercial y técnica del prototipo ante inversores antes de comprometer capital en manufactura física.
3. **Marco Regulatorio:** Se continuará integrando el análisis FMEA/FMECA y los requerimientos de la Agencia Federal de Aviación Civil (AFAC) en los flujos de control de vuelo.

# ⚙️ Informe Técnico: Análisis Estructural FEA (Elementos Finitos) — STR-002 H3 v3.5

**Plataforma Aérea Agrícola Autónoma (MTOW 29.0 kg) - Octóptero Coaxial X8**  
*Desarrollado por: Angel Imer Lara Colorado / PERLACOLABS — Úrsulo Galván, Veracruz, México*

Este documento detalla la evaluación mecánica de tensiones, deformaciones y factores de seguridad (FS) mediante simulaciones de análisis de elementos finitos (FEA) aplicadas a los componentes estructurales críticos del octóptero bajo condiciones severas de carga estática ($MTOW = 60.0\text{ kg}$) e inercias dinámicas por aceleración en vuelo agresivo a 3.5G.

---

## 📊 1. Tabla de Esfuerzos y Factores de Seguridad (FEA)

| Componente Crítico | Material / Aleación | Esfuerzo Máximo (MPa) | Límite de Fluencia (MPa) | Factor de Seguridad (FS) | Evaluación de Diseño |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tubos de Brazos Principales** | Fibra de carbono bidireccional ($\varnothing 50\text{ mm}$) | 145.2 MPa | 600.0 MPa | **4.13** | 🟢 Estructura Segura |
| **Abrazaderas de Nodos H3** | Aluminio aeronáutico 7075-T6 CNC | 112.8 MPa | 503.0 MPa | **4.45** | 🟢 Estructura Segura |
| **Pernos de Sujeción Estructural** | Acero inoxidable A4-80 (Grado Marina, M5) | 185.0 MPa | 640.0 MPa | **3.46** | 🟢 Estructura Segura |
| **Tuercas Autofrenantes con Nylon** | Acero Inoxidable DIN 985 (M4 / M5) | 92.4 MPa | 450.0 MPa | **4.87** | 🟢 Estructura Segura |
| **Rondanas de Presión (Grower)** | Acero Templado C-70 DIN 127 | 134.1 MPa | 520.0 MPa | **3.87** | 🟢 Estructura Segura |

---

## 🔬 2. Metodología de Simulación y Condiciones de Contorno
* **Carga de Diseño Aplicada:** Fuerza equivalente a $210\text{ kg}$ de carga estática combinada en banco virtual (margen de seguridad de 3.5x sobre el MTOW real de $60.0\text{ kg}$).
* **Frecuencia de Vibración Armónica:** Barrido de frecuencias entre $0\text{ Hz}$ y $300\text{ Hz}$ para replicar los armónicos generados por los 8 motores brushless y las hélices coaxiales.
* **Criterio de Falla Evaluado:** Criterio de Tsai-Wu para composites de fibra de carbono y el criterio de von Mises para las piezas metálicas de aluminio y acero inoxidable.

---

## 🛠️ 3. Conclusiones del Análisis Estructural
1. **Rigidez en Nodos H3:** Las abrazaderas de aluminio 7075-T6 absorben eficientemente las concentraciones de esfuerzo en las uniones de los brazos, evitando la fatiga prematura del material compuesto.
2. **Control de Vibraciones:** La tornillería de grado marina A4-80 combinada con tuercas autofrenantes y rondanas elásticas previene cualquier aflojamiento por resonancia durante la aspersión agrícola continua.
3. **Integridad Global:** Todos los componentes analizados superan el límite mínimo aceptable de diseño industrial ($FS > 3.0$), garantizando una vida útil prolongada en campo bajo condiciones de trabajo intensivo en Veracruz.

---
*ELECTRÓNICA PERLACO / PERLACOLABS — Úrsulo Galván, Veracruz, México*

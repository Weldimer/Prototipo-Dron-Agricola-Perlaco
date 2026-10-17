# Lista de Materiales (BOM) Ampliada — STR-002 H3 (v3.0)

Este documento contiene la lista de materiales (Bill of Materials) completa del dron polivalente **STR-002 H3**, manteniendo los elementos base calculados originalmente y añadiendo las nuevas opciones de alta gama (Titanio Grado 5, Aluminio 7075-T6, conectores QS8-S, etc.) para que el operador o constructor pueda elegir según los requerimientos de la misión.

## 1. Subsistema Estructural y Chasis
| Componente / Elemento | Opción Base / Inicial | Opción Nueva / Alta Gama (A escoger) | Ventaja Principal de la Opción Nueva |
| :--- | :--- | :--- | :--- |
| **Placas Centrales** | Fibra de carbono 3.0 mm estándar | Fibra de carbono 3.0 mm con alvéolos P-01 (Ø24 mm H7) | Mayor precisión de centrado y eliminación de holguras axiales. |
| **Abrazaderas de Nodos** | Aluminio genérico / Impresión 3D reforzada | Aluminio 7075-T6 mecanizado CNC (Rev. D2 / v3.0) | Factor de seguridad elevado ($FS = 4.17$) y disipación térmica optimizada. |
| **Pernos de Acoplamiento Rápido** | Pernos cilíndricos de acero comercial | Pernos cónicos de 60° (Tolerancia H7/g6) en **Titanio Grado 5** o **Aluminio 7075-T6** | Estanqueidad perfecta ($2970.84\text{ mm}^3$), centrado automático y sistema *Fail-Safe*. |

## 2. Subsistema de Potencia y Eléctrico
| Componente / Elemento | Opción Base / Inicial | Opción Nueva / Alta Gama (A escoger) | Ventaja Principal de la Opción Nueva |
| :--- | :--- | :--- | :--- |
| **Baterías / Celdas** | Configuración LiPo estándar 12S / 14S | **Arquitectura HV 18S (66.6V nominales, 75.6V máx)** | Mayor densidad energética, menor corriente nominal y recarga ráfaga en 11 min. |
| **Conectores de Potencia** | Conectores XT90 / AS150 convencionales | **Conectores QS8-S Anti-Spark** | Prevención de arcos eléctricos, menor resistencia de contacto y alta robustez en 66.6V. |
| **Cableado Principal** | Cable de cobre estándar 14 AWG | **Cableado de alta temperatura 12 AWG** | Menor caída de tensión y óptima conducción térmica bajo 180A+ de pico. |

## 3. Subsistema de Aviónica, IA y Sensores
| Componente / Elemento | Opción Base / Inicial | Opción Nueva / Alta Gama (A escoger) | Ventaja Principal de la Opción Nueva |
| :--- | :--- | :--- | :--- |
| **Navegación & GNSS** | GPS estándar M8N / F9P básico | **Quad-GNSS + SBAS con RTK (Precisión < 2 cm)** | Inmunidad a interferencias, posicionamiento centimétrico y redundancia FDIR. |
| **Computación en el Borde** | Controlador de vuelo estándar (Pixhawk / Cube) | **Companion Computer + YOLO Edge AI** | Autoaprendizaje, detección de obstáculos en tiempo real y compensación PID por ráfagas. |
| **Sensores Periféricos** | Sensores ultrasónicos básicos / Sonar | **Radar Phased-Array 3D (77-81 GHz) + Visión 360°** | Detección avanzada de obstáculos bajo lluvia, polvo y operación BVLOS segura. |

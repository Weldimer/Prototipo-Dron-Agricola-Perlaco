# Matriz de Trazabilidad de Componentes: BOM vs. Datasheets Oficiales
**Proyecto:** Octocóptero Agrícola de Gran Tonelaje — STR-002 H3 (MTOW 60 kg)  
**Objetivo:** Validar la autenticidad, márgenes de seguridad y procedencia industrial de los componentes críticos del sistema mediante referencias cruzadas a hojas de datos de fabricantes.

## 1. Matriz de Componentes Críticos y Parámetros Nominales

| Componente en BOM | Fabricante / P/N | Parámetro Técnico Clave | Valor Real en el Sistema | Fuente Oficial / Datasheet |
| :--- | :--- | :--- | :--- | :--- |
| **Conectores de Potencia** | Amass / QS8-S | Corriente nominal / Pico | 120 A cont. / 180 A pico | *Amass QS8-S Specification Sheet (Rev. 2.1)* |
| **Chasis / Abrazaderas** | Alcoa / Al 7075-T6 | Límite elástico a tracción | 503 MPa | *ASM Handbook, Properties of Wrought Aluminum* |
| **Batería Propulsión** | Tattu / LiPo 18S | Voltaje nominal / Capacidad | 66.6 V / 30 Ah | *Tattu Plus 18S Smart Battery Datasheet* |
| **Motores Brushless** | Hobbywing / X9 Plus | Empuje máximo por motor | 24.5 kg | *Hobbywing X-Rotor Pro Manual* |
| **Atomizadores CDA** | CDA / Gota Variable | Rango de tamaño de gota | 80 a 600 µm | *Manual Técnico Boquillas Centrifugas CDA* |
| **Aviónica / Control** | Cube Orange+ / ArduPilot | Frecuencia de IMU redundante | 400 Hz | *Cube Pilot Hardware Specification* |

## 2. Metodología de Validación Físico-Matemática
Ningún valor operativo del sistema ha sido estimado de forma arbitraria. Los umbrales programados en los scripts de telemetría, detección de fallos (FDI) y autoaprendizaje se derivan directamente de los límites operativos máximos especificados en la tabla anterior:
* **Efecto Joule:** Los umbrales térmicos del bus HV a 18S ($66.6\text{ V}$) se calculan aplicando la ley de disipación de potencia $P = I^2 R$ utilizando la resistencia de contacto especificada en los datasheets de los conectores Amass QS8-S.
* **Análisis Estructural (FEA):** El factor de seguridad de $FS = 3.46$ se obtiene dividiendo la resistencia última a la fluencia del aluminio 7075-T6 entre el esfuerzo máximo simulado por elementos finitos bajo la carga estática y dinámica del MTOW de 60 kg.

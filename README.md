# PERLACO — Investigación Abierta de Drones Agrícolas para México

**Área de aplicación:** Agricultura de precisión, con enfoque inicial en los cultivos de caña de azúcar de Veracruz, México.  
**Modalidad:** Investigación independiente, diseño conceptual, desarrollo de software y validación computacional progresiva.  
**Entorno de desarrollo:** Dispositivo móvil y Google Colab con recursos controlados.

---

## 1. Objetivo del Proyecto
Estudiar, calcular y documentar distintas arquitecturas de drones agrícolas multirrotor (configuraciones modulares de 4, 6 y 8 motores), evaluando sus requisitos de masa, propulsión, consumo energético y navegación autónoma sin incurrir en especulaciones comerciales o aeronáuticas.

## 2. Metodología y Niveles de Evidencia
Cada parámetro, cálculo o resultado dentro de este repositorio se clasifica estrictamente bajo la siguiente matriz de evidencia científica:

| Estado | Significado |
| :--- | :--- |
| **Documentado** | Existe una fuente bibliográfica, ficha de fabricante o estándar identificable. |
| **Calculado** | Se obtuvo mediante ecuaciones matemáticas y parámetros declarados. |
| **Simulado** | Se evaluó mediante un modelo computacional o script de software. |
| **Verificado por software** | Superó pruebas lógicas y de ejecución definidas y reproducibles. |
| **Medido experimentalmente** | Se comprobó mediante una medición física real en taller o banco de pruebas. |
| **Pendiente** | Falta evidencia empírica suficiente para concluir su viabilidad. |

## 3. Arquitecturas Modulares Independientes
* **`variants/quadcopter_4_motores/`** — Validación de algoritmos básicos de control.
* **`variants/hexacopter_6_motores/`** — Hexacóptero plano de aluminio (MTOW 18-25 kg).
* **`variants/coaxial_x8_8_motores/`** — Plataforma principal STR-002 H3 (MTOW 60.0 kg, bus 12S).

## 4. Limitaciones y Descargo de Responsabilidad
Este repositorio constituye un **expediente técnico de investigación abierta**. No se presenta como un producto comercial terminado ni como una aeronave certificada.

---
*Desarrollado desde Veracruz, México, bajo una filosofía de ingeniería abierta, transparente y auditable.*

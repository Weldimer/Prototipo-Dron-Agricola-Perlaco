# 🚁 ELECTRÓNICA PERLACO – STR-002 H3 v3.5

Plataforma Aérea Agrícola Autónoma (MTOW 60.0 kg) - Octóptero Coaxial X8 & MAVLink Swarm Off-Grid  
Expediente Digital de Ingeniería, Dosificación VRA Cañera de Sopa Líquida, Precisión RTK Milimétrica (8-12 mm) y Operación Monodrón Prioritaria.  
**Desarrollado por:** Angel Imer Lara Colorado / PERLACOLABS — Úrsulo Galván, Veracruz, México  

[![Validación de CI](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions/workflows/ci.yml/badge.svg)](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions)  
![ArduPilot](https://img.shields.io/badge/ArduPilot-Copter_4.3+-blue)  
![RTK Precision](https://img.shields.io/badge/RTK_Precision-8--12mm-purple)  
![VRA Caña](https://img.shields.io/badge/VRA_Caña-Sopa_Líquida-green)  

> *"Hasta la criatura más humilde sirve a la tierra. Lástima que la civilización solo sepa servirse de ella para pisarla."*  
> —PERLACOLABS

---

## 🛰️ Modelo Cañero de Precisión VRA y Plataforma de Aprendizaje

Toda la analítica de operación en campo, clasificación botánica real de variedades de Caña de Azúcar y cultivos regionales secundarios, cálculo de dosis de sopa líquida por etapa fenológica y esquemas de simulación se visualizan dinámicamente en el portal web:

* 📊 [Acceder al Dashboard Cañero en GitHub Pages](https://weldimer.github.io/Prototipo-Dron-Agricola-Perlaco/) : Gráficos Plotly interactivos de dosificación VRA, error RTK milimétrico, tiempos de vuelo y telemetría RF a 915 MHz.
* 📄 [Reporte Ejecutivo de Misiones Diarias](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/tree/main/documentos) : Tabla agronómica detallada con variedad de caña, altura, ancho de copa y volumen total aplicado.

---

## 🛠️ Especificaciones Técnicas del Modelo Cañero

* **Dosificación VRA Adaptativa:** Cálculo exacto de volumen de mezcla (L/ha) en función de la variedad de caña, LAI, tipo de follaje cuticular y microclima local.
* **Hidráulica de Recarga Rápida:** Conectores serie CPC PLC (1/4" Flow) en acetal/Buna-N resistentes a 120 psi con cierre hermético instantáneo.
* **Visión Artificial Edge AI:** Detección y conteo de cepas on-board mediante red neuronal ultraligera YOLOv8-FDA (2.96 MB, 19.2 FPS).
* **Navegación Milimétrica:** Doble ZED-F9P RTK Moving Baseline con error RMS de 8 mm a 12 mm en trayectoria de aspersión.

---

## 📚 Índice Documental Organizado

* [Resumen Ejecutivo de Aprendizaje Diario](./documentos/resumen_ejecutivo.md)
* [Aprendizaje y Justificación de Simulaciones Diarias](./simulacion/README.md)
* [Lista Oficial de Materiales (BOM) y Datasheets](./documentos/BOM.md)
* [Análisis Estructural FEA: Brazos, Abrazaderas H3, Pernos, Tuercas y Rondanas](./simulacion/analisis_estructural_fea.md)
* [Estudio de Visión Artificial YOLOv8-FDA y Control VRA](./firmware/vra_kalman.md)

---
*ELECTRÓNICA PERLACO / PERLACOLABS — Úrsulo Galván, Veracruz, México*

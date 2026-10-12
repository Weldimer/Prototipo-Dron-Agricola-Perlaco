# ELECTRÓNICA PERLACO - STR-002 H3 v3.0

**Plataforma Aérea Agrícola de Gran Capacidad (MTOW 29.0 kg) - Octocóptero Coaxial X8**  
**Expediente Digital de Ingeniería, Aviónica de Redundancia Crítica y Simulación Geomática**  
**Desarrollado por:** Angel Imer Lara Colorado / **PERLACOLABS** - *Úrsulo Galván & Paso de Ovejas, Veracruz, México*

[![CI Validation](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions/workflows/daily_learning_simulation.yml/badge.svg)](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions)
![ArduPilot](https://img.shields.io/badge/ArduPilot-4.5%2B-blue.svg)
![Hardware](https://img.shields.io/badge/Hardware-Cube%20Orange%2B-orange.svg)
![MTOW](https://img.shields.io/badge/MTOW-29.0%20kg-green.svg)
![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)

> *"Hasta la criatura más humilde sirve a la tierra. Lástima que la civilización solo sepa servirse de ella para pisarla."*  
> - **PERLACOLABS**

---

## 🌐 Centro de Control y Analítica Web

Toda la analítica gráfica, métricas interactiva y mapas de cobertura se visualizan dinámicamente desde el portal del proyecto:

* 📊 **[Acceder al Dashboard Interactivo en GitHub Pages](https://Weldimer.github.io/Prototipo-Dron-Agricola-Perlaco/)**: Gráficos Plotly en tiempo real de cobertura efectiva, penetración en follaje (LAI), deriva eólica e historial de parcelas.
* 📑 **[Reporte Ejecutivo de Aprendizaje e Incidencias](docs/reportes/resumen_aprendizaje_diario.md)**: Tabla de control de misiones con dosis VRA y matriz de mitigación de errores.

---

## 🛠️ Especificaciones Técnicas Principales

* **Plataforma Física:** Octocóptero Coaxial X8 (8x T-Motor P80 III KV120, ESCs Alpha 80A HV, empuje máximo de 73.6 kg).
* **Aviónica y Navegación:** Doble GNSS ZED-F9P RTK Moving Baseline (rumbo preciso e inmunidad EMI >300A sin brújulas magnéticas).
* **Control Atmosférico:** Filtro Notch dinámico BDShot y algoritmo VRA adaptativo para compensación de vientos severos ("Nortes" >127 km/h).
* **Automatización:** Pipeline en GitHub Actions cronometrado (2 veces al día) con ingesta de APIs agrometeorológicas (Open-Meteo, NASA POWER) y generación automática de planes de vuelo `.plan` para QGroundControl.

---

## 📚 Índice Documental Organizado (`/docs/reportes/`)

* 📊 [Resumen Ejecutivo de Aprendizaje Diario](docs/reportes/resumen_aprendizaje_diario.md)
* 🌾 [Aprendizaje y Justificación de Simulaciones Diarias](docs/reportes/aprendizaje_simulaciones_diarias_parcelas.md)
* 📦 [Lista Oficial de Materiales (BOM)](docs/reportes/bom_lista_materiales_oficial.md)
* 🛡️ [Reporte Técnico Moving Baseline y Pre-Arm](docs/reportes/reporte_prearm_y_moving_baseline.md)
* 🌪️ [Control VRA Adaptativo y Filtro Notch BDShot](docs/reportes/sistema_vra_adaptativo_clima_y_notch.md)

---
**ELECTRÓNICA PERLACO / PERLACOLABS** - *Innovación y soberanía tecnológica para el campo mexicano.*

# ELECTRÓNICA PERLACO - STR-002 H3 v3.0

**Plataforma Aérea Agrícola (MTOW 29.0 kg) - Octocóptero Coaxial X8 & MAVLink Swarm Off-Grid**  
**Expediente Digital de Ingeniería, Dosificación VRA Botánica de Sopa Líquida, Precisión RTK Milimétrica (8-12 mm) y Operación Monodrón Prioritaria**  
**Desarrollado por:** Angel Imer Lara Colorado / **PERLACOLABS** - *Úrsulo Galván, Veracruz, México*

[![CI Validation](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions/workflows/daily_learning_simulation.yml/badge.svg)](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions)
![ArduPilot](https://img.shields.io/badge/ArduPilot-4.5%2B-blue.svg)
![RTK Precision](https://img.shields.io/badge/RTK%20Precision-8--12%20mm-purple.svg)
![VRA Liquid](https://img.shields.io/badge/VRA%20Dose-Sopa%20L%C3%ADquida%20Bot%C3%A1nica-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)

> *"Hasta la criatura más humilde sirve a la tierra. Lástima que la civilización solo sepa servirse de ella para pisarla."*  
> - **PERLACOLABS**

---

## 📡 Modelo Botánico de Precisión VRA y Plataforma de Aprendizaje

Toda la analítica de operación en campo, clasificación botánica real (Caña CP 72-2086, Limón Persa, Papaya Maradol, Maíz H-516, Mango Manila, Piña MD2 Gold), cálculo de dosis de sopa líquida por arquitectura foliar y el esquema de simulaciones (4 Monodrón + 2 Enjambre) se visualizan dinámicamente en el portal web:

* 📊 **[Acceder al Dashboard Botánico en GitHub Pages](https://Weldimer.github.io/Prototipo-Dron-Agricola-Perlaco/)**: Gráficos Plotly interactivos de dosificación VRA de sopa líquida (L/ha), error RTK milimétrico, tiempos de vuelo y telemetría RF a 915 MHz.
* 📑 **[Reporte Ejecutivo de Misiones Diarias](docs/reportes/resumen_aprendizaje_diario.md)**: Tabla agronómica con variedad botánica, altura, ancho de copa, etapa fenológica y volumen total aplicado.

---

## 🛠️ Especificaciones Técnicas del Modelo Botánico

* **Dosificación VRA Adaptativa:** Cálculo exacto de volumen de mezcla (L/ha) en función de la variedad botánica, LAI, tipo de follaje y microclima local por API por coordenadas Lat/Lon.
* **Navegación Milimétrica:** Doble ZED-F9P RTK Moving Baseline con error RMS de 8 mm a 12 mm en trayectoria de aspersión.
* **Prioridad Operativa Monodrón:** Cobertura individual optimizada de 1 solo Dron para la mayoría de las parcelas regionales de Úrsulo Galván, manteniendo capacidad de Enjambre (3 UAVs) para predios de mayor extensión.

---

## 📚 Índice Documental Organizado (`/docs/reportes/`)

* 📊 [Resumen Ejecutivo de Aprendizaje Diario](docs/reportes/resumen_aprendizaje_diario.md)
* 🌾 [Aprendizaje y Justificación de Simulaciones Diarias](docs/reportes/aprendizaje_simulaciones_diarias_parcelas.md)
* 📦 [Lista Oficial de Materiales (BOM)](docs/reportes/bom_lista_materiales_oficial.md)
* 🛡️ [Reporte Técnico Moving Baseline y Pre-Arm](docs/reportes/reporte_prearm_y_moving_baseline.md)
* 🌪️ [Control VRA Adaptativo y Filtro Notch BDShot](docs/reportes/sistema_vra_adaptativo_clima_y_notch.md)

---
**ELECTRÓNICA PERLACO / PERLACOLABS** - *Úrsulo Galván, Veracruz, México*

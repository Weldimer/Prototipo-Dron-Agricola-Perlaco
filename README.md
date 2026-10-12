# ELECTRÓNICA PERLACO - STR-002 H3 v3.0

**Plataforma Aérea Agrícola (MTOW 29.0 kg) - Octocóptero Coaxial X8 & MAVLink Swarm**  
**Expediente Digital de Ingeniería, Coordinación Comparativa Monodron vs Enjambre y Partición Espacial**  
**Desarrollado por:** Angel Imer Lara Colorado / **PERLACOLABS** - *Úrsulo Galván & Paso de Ovejas, Veracruz, México*

[![CI Validation](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions/workflows/daily_learning_simulation.yml/badge.svg)](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions)
![ArduPilot](https://img.shields.io/badge/ArduPilot-4.5%2B-blue.svg)
![Swarm](https://img.shields.io/badge/Swarm-1%20vs%203%20UAVs-brightgreen.svg)
![MTOW](https://img.shields.io/badge/MTOW-29.0%20kg-green.svg)
![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)

> *"Hasta la criatura más humilde sirve a la tierra. Lástima que la civilización solo sepa servirse de ella para pisarla."*  
> - **PERLACOLABS**

---

## 🐝 Misiones de Comparación: Monodron (1 UAV) vs Enjambre (3 UAVs)

Toda la analítica de operación, división geométrica de parcelas y reducción del tiempo de vuelo se visualiza dinámicamente desde el portal web:

* 📊 **[Acceder al Dashboard Comparativo en GitHub Pages](https://Weldimer.github.io/Prototipo-Dron-Agricola-Perlaco/)**: Gráficos Plotly interactivos de tiempos de vuelo (Monodron vs Swarm), porcentajes de ahorro temporal y matrices de penetración foliar.
* 📑 **[Reporte Ejecutivo de Misiones Diarias](docs/reportes/resumen_aprendizaje_diario.md)**: Tabla comparativa de misiones con número exacto de aeronaves asignadas (1 UAV vs 3 UAVs) y redundancia MAVLink.

---

## 🛠️ Especificaciones Técnicas del Enjambre

* **Nodos de Vuelo (UAVs):** Configuración seleccionable entre 1 Unidad Individual (Monodron) y 3 Octocópteros Coaxiales X8 (`SYSID 1`, `SYSID 2`, `SYSID 3`).
* **Partición Espacial:** Algoritmo de sectorización paralelo Boustrophedon con margen de tolerancia lateral (15.0 m) para evitar colisiones.
* **Aviónica y Navegación:** Doble GNSS ZED-F9P RTK Moving Baseline por aeronave (rumbo relativo de alta precisión e inmunidad a interferencia magnética).
* **Ganancia Operativa:** Reducción de tiempo de misión superior al **60%** en parcelas de gran extensión (>10 ha) mediante operación colaborativa de 3 unidades.

---

## 📚 Índice Documental Organizado (`/docs/reportes/`)

* 📊 [Resumen Ejecutivo de Aprendizaje Diario](docs/reportes/resumen_aprendizaje_diario.md)
* 🌾 [Aprendizaje y Justificación de Simulaciones Diarias](docs/reportes/aprendizaje_simulaciones_diarias_parcelas.md)
* 📦 [Lista Oficial de Materiales (BOM)](docs/reportes/bom_lista_materiales_oficial.md)
* 🛡️ [Reporte Técnico Moving Baseline y Pre-Arm](docs/reportes/reporte_prearm_y_moving_baseline.md)
* 🌪️ [Control VRA Adaptativo y Filtro Notch BDShot](docs/reportes/sistema_vra_adaptativo_clima_y_notch.md)

---
**ELECTRÓNICA PERLACO / PERLACOLABS** - *Innovación y soberanía tecnológica para el campo mexicano.*

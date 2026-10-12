# ELECTRÓNICA PERLACO - STR-002 H3 v3.0

**Plataforma Aérea Agrícola Multi-UAV (MTOW 29.0 kg por unidad) - Octocóptero Coaxial X8 & MAVLink Swarm**  
**Expediente Digital de Ingeniería, Coordinación de Enjambres y Partición Espacial Boustrophedon**  
**Desarrollado por:** Angel Imer Lara Colorado / **PERLACOLABS** - *Úrsulo Galván & Paso de Ovejas, Veracruz, México*

[![CI Validation](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions/workflows/daily_learning_simulation.yml/badge.svg)](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions)
![ArduPilot](https://img.shields.io/badge/ArduPilot-4.5%2B-blue.svg)
![Swarm](https://img.shields.io/badge/Swarm-MAVLink%20SYSID-brightgreen.svg)
![MTOW](https://img.shields.io/badge/MTOW-29.0%20kg-green.svg)
![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)

> *"Hasta la criatura más humilde sirve a la tierra. Lástima que la civilización solo sepa servirse de ella para pisarla."*  
> - **PERLACOLABS**

---

## 🐝 Arquitectura de Drones en Enjambre (Multi-UAV Coordination)

Toda la analítica de operación en enjambre, división geométrica de parcelas y reducción del tiempo operativo se visualizan dinámicamente desde el portal web:

* 📊 **[Acceder al Dashboard de Enjambres en GitHub Pages](https://Weldimer.github.io/Prototipo-Dron-Agricola-Perlaco/)**: Gráficos Plotly comparativos de tiempos de vuelo (Monodron vs Swarm), porcentajes de ahorro temporal y matrices de penetración foliar.
* 📑 **[Reporte Ejecutivo de Misiones y Cobertura Multi-UAV](docs/reportes/resumen_aprendizaje_diario.md)**: Tabla de control de enjambres con asignación de pasadas por unidad y redundancia MAVLink.

---

## 🛠️ Especificaciones Técnicas del Enjambre

* **Nodos de Vuelo (UAVs):** Formación estándar de 3 Octocópteros Coaxiales X8 (Dron Alpha `SYSID 1`, Dron Beta `SYSID 2`, Dron Gamma `SYSID 3`).
* **Partición Espacial:** Algoritmo de sectorización paralelo Boustrophedon con margen de tolerancia lateral (15.0 m) para evitar colisiones.
* **Aviónica y Navegación:** Doble GNSS ZED-F9P RTK Moving Baseline por aeronave (rumbo relativo de alta precisión e inmunidad a interferencia magnética).
* **Ganancia Operativa:** Reducción de tiempo de misión superior al **60%** en parcelas de gran extensión (>10 ha).

---

## 📚 Índice Documental Organizado (`/docs/reportes/`)

* 📊 [Resumen Ejecutivo de Aprendizaje Diario](docs/reportes/resumen_aprendizaje_diario.md)
* 🌾 [Aprendizaje y Justificación de Simulaciones Diarias](docs/reportes/aprendizaje_simulaciones_diarias_parcelas.md)
* 📦 [Lista Oficial de Materiales (BOM)](docs/reportes/bom_lista_materiales_oficial.md)
* 🛡️ [Reporte Técnico Moving Baseline y Pre-Arm](docs/reportes/reporte_prearm_y_moving_baseline.md)
* 🌪️ [Control VRA Adaptativo y Filtro Notch BDShot](docs/reportes/sistema_vra_adaptativo_clima_y_notch.md)

---
**ELECTRÓNICA PERLACO / PERLACOLABS** - *Innovación y soberanía tecnológica para el campo mexicano.*

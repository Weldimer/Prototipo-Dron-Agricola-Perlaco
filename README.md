# ELECTRÓNICA PERLACO - STR-002 H3 v3.0

**Plataforma Aérea Agrícola (MTOW 29.0 kg) - Octocóptero Coaxial X8 & MAVLink Swarm Off-Grid**  
**Expediente Digital de Ingeniería, Telemetría RF 915 MHz, Enjambres y Partición Espacial Boustrophedon**  
**Desarrollado por:** Angel Imer Lara Colorado / **PERLACOLABS** - *Úrsulo Galván, Veracruz, México*

[![CI Validation](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions/workflows/daily_learning_simulation.yml/badge.svg)](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions)
![ArduPilot](https://img.shields.io/badge/ArduPilot-4.5%2B-blue.svg)
![RF Link](https://img.shields.io/badge/RF%20Link-915MHz%20Mesh-orange.svg)
![Swarm](https://img.shields.io/badge/Swarm-2x%20Mono%20%2B%201x%20Enjambre-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)

> *"Hasta la criatura más humilde sirve a la tierra. Lástima que la civilización solo sepa servirse de ella para pisarla."*  
> - **PERLACOLABS**

---

## 📡 Arquitectura de Enlace RF Off-Grid y Plataforma de Aprendizaje

Toda la analítica de operación en campo, simulación de calidad de señal en 915 MHz (RSSI y SNR) y reducción del tiempo de vuelo se visualiza dinámicamente en el portal web:

* 📊 **[Acceder al Dashboard Off-Grid en GitHub Pages](https://Weldimer.github.io/Prototipo-Dron-Agricola-Perlaco/)**: Gráficos Plotly interactivos de potencia de señal RF, relación señal-ruido, tiempos de vuelo (Monodron vs Swarm) y atenuación foliar.
* 📑 **[Reporte Ejecutivo de Misiones Diarias](docs/reportes/resumen_aprendizaje_diario.md)**: Tabla comparativa con misiones de 1 Dron y Enjambres de 3 Drones.

---

## 🛠️ Especificaciones Técnicas de Conexión Off-Grid

* **Enlace Primario (GCS ↔ UAV):** Radiofrecuencia pura en 915 MHz (RFD900x a 1W) con diversidad de antena y alcance >40 km sin red celular.
* **Coordinación en Enjambre (UAV ↔ UAV):** Red MAVLink Mesh asíncrona local entre 3 aeronaves (`SYSID 1, 2, 3`) para mantener márgenes de separación de 15.0 m.
* **Corrección RTK Local:** Base GNSS RTK en trípode con inyección de mensajes RTCM3 por radiofrecuencia (sin conexión internet/NTRIP).

---

## 📚 Índice Documental Organizado (`/docs/reportes/`)

* 📊 [Resumen Ejecutivo de Aprendizaje Diario](docs/reportes/resumen_aprendizaje_diario.md)
* 🌾 [Aprendizaje y Justificación de Simulaciones Diarias](docs/reportes/aprendizaje_simulaciones_diarias_parcelas.md)
* 📦 [Lista Oficial de Materiales (BOM)](docs/reportes/bom_lista_materiales_oficial.md)
* 🛡️ [Reporte Técnico Moving Baseline y Pre-Arm](docs/reportes/reporte_prearm_y_moving_baseline.md)
* 🌪️ [Control VRA Adaptativo y Filtro Notch BDShot](docs/reportes/sistema_vra_adaptativo_clima_y_notch.md)

---
**ELECTRÓNICA PERLACO / PERLACOLABS** - *Úrsulo Galván, Veracruz, México*

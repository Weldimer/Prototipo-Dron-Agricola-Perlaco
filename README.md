# ELECTRÓNICA PERLACO - STR-002 H3 v3.0

**Plataforma Aérea Agrícola (MTOW 29.0 kg) - Octocóptero Coaxial X8 & MAVLink Swarm Off-Grid**  
**Expediente Digital de Ingeniería, Precisión RTK Milimétrica (8-12 mm), Telemetría RF 915 MHz y Operación Monodrón Prioritaria**  
**Desarrollado por:** Angel Imer Lara Colorado / **PERLACOLABS** - *Úrsulo Galván, Veracruz, México*

[![CI Validation](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions/workflows/daily_learning_simulation.yml/badge.svg)](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions)
![ArduPilot](https://img.shields.io/badge/ArduPilot-4.5%2B-blue.svg)
![RTK Precision](https://img.shields.io/badge/RTK%20Precision-8--12%20mm-purple.svg)
![Swarm](https://img.shields.io/badge/Misiones-4x%20Mono%20%2B%202x%20Enjambre-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)

> *"Hasta la criatura más humilde sirve a la tierra. Lástima que la civilización solo sepa servirse de ella para pisarla."*  
> - **PERLACOLABS**

---

## 📡 Precisión Milimétrica y Plataforma de Aprendizaje Diario

Toda la analítica de operación en campo, georreferenciación de parcelas (Latitud, Longitud, Área en m²), precisión RTK de ±8 mm a 12 mm y el esquema de simulaciones (4 Monodrón + 2 Enjambre) se visualizan dinámicamente en el portal web:

* 📊 **[Acceder al Dashboard Geodésico en GitHub Pages](https://Weldimer.github.io/Prototipo-Dron-Agricola-Perlaco/)**: Gráficos Plotly interactivos de área trabajada en m², error RTK milimétrico, tiempos de vuelo y telemetría RF a 915 MHz.
* 📑 **[Reporte Ejecutivo de Misiones Diarias](docs/reportes/resumen_aprendizaje_diario.md)**: Tabla georreferenciada con coordenadas exactas, superficie total en hectáreas y metros cuadrados, y configuración de vuelo.

---

## 🛠️ Especificaciones Técnicas de Conexión Off-Grid y RTK

* **Navegación Milimétrica:** Doble ZED-F9P RTK Moving Baseline con error RMS de 8 mm a 12 mm en trayectoria de aspersión.
* **Enlace Primario Off-Grid:** Radiofrecuencia pura en 915 MHz (RFD900x a 1W) con alcance >40 km sin red celular ni internet.
* **Prioridad Operativa Monodrón:** Cobertura individual optimizada de 1 solo Dron para la mayoría de las parcelas regionales, manteniendo capacidad de Enjambre (3 UAVs) para predios de gran escala.

---

## 📚 Índice Documental Organizado (`/docs/reportes/`)

* 📊 [Resumen Ejecutivo de Aprendizaje Diario](docs/reportes/resumen_aprendizaje_diario.md)
* 🌾 [Aprendizaje y Justificación de Simulaciones Diarias](docs/reportes/aprendizaje_simulaciones_diarias_parcelas.md)
* 📦 [Lista Oficial de Materiales (BOM)](docs/reportes/bom_lista_materiales_oficial.md)
* 🛡️ [Reporte Técnico Moving Baseline y Pre-Arm](docs/reportes/reporte_prearm_y_moving_baseline.md)
* 🌪️ [Control VRA Adaptativo y Filtro Notch BDShot](docs/reportes/sistema_vra_adaptativo_clima_y_notch.md)

---
**ELECTRÓNICA PERLACO / PERLACOLABS** - *Úrsulo Galván, Veracruz, México*

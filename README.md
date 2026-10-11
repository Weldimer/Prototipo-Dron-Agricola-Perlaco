# ELECTRÓNICA PERLACO — STR-002 H3 v3.0

**Dron Agrícola Octocóptero VRA con Navegación Centimétrica RTK Dual y Control Hidráulico Anti-Goteo Distribuido**

![Licencia](https://img.shields.io/badge/License-CERN--OHL--W--v2-blue.svg)
![Firmware](https://img.shields.io/badge/ArduPilot-Copter_4.2%2B-orange.svg)
![Status](https://img.shields.io/badge/Status-Manufacturable_&_Validated-brightgreen.svg)

---



## 📋 Descripción General del Proyecto
El **STR-002 H3 v3.0** es un vehículo aéreo no tripulado agrícola de categoría pesada (MTOW ≈ 28.5 - 29.5 kg) diseñado para la aplicación de tasa variable (VRA) de agroquímicos en cultivos de alta densidad en Úrsulo Galván, Veracruz.

---

## 🛠️ Especificaciones Técnicas Principales
* **MTOW:** 28.5 kg - 29.5 kg
* **Carga Útil (Payload):** 10.0 L (Tanque HDPE con rompeolas)
* **Chasis:** Fibra de Carbono 3K (3.0 mm) + Abrazaderas H3 7075-T6 ($Y = \pm 26.0\text{ mm}$)
* **Alimentación:** Bus 12S LiPo (50.4V pico) + QS8-S Anti-Spark
* **Motopropulsión:** 8x T-Motor P80 III KV120 + Hélices plegables 30x10.5"
* **Aviónica:** Cube Orange+ (STM32H7) con triple IMU a 60 °C
* **Navegación:** RTK Dual (*Moving Baseline*) u-Blox ZED-F9P (Rumbo sin brújula magnética)
* **Seguimiento de Terreno:** Radar FMCW mmWave 77 GHz (0.5 m - 10.0 m AGL)
* **Hidráulica:** 4x Electroválvulas NC 24V distribuidas en puntas (<35 ms) + Caudalímetro YF-S201 (450 p/L)

---

## 📁 Archivos de Ingeniería Incluidos
* `/cad`: Plano DXF de chasis central CFRP 3.0 mm.
* `/firmware`: Script Lua v2.2 (`vra_tank_failsafe.lua`) para dosificación VRA y Failsafe.
* `/mission`: Archivo de misión agrícola QGC WPL 110 (`mision_agricola_str002_h3.waypoints`).
* `/simulation`: Script de simulación hidráulica y respuesta de caudal en Python.
* `/docs`: Memoria técnica de ingeniería y reivindicaciones de patente.
* `/assets`: Galería de fotografías reales y componentes mecatrónicos.

---

## 👤 Autor e Inventor Principal
**Angel Imer Lara Colorado**  
*ELECTRÓNICA PERLACO* — Úrsulo Galván, Veracruz, México.

---

## 📜 Licencia
Distribuido bajo la licencia **CERN Open Hardware Licence Version 2 - Weakly Reciprocal (CERN-OHL-W v2)** y **GNU General Public License v3.0 (GPLv3)**.

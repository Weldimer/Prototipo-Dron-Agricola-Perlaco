# ELECTRÓNICA PERLACO — STR-002 H3 v3.0

**Dron Agrícola Octocóptero VRA con Navegación Centimétrica RTK Dual y Control Hidráulico Anti-Goteo Distribuido**

![Licencia](https://img.shields.io/badge/License-CERN--OHL--W--v2-blue.svg)
![Firmware](https://img.shields.io/badge/ArduPilot-Copter_4.2%2B-orange.svg)
![Status](https://img.shields.io/badge/Status-Manufacturable_&_Validated-brightgreen.svg)

---
### 5. Reporte de Auditoría y Verificación de Errores de Sistema
<div align="center">
  <img src="assets/diagnostico_errores_sistema.png" width="95%" alt="Diagnóstico de Errores y Estrés" />
</div>

---

## 📈 Resultados de Simulación Dinámica y Telemetría

### 1. Telemetría Misión de Campo Real (Sincronización VRA y Bus 12S LiPo)
<div align="center">
  <img src="assets/simulacion_telemetria_vuelo.png" width="95%" alt="Simulacion Telemetria Real" />
</div>

### 2. Atenuación Espectral por Filtro Notch Armónico ($45\text{ Hz}$ / $90\text{ Hz}$)
<div align="center">
  <img src="assets/simulacion_filtro_notch.png" width="95%" alt="Filtro Notch FFT" />
</div>

### 3. Variación Dinámica del Centro de Gravedad ($Z_{CG}$) e Inercia ($I_{xx}$)
<div align="center">
  <img src="assets/simulacion_cg_inercia.png" width="95%" alt="Desplazamiento CG e Inercia" />
</div>

---

## 🛠️ Especificaciones Técnicas Principales
* **MTOW:** 28.5 kg - 29.5 kg
* **Carga Útil (Payload):** 10.0 L (Tanque HDPE con rompeolas)
* **Chasis:** Fibra de Carbono 3K (3.0 mm) + Abrazaderas H3 7075-T6
* **Alimentación:** Bus 12S LiPo (50.4V pico) + QS8-S Anti-Spark
* **Motopropulsión:** 8x T-Motor P80 III KV120 + Hélices plegables 30x10.5"
* **Aviónica:** Cube Orange+ (STM32H7) con triple IMU a 60 °C
* **Navegación:** RTK Dual (*Moving Baseline*) u-Blox ZED-F9P
* **Hidráulica:** 4x Electroválvulas NC 24V distribuidas en puntas (<35 ms) + Caudalímetro YF-S201 (450 p/L)

---

## 👤 Autor e Inventor Principal
**Angel Imer Lara Colorado**  
*ELECTRÓNICA PERLACO* — Úrsulo Galván, Veracruz, México.

# MATRIZ DE APRENDIZAJE Y SÍNTESIS DE REPOSITORIOS OPEN-SOURCE — STR-002 H3 v3.0
**PERLACOLABS — ELECTRÓNICA PERLACO**  
**Autor e Inventor Principal:** Angel Imer Lara Colorado — *Úrsulo Galván, Veracruz, México*

---

## 📚 1. Repositorios de Referencia e Integración Tecnológica

El diseño del expediente técnico y firmware del octocóptero **STR-002 H3 v3.0** integra lecciones de arquitectura extraídas de los principales repositorios abiertos de la industria aeroespacial y de robótica:

### A. `ArduPilot/ardupilot` (Librerías `AP_Scripting` y `AP_Peripheral`)
* **Aporte Principal:** Arquitectura de ejecución Lua en lazo cerrado dentro del sistema operativo ChibiOS RTOS.
* **Aplicación en STR-002 H3:** Implementación de scripts Lua deterministas para control hidráulico VRA (`vra_tank_failsafe.lua`), auditoría de salud Pre-Arm (`prearm_health_audit.lua`), lectura BDShot de los 8 ESCs T-Motor Alpha 80A HV y sintetizador RTTTL de audio (`pilot_audio_beacon.lua`).

### B. `mavlink/pymavlink` & `ArduPilot/mavlink` (Protocolo MAVLink v2)
* **Aporte Principal:** Empaquetado binario ligero con compresión de encabezado y verificación CRC-EXTRA.
* **Aplicación en STR-002 H3:** Inyección de mensajes MAVLink `NAMED_VALUE_FLOAT` e `STATUSTEXT` para enviar el nivel de tanque HDPE ($10.0\text{ L}$), tasa de dosis L/ha del caudalímetro YF-S201 y estado de alerta de la baliza acústica a QGroundControl.

### C. `PX4/Battery-Management-System` & `ArduPilot/AP_BattMonitor`
* **Aporte Principal:** Modelado electroquímico LiPo $12\text{S}$ con estimación de Estado de Carga (SOC) y Estado de Salud (SOH).
* **Aplicación en STR-002 H3:** Algoritmo de compensación de caída de tensión por carga (*voltage sag*) considerando la resistencia interna ($R_i = 24.0\text{ m}\Omega$), garantizando lecturas precisas durante picos de corriente de $320\text{ A}$ frente a ráfagas de viento de los 'Nortes' ($>127\text{ km/h}$).

### D. `DroneCAN/uavcan_vendor_specific` (Bus CAN Robusto)
* **Aporte Principal:** Protocolo de comunicación diferencial tolerante a ruido electromagnético severo (EMI).
* **Aplicación en STR-002 H3:** Inmunidad en la línea de comando para los 8 ESCs Alpha 80A y nodos de sensor de presión diferencial de fluido, eliminando interferencias generadas por las líneas de potencia de alta corriente.

---

## ⚙️ 2. Resumen de Transferencia Tecnológica al Repositorio Oficial

| Repositorio Origen | Módulo Integrado en STR-002 H3 | Archivo en Repositorio Local |
| :--- | :--- | :--- |
| `ArduPilot/ardupilot` | Motor Lua Lazo Cerrado, Pre-Arm, Dual GNSS | `firmware/prearm_health_audit.lua`, `firmware/moving_baseline_dual_gnss.param` |
| `mavlink/pymavlink` | Logs MAVLink CSV & Telemetría VRA | `simulation/simulacion_mision_integral.py`, `simulation/log_telemetria_mision_real.csv` |
| `PX4/BMS` | Modelo Electroquímico $12\text{S}$ y Sag Compensation | `firmware/smart_battery_bms_12s.lua` |
| `DroneCAN` | Red de Telemetría BDShot en 8 Motores X8 | `firmware/esc_rpm_health_monitor.lua` |

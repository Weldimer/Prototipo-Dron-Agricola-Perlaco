# LISTA DE MATERIALES OFICIAL (BOM) — STR-002 H3 v3.0
**PERLACOLABS — ELECTRÓNICA PERLACO**  
**Autor e Inventor Principal:** Angel Imer Lara Colorado — *Úrsulo Galván, Veracruz, México*

---

## 📋 1. Especificación Detallada de Componentes, Datasheets y Justificación

| Subsistema | Componente | Fabricante / Modelo | Cant. | Datasheet / Enlace | Justificación Técnica de Ingeniería |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **Aviónica** | Autopiloto Triple Redundancia | CubePilot Cube Orange+ | 1 | [Datasheet](https://docs.cubepilot.org/user-guides/autopilot/the-cube-user-manual) | Procesador STM32H753, IMUs aisladas térmicamente y ChibiOS RTOS para scripts Lua en lazo cerrado. |
| **Navegación** | Receptor GNSS RTK Multibanda | u-blox ZED-F9P | 2 | [Datasheet](https://www.u-blox.com/en/product/zed-f9p-module) | Rumbo por fase de portadora Moving Baseline (L1/L2) con resolución $0.47^\circ$. Inmunidad total a EMI (>300A). |
| **Propulsión** | Motor Brushless Agrícola | T-Motor P80 III KV120 | 8 | [Datasheet](https://store.tmotor.com/goods.php?id=832) | $73.6\text{ kg}$ de empuje total ($T/W = 2.53:1$). Resistencia aerodinámica a rachas de 'Nortes' (>127 km/h). |
| **Propulsión** | ESC Inteligente HV FOC | T-Motor Alpha 80A HV | 8 | [Datasheet](https://store.tmotor.com/goods.php?id=832) | Comunicación BDShot para telemetría de RPM e inyección en el filtro Notch dinámico (`-40 dB`). |
| **Propulsión** | Hélices Plegables Carbono | T-Motor $30\times 10.5''$ | 8 | [Datasheet](https://store.tmotor.com/goods.php?id=832) | Alta eficiencia aerodinámica en configuración Coaxial X8. |
| **Audio / Alerta**| Megáfono Industrial IP67 | PERLACO Audio 24V | 1 | [Especificación](docs/sistema_audio_y_alertas.md) | Disuasión activa de avifauna a $110\text{ dB SPL}$ (2.8 kHz) impulsado por canal aux PWM/Relé. |
| **Audio / Alerta**| Sintetizador RTTTL Nativo | Zumbador Piezo Cube Orange+ | 1 | [Especificación](docs/sistema_audio_y_alertas.md) | Baliza acústica de localización en cañavérales ejecutando la Marcha Turca (*Turkish March*) a 78.5 dB. |
| **Hidráulica VRA**| Caudalímetro Efecto Hall | YF-S201 ($450\text{ imp/L}$) | 1 | [Datasheet](https://www.alldatasheet.com/view.jsp?Searchword=YF-S201) | Medición continua de tasa de dosis L/ha correlacionada con las APIs de Open-Meteo y NASA POWER. |
| **Hidráulica VRA**| Estanque Principal HDPE | PERLACOLABS $10.0\text{ L}$ | 1 | [Plano CAD](cad/estanque_hdpe_10l.step) | Diseño rompeolas interno para amortiguar el oleaje (*sloshing*) durante maniobras contraviento. |
| **Hidráulica VRA**| Sensor Presión de Fluido | CAN/I2C $0-10\text{ bar}$ | 1 | Especificación Técnica | Detección de boquillas obstruidas o cavitación en la bomba en tiempo real. |
| **Energía** | Batería LiPo Agrícola | Tattu $12\text{S}$ 22000mAh | 2 | [Especificación](https://www.genstattu.com) | Suministro de alta corriente ($300\text{ A}$ picos) con monitoreo de $R_i = 24\text{ m}\Omega$ via Lua BMS. |

---

## 📐 2. Resumen Estructural y Balance de Peso

* **Peso Vacío (Sin Carga Liquida):** $18.5 - 19.5\text{ kg}$
* **Carga Útil Nomilal (Agroquímico):** $10.0\text{ kg}$ ($10.0\text{ L}$)
* **Peso Máximo al Despegue ($MTOW$):** $28.5 - 29.5\text{ kg}$
* **Relación Empuje / Peso ($T/W$):** $2.53:1$ ($73.6\text{ kg}$ de empuje máximo disponible)

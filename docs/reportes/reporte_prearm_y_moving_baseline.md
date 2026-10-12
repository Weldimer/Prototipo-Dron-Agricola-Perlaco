# REPORTE TÉCNICO: INMUNIDAD ELECTROMAGNÉTICA (EMI), DUAL GNSS Y AUDITORÍA PRE-ARM — STR-002 H3 v3.0
**PERLACOLABS — ELECTRÓNICA PERLACO**  
**Autor e Inventor Principal:** Angel Imer Lara Colorado — *Úrsulo Galván, Veracruz, México*

---

## 🛡️ 1. Justificación de la Eliminación de Magnetómetros (Compass-less Yaw)

En drones agrícolas de alta capacidad ($MTOW \approx 29.0\text{ kg}$), los picos de corriente continua de la línea de alta potencia $12\text{S}$ ($> 300\text{ A}$ a pleno empuje de los 8 motores T-Motor P80 III) generan campos magnéticos inducidos según la Ley de Ampère:

$$B_{\text{inducido}} = \frac{\mu_0 I}{2 \pi r}$$

Este campo parásito causa desviaciones dinámicas en el magnetómetro de hasta $44.8^\circ$ de rumbo, corrompiendo las estimaciones del filtro EKF3 y provocando el fenómeno de *toilet-bowling* o giros incontrolados.

---

## 🛰️ 2. Arquitectura Doble ZED-F9P Moving Baseline RTK

Se integran dos receptores GNSS u-blox ZED-F9P montados sobre la estructura de la aeronave con una línea base inter-antena de $L = 0.60\text{ m}$ ($60\text{ cm}$):

* **Cálculo del Vector de Rumbo:** La diferencia de fase en las portadoras L1/L2 entre la antena Base (+30 cm X) y Rover (-30 cm X) determina el ángulo de rumbo ($Yaw$) exacto con una resolución angular de:

$$\Delta \theta = \arctan\left(\frac{\sigma_{\text{fase}}}{L}\right) = \arctan\left(\frac{0.005\text{ m}}{0.60\text{ m}}\right) \approx 0.47^\circ$$

* **Inmunidad Magnética $100\%$:** La navegación no depende del campo magnético terrestre, permitiendo desactivar totalmente las brújulas (`COMPASS_USE = 0`, `EK3_SRC1_YAW = 2`).

---

## 📊 3. Resultados de la Auditoría Pre-Armado Lua

El script `prearm_health_audit.lua` evalúa tres condicionantes antes de autorizar el despegue:

1. **Tensión de Celda $12\text{S} \ge 3.75\text{ V}$:** Garantiza capacidad electroquímica para completar la misión.
2. **Modo RTK Fixed (GPS Status 6):** Confirma la convergencia de fase de la portadora Moving Baseline.
3. **Telemetría BDShot en 8 ESCs:** Verifica la comunicación bidireccional serial con cada ESC T-Motor Alpha 80A HV.

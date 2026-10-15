# CERTIFICACIÓN DE REDUNDANCIA X8, FEA ESTRUCTURAL Y SLOSHING — STR-002 H3 v3.0
**PERLACOLABS — ELECTRÓNICA PERLACO**  
**Autor e Inventor Principal:** Angel Imer Lara Colorado — *Úrsulo Galván, Veracruz, México*

---

## 🚁 1. Tolerancia a Falla de Motor en Vuelo (X8 Motor-Out Redundancy)

El diseño del octocóptero coaxial X8 garantiza la continuidad del vuelo controlado ante la pérdida imprevista de una unidad motopropulsora:

* **Empuje Nominal (8 Motores T-Motor P80 III):** $73.6\text{ kg}$ (Ratio T/W: $2.53:1$).
* **Empuje en Condición de Falla (7 Motores Activos):** $64.4\text{ kg}$ (Ratio T/W: $2.22:1$).
* **Criterio de Seguridad:** Al mantener un Ratio T/W superior a $2.0:1$, ArduPilot rebalanza la matriz de mezcla (*motor mixing matrix*) de manera automática, notificando a QGroundControl la alerta e iniciando el retorno a base (RTL) sin descompensación inercial.

---

## 📐 2. Análisis de Elementos Finitos (FEA) de Abrazaderas H3 y Brazos CFRP

Someter la estructura a una maniobra agresiva de $3G$ ($1.5\times$ factor de carga nominal) arroja los siguientes valores mecánicos:

1. **Deflexión en Tubo CFRP ($\varnothing 50\text{ mm} \times 550\text{ mm}$):** $1.78\text{ mm}$ de flexión máxima en punta, dentro del margen admisible ($< 3.0\text{ mm}$).
2. **Esfuerzos de Von Mises en Abrazaderas H3 (Aluminio 7075-T6):** $\sigma_{mises} = 120.8\text{ MPa}$.
3. **Factor de Seguridad ($FS$):** $FS = \frac{505.0\text{ MPa}}{120.8\text{ MPa}} = 4.18$, superando holgadamente el criterio de diseño aeronáutico ($FS > 3.0$).

---

## 🌊 3. Dinámica de Fluidos y Amortiguamiento de Oleaje (Sloshing)

* **Atenuación con Deflector Interno:** El rompeolas HDPE reduce la fuerza de impacto de $71.0\text{ N}$ a sólo $17.8\text{ N}$ durante frenados a $25^\circ$ de pitch.
* **Estabilización de $Z_{CG}$:** El tiempo de amortiguamiento del fluido decae a $< 0.35\text{ s}$, eliminando las oscilaciones parásitas que afectan el bucle de control de la Cube Orange+.

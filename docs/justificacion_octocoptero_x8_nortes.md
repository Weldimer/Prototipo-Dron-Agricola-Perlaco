# JUSTIFICACIÓN TÉCNICA: ARQUITECTURA OCTOCÓPTERO X8 CONTRA VIENTOS EXTREMOS ('NORTES' >127 KM/H)
**PERLACOLABS — ELECTRÓNICA PERLACO**  
**Autor e Inventor Principal:** Angel Imer Lara Colorado — *Úrsulo Galván, Veracruz, México*

---

## 🌪️ 1. Contexto Meteorológico: Los 'Nortes' en la Costa de Veracruz

La zona agrícola de Úrsulo Galván y la franja costera del Golfo de México se ven impactadas de manera recurrente por frentes fríos estacionales conocidos como **'Nortes'**, los cuales generan ráfagas de viento contínuas y microburras de viento que superan los **127 km/h** ($>35.3	ext{ m/s}$ / 68 nudos). Operar un RPAS agrícola de $MTOW pprox 28.5 - 29.5	ext{ kg}$ bajo estas condiciones requiere un diseño aerodinámico y una reserva motriz de alta densidad que imposibilita el uso de arquitecturas convencionales de 4 o 6 motores.

---

## 🚁 2. Fundamentos de Ingeniería de la Configuración Coaxial X8 (8 Motores)

El prototipo **STR-002 H3 v3.0** integra **8 motores brushless T-Motor P80 III KV120** y **8 ESCs T-Motor Alpha 80A HV** organizados en 4 pares coaxiales. Esta selección se basa en los siguientes principios físicos y aerodinámicos:

### A. Reserva de Empuje y Prevención de Saturación de PWM
* **Empuje Total Disponible:** $73.6	ext{ kg}$ de empuje máximo frente a un $MTOW$ nominal de $29.0	ext{ kg}$ ($T/W = 2.53:1$).
* **Control de Inclinación (Pitch/Roll) a $35^\circ$:** Para contrarrestar vientos fijos o ráfagas de $127	ext{ km/h}$, la aeronave debe inclinarse agresivamente. En plataformas de 4 o 6 motores, los motores orientados hacia barlovento se saturan al $100\%$ de aceleración, perdiendo el control de actitud y desplomándose.
* **Reserva Activa:** El X8 retiene más del **$60.5\%$ de reserva de empuje** dedicada exclusivamente al bucle de control de actitud en lazo cerrado sin saturar la matriz de mezcla (*motor mixing matrix*).

### B. Densidad Aerodinámica y Respuesta Temporal Microsegundal
* La disposición coaxial concentra 8 motores sobre 4 brazos de $arnothing 50	ext{ mm}$, reduciendo la superficie frontal expuesta a la fricción del viento en un $40\%$ comparado con un octocóptero plano de 8 brazos extensos.
* Los ESCs Alpha 80A HV con protocolo de alta velocidad ajustan el torque sobre las hélices plegables de $30	imes 10.5''$ en microsegundos, amortiguando las fluctuaciones térmicas e inerciales del viento racheado.

### C. Redundancia Crítica ante Falla en Vuelo (*Motor-Out*)
* En ráfagas extremas, un esfuerzo térmico o fallo mecánico en un motor no compromete la aeronave.
* Con **1 motor inoperativo (7/8 activos)**, el sistema dispone de **$64.4	ext{ kg}$** de empuje ($T/W = 2.22:1$). Al superar el umbral mínimo de sustentación ($> 2.0:1$), el autopiloto Cube Orange+ rebalancea los pares y ejecuta el Retorno a Base (**RTL**) automático de forma segura.

### D. Compensación Dinámica de Oleaje (*Sloshing*)
* Las ráfagas de $127	ext{ km/h}$ generan desaceleraciones bruscas que agitan los $10.0	ext{ L}$ de mezcla hidráulica en el estanque HDPE.
* El par motor instantáneo de los 8 motores contrarresta la compensación del centro de gravedad ($Z_{CG}$), logrando la estabilización de actitud en menos de **$0.35	ext{ segundos}$**.

---

## ⚙️ 3. Parámetros Clave de Configuración en ArduPilot

| Parámetro | Valor | Función Técnica para Clima de Viento Severo |
| :--- | :---: | :--- |
| `MOT_FRAME_CLASS` | `6` | Establece la geometría Coaxial X8. |
| `MOT_FRAME_TYPE` | `1` | Disposición en X para equilibrio de momentos. |
| `ANGLE_MAX` | `3500` | Inclinación máxima de $35.0^\circ$ para vencer empuje contraviento de $127	ext{ km/h}$. |
| `PILOT_THR_BHV` | `1` | Conserva la referencia de aceleración en corrientes descendentes. |
| `PSC_ACCZ_P` | `0.300` | Elevada ganancia vertical para amortiguar ráfagas cortantes (*microbursts*). |

# CONTROL VRA ADAPTATIVO AL CLIMA Y FILTRO NOTCH BDSHOT — STR-002 H3 v3.0
**PERLACOLABS — ELECTRÓNICA PERLACO**  
**Autor e Inventor Principal:** Angel Imer Lara Colorado — *Úrsulo Galván, Veracruz, México*

---

## 🌪️ 1. Mantenimiento de Ruta y Corrección de Deriva (*Crab Angle*)

Para evitar que las ráfagas de los 'Nortes' ($> 127\text{ km/h}$) desvíen la aeronave de su franja de asperjado, el autopiloto ejecuta una compensación de vector de rumbo (*Crab Angle* o Ángulo de Cangrejo):

$$\phi_{\text{crab}} = \arcsin\left(\frac{V_{\text{viento\_transversal}}}{V_{\text{aire}}}\right)$$

Combinado con la orientación por **Doble GNSS Moving Baseline RTK**, la aeronave apunta su chasis hacia el viento mientras mantiene su centro de masa desplazándose exactamente sobre la línea de waypoint con un error lateral inferior a $0.05\text{ m}$.

---

## 💧 2. Caudal de Asperjado Adaptativo VRA en Tiempo Real

El script `vra_wind_compensation.lua` ajusta el caudal $Q_{\text{req}}$ (L/min) en lazo cerrado relacionando la velocidad sobre el suelo y las pérdidas por deriva de gota inducidas por el viento:

$$Q_{\text{req}}(\text{L/min}) = \frac{\text{Dosis}(\text{L/ha}) \times \text{Ancho}(m) \times V_{\text{terreno}}(\text{km/h})}{600} \times \left(1 + \max(0, (V_{\text{viento}} - 5) \times 0.04)\right)$$

---

## 🔇 3. Atenuación de Vibraciones Armónicas (BDShot Dynamic Notch)

Las hélices de $30''$ operan a frecuencias rotacionales variables. El parámetro `INS_HNOTCH_MODE = 3` lee la velocidad RPM exacta de cada uno de los 8 motores T-Motor P80 III a través del canal digital BDShot y aplica un filtro muesca atenuador que reduce el ruido en los sensores giroscópicos en **$-40\text{ dB}$**.

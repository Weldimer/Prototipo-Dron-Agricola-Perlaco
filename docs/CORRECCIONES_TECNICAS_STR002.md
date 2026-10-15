# ELECTRÓNICA PERLACO — STR-002 H3 v3.0 (Registro Maestro de Ingeniería)

## Matriz de Correcciones Críticas y Auditoría Estructural

Este documento consolida la depuración técnica y el cierre de no conformidades del prototipo **STR-002 H3** (MTOW $\approx 29\text{ kg}$):

### 1. Correcciones Mecánicas y Estructurales (Chasis y Abrazadera H3)
* **Altura del Chasis (Envolvente Vertical):** Separación de placas fijada estrictamente a **$56.00\text{ mm}$** mediante pilares. Cuerpo de abrazadera $H3$ rebajado a **$54.00\text{ mm}$** (con $1.00\text{ mm}$ de holgura por cara para evitar compresión directa sobre el tubo de carbono de $\varnothing 50\text{ mm}$). Torretas de contacto plano (*bosses*) rectificadas a $56.00\text{ mm}$.
* **Ligamento Residual (P-01):** Reposicionamiento del barreno M5 para garantizar un ligamento mínimo $t_{\min} \ge 2.75\text{ mm}$ (evitando concentradores de tensión excesivos y riesgos de fatiga).
* **Momento Flector en Voladizo ($M_y$):** Incorporación formal del momento flector de raíz ($M_y = F_z \cdot L = 115.6\text{ N}\cdot\text{m}$ hasta $286.94\text{ N}\cdot\text{m}$ bajo cargas dinámicas de $3g$), generando un par de cortantes horizontales de **$2,312\text{ N}$** en las placas.
* **Modelo de Contacto y Aplastamiento (*Bearing*):** Suposición de fricción pura eliminada. Los pernos M5 trabajan bajo contacto directo de vástago y aplastamiento, limitando la carga admisible a los márgenes normativos de la placa de aluminio 6061-T6.
* **Estado del Gate:** Se mantiene el estricto estado **GATE-STR-002 ABIERTO**; prohibida la liberación para fabricación hasta completar las corridas FEA tridimensionales con malla convergente.

### 2. Correcciones Eléctricas y de Potencia
* **Bus de Propulsión 12S:** Migración formal del sistema de $14S$ a **$12S$ LiPo** ($44.4\text{ V}$ nominal / $50.4\text{ V}$ pico) para respetar el rango homologado del motor **T-Motor P80 III KV120**.
* **Partida de Masa Seca (SYS-002):** Actualización de la partida propulsora a **$\approx 4.300\text{ kg}$** para absorber con precisión el peso real de los motores ($647\text{ g}$ c/u) y hélices de carbono de $30''$.
* **Gestión Térmica y de Autonomía:** Cálculo de batería considerando reservas estrictas para retorno a casa (RTL), pérdidas por resistencia de cables ($I^2R$) y degradación térmica en clima tropical ($>34^\circ\text{C}$).

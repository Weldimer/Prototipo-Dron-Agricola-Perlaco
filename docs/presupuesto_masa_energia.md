# ⚖️ Presupuesto de Masa y Energía Trazable — STR-002 H3 v3.5

Este documento establece el balance formal de masas, energía y autonomía del prototipo **ELECTRÓNICA PERLACO STR-002 H3 v3.5**, separando los datos verificados por fabricante de los parámetros teóricos y las incógnitas pendientes de validación experimental.

---

## 1. Presupuesto de Masa (Objetivo MTOW: 29.0 kg)

| Componente / Subsistema | Masa Unitaria | Cantidad | Masa Total | Categoría de Evidencia | Fuente / Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Motores T-Motor P80 III** | $649	ext{ g}$ | $8$ | $5.19	ext{ kg}$ | 🧮 **Calculado** | Ficha técnica oficial del fabricante. |
| **ESC T-Motor Alpha 80A** | $110	ext{ g}$ | $8$ | $0.88	ext{ kg}$ | 🧮 **Calculado** | Ficha técnica oficial del fabricante. |
| **Chasis y Brazos de Carbono** | Variable | Set | $4.50	ext{ kg}$ | 📐 **Diseño CAD** | Estimación preliminar por volumen de fibra (Pendiente de validación física). |
| **Aviónica (Cube Orange+, GNSS RTK, Edge AI, PDB)** | Variable | Set | $1.20	ext{ kg}$ | 🧮 **Calculado** | Pesaje acumulado de componentes electrónicos y cableado de potencia. |
| **Sistema Hidráulico (Bombas, mangueras, manifold, boquillas)** | Variable | Set | $0.73	ext{ kg}$ | 🧮 **Calculado** | Suma de componentes hidráulicos seleccionados. |
| **Batería de Propulsión (18S)** | $6.50	ext{ kg}$ | $1$ | $6.50	ext{ kg}$ | 🟡 **Estimación** | Requerida para autonomía estimada de 10-12 min (Pendiente de selección de celdas). |
| **Carga Útil Líquida (Tanque + 10 L de Caldo)** | $10.00	ext{ kg}$ | $1$ | $10.00	ext{ kg}$ | 📐 **Diseño** | 10 litros de caldo agrícola ($10	ext{ kg}$) + estructura plástica del depósito. |
| **Masa Total Calculada al Despegue (MTOW)** | — | — | **$29.00	ext{ kg}$** | 🟡 **Cuadrado por Diseño** | **Coincide exactamente con el límite estructural proyectado.** |

---

## 2. Presupuesto de Energía y Autonomía (Modelo Teórico Inicial)

* **Voltaje Nominal del Sistema:** $18	ext{S}$ LiPo ($pprox 66.6	ext{ V}$ nominales, $pprox 75.6	ext{ V}$ a carga plena).
* **Consumo Estimado en Estacionario (Hover):** Con un peso total de $29	ext{ kg}$, asumiendo una eficiencia aerodinámica conservadora del arreglo coaxial X8, el consumo aproximado en vuelo estacionario se sitúa en torno a los **$3.2	ext{ kW} - 3.8	ext{ kW}$**.
* **Capacidad Energética de la Batería (Estimación):** Una batería de $18	ext{S}$ con una capacidad estimada de $16,000	ext{ mAh}$ a $22,000	ext{ mAh}$ almacena aproximadamente de $1.0	ext{ kWh}$ a $1.4	ext{ kWh}$ de energía útil.
* **Autonomía Proyectada:** 
  $$\text{Autonomía útil} \approx 8 \text{ a } 12 \text{ minutos}$`, considerando un factor de descarga segura del $80\%$ ($	ext{DoD}$) y un margen de reserva para el retorno a base (*RTL*).

---

## 3. Lista de Incertidumbres Críticas (Pendientes de Resolución)

1. **Eficiencia Coaxial Real ($\eta_{coax}$):** Las pérdidas aerodinámicas en el disco inferior del arreglo X8 deben verificarse en banco estático con dinamómetro para evitar sobrestimar el empuje real.
2. **Curva Térmica del PDB:** Demostrar por simulación o cálculo térmico que las pistas de cobre de 6 oz resisten los transitorios de corriente sin superar la temperatura de transición vítrea del laminado FR4.
3. **Consumo Dinámico de las Bombas Hidráulicas:** Integrar la corriente real de arranque y operación continua de las bombas en el balance eléctrico total de la batería de 18S.

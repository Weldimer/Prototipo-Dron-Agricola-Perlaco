# ⚡ Análisis Térmico y Eléctrico (Arquitectura 18S / 75.6V HV) - STR-002 H3

## 1. Balance de Potencias y Corriente
El sistema está alimentado por una configuración de baterías en serie **18S** (Voltaje nominal: $66.6 \text{ V}$, Voltaje máximo a plena carga: $75.6 \text{ V}$).

* **Potencia Nominal del Sistema (8 Motores P80 III + Carga):** $8,400 \text{ W}$
* **Corriente Nominal en Bus Principal ($I_{nom}$):**
  
$$I_{nom} = \frac{P}{V} = \frac{8,400 \text{ W}}{66.6 \text{ V}} \approx 126.12 \text{ A}$$

* **Corriente Pico Transitoria (Maniobras de Emergencia / Ráfagas):** $210.0 \text{ A}$ (Soportada por conectores QS8-S de alta capacidad).

---

## 2. Modelado de Caída de Voltaje y Efecto Joule
Utilizando cableado de cobre trenzado calibre **12 AWG** (Resistencia lineal aproximada de $5.21 \text{ m}\Omega / 100 \text{ m}$, longitud estimada del circuito de potencia $L = 1.2 \text{ m}$):

* **Resistencia Total del Cable ($R$):** $\approx 0.00625 \Omega$
* **Caída de Voltaje en Conducción ($V_{drop}$):**

$$V_{drop} = I_{nom} \cdot R = 126.12 \text{ A} \cdot 0.00625 \Omega = 0.788 \text{ V}$$

* **Disipación Térmica (Efecto Joule $P_j$):**

$$P_j = I_{nom}^2 \cdot R = (126.12 \text{ A})^2 \cdot 0.00625 \Omega \approx 99.39 \text{ W}$$

La disipación se distribuye eficientemente mediante placas disipadoras de aluminio y pasta térmica de alta conductividad (> 8.5 W/mK) en los módulos ESC y PDB, evitando superar el umbral crítico de temperatura de transición del aislamiento (nominal de 105 °C).

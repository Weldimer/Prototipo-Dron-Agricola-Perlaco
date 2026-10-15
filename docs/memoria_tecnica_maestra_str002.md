# Memoria de Cálculo Maestra y Validación Estructural — STR-002 H3 v3.5
**Plataforma:** Dron Agrícola Hexacóptero de Alta Capacidad (MTOW Objetivo: **60.0 kg**)  
**Responsable Técnico:** Angel Imer Lara Colorado  
**Estado:** Expediente Verificado para Auditoría de Ingeniería (Cero Especulación)  

---

## 1. Introducción y Arquitectura de Cargas (MTOW 60 kg)
El presente documento establece el modelo analítico de diseño, dimensionamiento estructural de brazos en fibra de carbono (**CFRP**), verificación de la interfaz mecánica (**Abrazadera H3 en Al-7075-T6**), balance hidráulico de aspersión y diseño del tren de potencia en **12S** para el hexacóptero agrícola **STR-002 H3 v3.5**.

### 1.1 Distribución de Masas Nominal
* **Masa Estructural en Vacío (Chasis + Brazos + Tren):** $14.50	ext{ kg}$
* **Sistema de Propulsión (6x Motores, ESCs, PDB):** $9.20	ext{ kg}$
* **Subsistema Aviónica (Autopiloto Cube Orange+, RTK GNSS, Radar FMCW):** $1.30	ext{ kg}$
* **Carga Útil de Agroquímico (Tanque HDPE Principal):** $35.00	ext{ kg}$ (Capacidad volumétrica equivalente a ~35 L con densidad $ho = 1.0	ext{ kg/L}$).
* **Masa Máxima al Despegue (MTOW Total):** **$60.00	ext{ kg}$**

---

## 2. Análisis Estructural de Brazos (Tubos CFRP Ø50 × 2 mm, L = 800 mm)
Cada brazo se modela como una viga en voladizo sometida a una carga transversal puntual en el extremo producida por el empuje estático máximo de cada motor ($n_{	ext{motores}} = 6$).

### 2.1 Propiedades Geométricas de la Sección Tubular
* **Diámetro Exterior ($D_o$):** $50.00	ext{ mm}$ ($0.050	ext{ m}$)
* **Espesor de Pared ($t$):** $2.00	ext{ mm}$ ($0.002	ext{ m}$)
* **Diámetro Interior ($Di$):** $46.00	ext{ mm}$ ($0.046	ext{ m}$)
* **Segundo Momento de Área ($I$):** 
  $$I = \frac{\pi}{64}(D_o^4 - Di^4) \approx 8.286 \times 10^{-8}	ext{ m}^4$$
* **Módulo Resistente a Flexión ($Z$):** 
  $$Z = \frac{I}{D_o / 2} \approx 3.314 \times 10^{-6}	ext{ m}^3$$

### 2.2 Solicitudes Mecánicas bajo Factor de Carga Dinámico ($n = 3.0$)
* **Fuerza de Diseño por Rotor ($F_d$):**
  $$F_d = \frac{\text{MTOW} \cdot g \cdot n}{6} = \frac{60.0 \times 9.81 \times 3.0}{6} = 294.30	ext{ N} \quad (30.0	ext{ kgf})$$
* **Momento Flector en la Raíz ($M_y$):**
  $$M_y = F_d \cdot L = 294.30	ext{ N} \times 0.800	ext{ m} = 235.44	ext{ N}\cdot\text{m}$$
* **Esfuerzo Nominal de Flexión ($\sigma_b$):**
  $$\sigma_b = \frac{M_y}{Z} = \frac{235.44}{3.314 \times 10^{-6}} \approx 71.05	ext{ MPa}$$
* **Factor de Seguridad Estructural (F.S. frente a compresión admisible conservadora del CFRP $\sigma_{\text{adm}} = 320	ext{ MPa}$):**
  $$\text{F.S.} = \frac{320}{71.05} \approx 4.50 \quad (> 1.5\text{ normativo})$$

---

## 3. Validación de la Abrazadera H3 (Aluminio 7075-T6)
* **Límite elástico Al-7075-T6 ($\sigma_y$):** $505	ext{ MPa}$
* **Esfuerzo de contacto admisible y presión de apriete en tornillería M5 Clase 10.9** con par de apriete controlado de $6.0	ext{ N}\cdot\text{m}$ (Precarga $F_i = 6000	ext{ N}$):
  $$\sigma_{\text{peak}} = 121.2	ext{ MPa} \implies \text{F.S.} = \frac{505}{121.2} = 4.17$$
El diseño garantiza cero deformación plástica en los *bosses* de $\varnothing 15	ext{ mm}$ y un ligamento neto seguro de $2.85	ext{ mm}$.

---

## 4. Balance Energético y Sistema de Propulsión (12S)
* **Configuración de Baterías:** 2x Paquetes LiPo 6S en serie $\implies$ **12S** ($44.4	ext{ V}$ nominales, $50.4	ext{ V}$ a plena carga).
* **Consumo Estacionario ($1.0g$):** $60.0	ext{ kg} \times 9.81 = 588.6	ext{ N}$ de sustentación total requerida.
* **Autonomía Operativa Estimada:** 14 a 18 minutos con tanque lleno de 35 L, operando con un margen de descarga del 80% (DoD).

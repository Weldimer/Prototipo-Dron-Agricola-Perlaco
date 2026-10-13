# 🛠️ Lista Oficial de Materiales (BOM) Integral y Definitiva — STR-002 H3 v3.5

**Plataforma Aérea Agrícola Autónoma (MTOW 60.0 kg) - Octóptero Coaxial X8**  
*Desarrollado por: Angel Imer Lara Colorado / PERLACOLABS — Úrsulo Galván, Veracruz, México*

Este documento constituye el inventario técnico global de todos los componentes de hardware, software, aviónica, estructura mecánica, cableado, elementos hidráulicos, atomizadores centrífugos, antenas y sistemas de aspersión que conforman el prototipo agrícola.

---

## 🏗️ 1. Estructura Mecánica y Elementos de Fijación

| Ít. | Componente / Pieza | Material / Especificación Técnica | Cantidad | Función Principal |
| :--- | :--- | :--- | :--- | :--- |
| **1.1** | Tubos de Brazos Principales | Fibra de carbono bidireccional ($\varnothing 50\text{ mm} \times 2.0\text{ mm} \times 650\text{ mm}$) | 8 pzas | Soporta flexión de motores coaxiales y alberga cableado de potencia. |
| **1.2** | Tubos del Tren y Refuerzo | Fibra de carbono pultruida ($\varnothing 25\text{ mm} \times 400\text{ mm}$) | 4 pzas | Rigidez estructural del tren de aterrizaje y soporte de tanque. |
| **1.3** | Placas del Chasis Central | Matriz epoxídica de carbono (Espesor $3.0\text{ mm}$, alvéolos P-01) | 2 pzas | Distribución de esfuerzos y plataforma de montaje de aviónica. |
| **1.4** | Abrazaderas de Nodos H3 | Aluminio Aeronáutico 7075-T6 mecanizado CNC ($\pm0.02\text{ mm}$) | 16 pzas | Acoplamiento rígido entre brazos y placas centrales. |
| **1.5** | Pernos Estructurales M5 | Acero Inoxidable A4-80 (Grado Marina, M5 x 35 mm) | 32 pzas | Sujeción principal en nodos H3 y montajes de motores. |
| **1.6** | Tornillería de Chasis M4 | Acero Inoxidable A4-80 (M4 x 16 mm / M4 x 20 mm) | 64 pzas | Montaje de PDB, sensores y placas secundarias. |
| **1.7** | Tuercas Autofrenantes | Acero Inoxidable con inserto de nylon (DIN 985, M4 y M5) | 96 pzas | Bloqueo mecánico antivibración por armónicos de motores. |
| **1.8** | Rondanas Planas | Acero Inoxidable A4 (DIN 125, M4 y M5) | 128 pzas | Distribución uniforme de carga de apriete. |
| **1.9** | Rondanas de Presión (Grower) | Acero Templado C-70 (DIN 127, M4 y M5) | 64 pzas | Aseguramiento elástico en uniones sometidas a alta vibración. |
| **1.10**| Rondanas de Fibra de Carbono | Fibra de Carbono estructural (Espesor $1.0\text{ mm}$, $\varnothing 15\text{ mm}$) | 32 pzas | Aislamiento galVánico y protección contra deslaminación. |

---

## ⚡ 2. Sistema Propulsor y Eléctrico (Motores, ESCs y Cables)

| Ít. | Componente / Subsistema | Especificación Técnica Nominal | Cantidad | Referencia / Fabricante |
| :--- | :--- | :--- | :--- | :--- |
| **2.1** | Motores Brushless Coaxiales | Alto torque magnético, bobinado en cobre clase H | 8 pzas | Configuración coaxial X8 |
| **2.2** | Controladores de Velocidad (ESC) | ESC FOC de alta eficiencia con telemetría en tiempo real | 8 pzas | Soporte HV 18S |
| **2.3** | Batería Principal HV | LiPo / Li-Ion HV 18S (66.6V nominal, descarga alta tasa) | 2 pzas (Set) | Autonomía de operación en campo |
| **2.4** | Placa de Distribución (PDB) | Heavy-Copper multicateada con aislamiento IP65 | 1 pza | PDB Principal PERLACO |
| **2.5** | Cables de Potencia AWG | Cable de cobre flexible AWG 8 y AWG 10 con funda ignífuga | 5 metros | Alimentación general de ESCs y PDB |
| **2.6** | Cableado de Señal / Datos | Cables mallados blindados trenzados para I2C / CAN / PWM | 10 metros | Conectividad de aviónica y sensores |

---

## 🛰️ 3. Aviónica, Navegación y Telecomunicaciones (Antenas)

| Ít. | Componente / Subsistema | Especificación Técnica / Modelo | Cantidad | Función Principal |
| :--- | :--- | :--- | :--- | :--- |
| **3.1** | Controlador de Vuelo | Pixhawk Cube Orange+ (STM32H757 Dual Core) | 1 pza | Cerebro de navegación (ArduPilot Copter 4.3+) |
| **3.2** | Sistema GNSS RTK | Doble u-blox ZED-F9P (Moving Baseline) | 2 módulos | Precisión milimétrica de posicionamiento (8-12 mm RMS) |
| **3.3** | Antenas GPS / RTK | Antenas helicoidales cuatrifilares de alta ganancia | 2 pzas | Recepción de constelaciones satelitales y corrección RTK |
| **3.4** | Radio Telemetría Off-Grid | Módulo FANET / LoRa en banda ISM 915 MHz | 2 pzas | Enlace de datos punto a multipunto sin red celular |
| **3.5** | Antenas de Telemetría RF | Antenas omnidireccionales de 915 MHz con conector SMA | 2 pzas | Transmisión de telemetría y comandos MAVLink |

---

## 💧 4. Sistema Hidráulico, Mangueras, Atomizadores y Aspersores

| Ít. | Componente / Subsistema | Especificación Técnica / Material | Cantidad | Función Principal |
| :--- | :--- | :--- | :--- | :--- |
| **4.1** | Tanque de Caldo Agrícola | Polietileno de alta densidad (HDPE) con escala de nivel ($35\text{ L}$) | 1 pza | Almacenamiento de sopa líquida VRA |
| **4.2** | Bomba de Presión | Bomba triplex de diafragma con control PWM adaptativo | 1 pza | Presurización de línea hidráulica ($0 - 120\text{ psi}$) |
| **4.3** | Mangueras Hidráulicas | Manguera mallada de PVC flexible de alta presión ($1/4\text{ pulgadas}$) | 8 metros | Conducción de caldo hacia boquillas y atomizadores |
| **4.4** | Conectores Rápidos Hidráulicos | Serie CPC PLC ($1/4\text{ Flow}$) en acetal con sellos de Buna-N | 6 juegos | Conexión y desconexión rápida de recarga (120 psi máx) |
| **4.5** | Caudalímetro de Efecto Hall | Sensor de turbina con linealización por Filtro Kalman 1D | 1 pza | Medición de flujo en tiempo real (50 Hz) |
| **4.6** | Atomizadores Centrifugos CDA | Atomizadores de gota variable controlada ($80$ a $600\text{ }\mu\text{m}$) | 4 pzas | Aspersión ultrafina de alta cobertura foliar |
| **4.7** | Boquillas / Aspersores VRA | Manifold de inyección en POM-C con válvulas solenoides PWM | 4 pzas | Regulación de caudal variable por sección |

---

## 💻 5. Software, Firmware y Edge AI

| Ít. | Módulo / Software | Versión / Plataforma | Descripción y Aplicación |
| :--- | :--- | :--- | :--- |
| **5.1** | Firmware de Autopiloto | ArduPilot Copter v4.3+ (Custom PERLACO) | Control de vuelo autónomo, navegación georreferenciada y failsafes. |
| **5.2** | Modelo de Visión Artificial | YOLOv8-FDA (Edge AI On-board, $2.96\text{ MB}$) | Conteo de cepas de caña y cálculo de LAI en tiempo real ($19.2\text{ FPS}$). |
| **5.3** | Algoritmo VRA & Kalman | Python / C++ en Companion Computer | Filtrado estocástico de caudal y dosificación adaptativa de sopa líquida. |
| **5.4** | Consenso de Red (PoA) | Protocolo Proof-of-Authority Off-Grid | Aislamiento de nodos bizantinos y sincronización de enjambre. |

---
*ELECTRÓNICA PERLACO / PERLACOLABS — Úrsulo Galván, Veracruz, México*

# 📦 Lista Oficial de Materiales (BOM v3.5) - ELECTRÓNICA PERLACO STR-002 H3
**Plataforma Aérea Agrícola (MTOW 29.0 kg) — Octocóptero Coaxial X8 Rediseñado**  
**Auditoría de Ingeniería:** Pérdidas Coaxiales, Térmicas en PDB, Ruido Vibracional y Conectividad Hidráulica CPC  
**Autor:** Angel Imer Lara Colorado / **PERLACOLABS** — *Úrsulo Galván, Veracruz, México*

---

## 🛠️ 1. Estructura, Chasis y Desacoplamiento Vibracional
| Componente | Especificación Técnica & Datasheet | Cantidad | Ubicación / Montaje Mecánico |
| :--- | :--- | :---: | :--- |
| **Chasis Principal** | Fibra de carbono 3K + Aluminio CNC 6061 | 1 | Estructura central Octocóptero X8 |
| **Lanzas Extensoras de Aspersión** | Tubos de fibra de carbono Ø16 mm extruido | 4 | Extendidas 20 cm fuera del eje del downwash directo |
| **Montaje Antivibratorio de Caudalímetro** | Bujes de **Sorbothane Duo-Density 50D** + TPU 85A | 1 juego | Aislamiento armónico del cuerpo del sensor de flujo |
| **Manguera Flexible Anti-Propagación** | EPDM Siliconado de alta flexión Ø12 mm | 0.8 m | Tramos de 10 cm antes y después del caudalímetro |

---

## 💧 2. Sistema Hidráulico Industrial & Recarga Rápida
| Componente | Especificación Técnica & Datasheet | Cantidad | Ubicación / Montaje Mecánico |
| :--- | :--- | :---: | :--- |
| **Conectores Acople Rápido** | **CPC PLC Series 1/4" Flow (Acetal / Buna-N / SS Latch, 120 psi)** | 2 pares | Conexión rápida de la línea principal del tanque de Sopa Líquida |
| **Bomba de Aspersión PWM** | Bomba de diafragma de alta presión de 12V / 5.0 L/min | 2 | Montaje central bajo chasis con damper de caucho |
| **Boquillas de Aspersión** | Boquillas de abanico plano anti-deriva VMD 200–280 µm | 4 | Extremos de las lanzas de fibra de carbono |

---

## ⚡ 3. Propulsión, Hélices de Paso Diferencial y Control Térmico
| Componente | Especificación Técnica & Datasheet | Cantidad | Ubicación / Montaje Mecánico |
| :--- | :--- | :---: | :--- |
| **Motores Brushless** | T-Motor P80 III KV120 (Empuje máx. 18.4 kg/motor) | 8 | Configuración Coaxial Co-Rotativa / Contrarrotativa |
| **Controladores ESC** | T-Motor Alpha 80A HV FOC (IP67, Telemetría RPM/CAN) | 8 | Bajo motores con disipador expuesto al flujo de aire |
| **Hélices Superiores (Top)** | Carbono Polímero **30x10.5"** Plegables | 4 pares | Rotores superiores (Aire denso de entrada) |
| **Hélices Inferiores (Bottom)** | Carbono Polímero **30x11.5" (Paso Mayor +1.0")** | 4 pares | Rotores inferiores (Compensación de velocidad de aire) |
| **PDB Heavy-Copper de Alta Corriente** | PDB Industrial de **6 oz Cobre (210 µm)** + Busbars Cobre | 1 | Núcleo del chasis acoplado a disipador de aluminio anodizado |
| **Barniz Dieléctrico / Conformante** | MG Chemicals 422B Silicone Conformal Coating | 1 lata | Recubrimiento hidrófugo y químico sobre PDB y sensores |

---

## 🧠 4. Aviónica, Medición Hall, Edge AI y Filtros Dinámicos
| Componente | Especificación Técnica & Datasheet | Cantidad | Ubicación / Montaje Mecánico |
| :--- | :--- | :---: | :--- |
| **Piloto Automático** | Cube Orange+ (Procesador STM32H7, Triple IMU aislada) | 1 | Amortiguación dieléctrica interna + Filtro Notch BDShot |
| **Unidad Edge AI (Visión A Bordo)** | **Micro-computador embebido (YOLOv8-FDA 2.96 MB, 19.2 FPS)** | 1 | Soporte superior en cúpula Canopy IP67 |
| **Sensor de Corriente Hall Aislado** | **Allegro ACS770LCB-050B / ACS758 (300A, Galvanic Isolation)** | 1 | Integrado en la línea principal VCC sin shunt resistivo |
| **Navegación GNSS RTK** | Doble ZED-F9P RTK Moving Baseline (GPS/GLONASS/Galileo/Beidou) | 2 | Antenas en mástiles de brazos principal y secundario |
| **Sensor de Flujo Digital** | Caudalímetro ultrasónico / pulso con **Filtro de Kalman Embebido** | 1 | Tubería principal aislada hidráulicamente |

---
**ELECTRÓNICA PERLACO / PERLACOLABS** — *Ingeniería Agrícola de Alta Resiliencia.*

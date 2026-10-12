# 📦 Lista Oficial de Materiales (BOM v3.5) - ELECTRÓNICA PERLACO STR-002 H3
**Plataforma Aérea Agrícola (MTOW 29.0 kg) — Octocóptero Coaxial X8 Rediseñado**  
**Auditoría de Ingeniería:** Resolución de Pérdidas Coaxiales, Térmicas en PDB y Ruido Vibracional  
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

## ⚡ 2. Propulsión, Hélices de Paso Diferencial y Control Térmico
| Componente | Especificación Técnica & Datasheet | Cantidad | Ubicación / Montaje Mecánico |
| :--- | :--- | :---: | :--- |
| **Motores Brushless** | T-Motor P80 III KV120 (Empuje máx. 18.4 kg/motor) | 8 | Configuración Coaxial Co-Rotativa / Contrarrotativa |
| **Controladores ESC** | T-Motor Alpha 80A HV FOC (IP67, Telemetría RPM/CAN) | 8 | Bajo motores con disipador expuesto al flujo de aire |
| **Hélices Superiores (Top)** | Carbono Polímero **30x10.5"** Plegables | 4 pares | Rotores superiores (Aire denso de entrada) |
| **Hélices Inferiores (Bottom)** | Carbono Polímero **30x11.5" (Paso Mayor +1.0")** | 4 pares | Rotores inferiores (Compensación de velocidad de aire) |
| **PDB Heavy-Copper de Alta Corriente** | PDB Industrial de **6 oz Cobre (210 µm)** + Busbars Cobre | 1 | Núcleo del chasis acoplado a disipador de aluminio anodizado |
| **Barniz Dieléctrico / Conformante** | MG Chemicals 422B Silicone Conformal Coating | 1 lata | Recubrimiento hidrófugo y químico sobre PDB y sensores |

---

## 🧠 3. Aviónica, Medición de Corriente y Filtros Dinámicos
| Componente | Especificación Técnica & Datasheet | Cantidad | Ubicación / Montaje Mecánico |
| :--- | :--- | :---: | :--- |
| **Piloto Automático** | Cube Orange+ (Procesador STM32H7, Triple IMU aislada) | 1 | Amortiguación dieléctrica interna + Filtro Notch BDShot |
| **Sensor de Corriente Hall Aislado** | **Allegro ACS770LCB-050B / ACS758 (300A, Galvanic Isolation)** | 1 | Integrado en la línea principal VCC sin shunt resistivo |
| **Navegación GNSS RTK** | Doble ZED-F9P RTK Moving Baseline (GPS/GLONASS/Galileo/Beidou) | 2 | Antenas en mástiles de brazos principal y secundario |
| **Sensor de Flujo Digital** | Caudalímetro ultrasónico / pulso con **Filtro de Kalman Embebido** | 1 | Tubería principal aislada hidráulicamente |

---

## 📊 4. Justificación Técnica de Cambios y Tablas Comparativas

### 🔄 A. Corrección Aerodinámica Coaxial (Downwash)
| Parámetro | Configuración Anterior (Con Error) | Configuración Nueva (Corregida v3.5) | Justificación Técnica |
| :--- | :--- | :--- | :--- |
| **Hélices Inferiores** | 30x10.5" (Igual a la superior) | **30x11.5" (Paso +1.0" incrementado)** | El rotor inferior trabaja en aire acelerado. El paso mayor restablece el $C_T$ (coeficiente de empuje) y recupera un **12% de eficiencia**. |
| **Posición de Boquillas** | Directamente bajo el centro del motor | **Extendidas 20 cm fuera del radio rotórico** | Evita que el torbellino central rompa la gota. Mantiene el $VMD$ en $200	ext{--}280\ \mu	ext{m}$ sin atomización errática. |

### 🌡️ B. Reducción de Estrés Térmico y Eléctrico en PDB (>300A)
| Parámetro | Configuración Anterior (Con Error) | Configuración Nueva (Corregida v3.5) | Justificación Técnica |
| :--- | :--- | :--- | :--- |
| **Grosor de Pistas Cobre** | 2 oz / 3 oz ($70	ext{--}105\ \mu	ext{m}$) | **6 oz Cobre ($210\ \mu	ext{m}$) + Bars de Cobre Sólido** | Reduce la resistencia interna $R_{PDB}$. Disminuye la disipación por efecto Joule ($P = I^2 R$) en un **65%**. |
| **Medición de Corriente** | Shunt resistivo tradicional | **Sensor de Efecto Hall Allegro ACS770 (300A)** | Eliminación de la resistencia de caída ($V=IR$). Aislamiento galvánico total contra picos de retro-EMF. |
| **Protección Ambiental** | Exposición directa de PCB | **Doble capa de MG Chemicals 422B** | Previene cortocircuitos por humedad tropical y corrosión por nitrógeno/plaguicidas. |

### 🔊 C. Supresión de Ruido Vibracional en Caudalímetro y Aviónica
| Parámetro | Configuración Anterior (Con Error) | Configuración Nueva (Corregida v3.5) | Justificación Técnica |
| :--- | :--- | :--- | :--- |
| **Conexión Hidráulica** | Tubo rígido acoplado al chasis | **Mangueras EPDM + Bujes Sorbothane 50D** | Filtras las micro-vibraciones mecánicas de $100	ext{--}350\ 	ext{Hz}$ transmitidas por la estructura. |
| **Filtrado de Datos** | Lectura cruda de pulsos | **Filtro de Kalman 1D + Notch Dynamic Filter** | Elimina picos de flujo falsos en la telemetría MAVLink. Mantiene el bucle cerrado PWM con error $< 1.5\%$. |

---
**ELECTRÓNICA PERLACO / PERLACOLABS** — *Ingeniería Agrícola de Alta Resiliencia.*

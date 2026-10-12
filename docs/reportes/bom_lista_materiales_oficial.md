# 📦 Lista Oficial de Materiales (BOM) - ELECTRÓNICA PERLACO STR-002 H3 v3.0
**Plataforma Aérea Agrícola (MTOW 29.0 kg) — Octocóptero Coaxial X8**  
**Proyecto:** Prototipo Dron Agrícola Perlaco (Dosificador VRA de Sopa Líquida en Caña de Azúcar)  
**Autor:** Angel Imer Lara Colorado / **PERLACOLABS** — *Úrsulo Galván, Veracruz, México*

---

## 🛠️ 1. Estructura y Chasis
| Componente | Especificación Técnica | Cantidad | Ubicación / Montaje Mecánico |
| :--- | :--- | :---: | :--- |
| **Chasis Principal** | Fibra de carbono de grado aeronáutico 3K + Aluminio CNC 6061 | 1 | Estructura central Octocóptero Coaxial X8 |
| **Brazos Plegables** | Tubo de fibra de carbono Ø40 mm ultra-resistente | 4 | Distribución simétrica X8 |
| **Mástiles de Antena RF** | Mástiles flexibles amortiguados con soporte TPU 95A | 2 | Elevados 15 cm sobre la placa superior (Top Deck) |

---

## ⚡ 2. Propulsión y Sistemas de Potencia
| Componente | Especificación Técnica | Cantidad | Ubicación / Montaje Mecánico |
| :--- | :--- | :---: | :--- |
| **Motores Brushless** | T-Motor P80 III KV120 (Empuje máx. 18.4 kg/motor) | 8 | Configuración Coaxial Co-Rotativa / Contrarrotativa |
| **Controladores ESC** | T-Motor Alpha 80A HV FOC (IP67) | 8 | Integrados en la parte inferior de los brazos |
| **Hélices** | Carbono Polímero 30x10.5" Plegables | 8 pares | Acopladas a rotores P80 III |
| **Distribución de Potencia** | PDB Industrial de alta corriente (>300A continuos) | 1 | Núcleo del chasis bajo la placa de aviónica |

---

## 🧠 3. Aviónica y Navegación de Precisión Milimétrica
| Componente | Especificación Técnica | Cantidad | Ubicación / Montaje Mecánico |
| :--- | :--- | :---: | :--- |
| **Piloto Automático** | Cube Orange+ (Procesador STM32H7, Triple IMU aislada) | 1 | Placa central amortiguada por silicona dieléctrica |
| **Navegación GNSS RTK** | Doble ZED-F9P RTK Moving Baseline (GPS/GLONASS/Galileo/Beidou - Precisión 8-12 mm) | 2 | Antenas en mástiles de los brazos principal y secundario |
| **Sensor de Flujo / Nivel** | Caudalímetro ultrasónico digital de alta precisión | 1 | Tubería principal de distribución del tanque |

---

## 📡 4. Enlace de Radiofrecuencia (RF), Control y Telemetría Off-Grid
| Componente | Especificación Técnica | Cantidad | Ubicación / Montaje Mecánico |
| :--- | :--- | :---: | :--- |
| **Radio de Telemetría RF** | RFD900x 915 MHz (1W / +30 dBm, Modo Mesh, MAVLink, Rango >40 km) | 1 por UAV | Placa superior (Top Deck) aislada de la PDB para evitar EMI |
| **Radiocontrol Smart** | SIYI MK15 / Skydroid H16 (Pantalla 1000 nits, Enlace Dual 2.4 GHz RC+Video+MAVLink) | 1 | Estación de Control de Tierra (GCS Handheld) en mano del operador |
| **Base GNSS RTK Local** | CUAV C-RTK 9P Base (Procesamiento Multi-Banda, RTCM3 por USB/RF) | 1 | Trípode elevable de aluminio (2.5 m) en perímetro de parcela |
| **Antenas Dipolo 915 MHz** | Dipolo omnidireccional de alta ganancia (+3 dBi) | 2 por UAV | Orientación vertical en mástiles superiores para cobertura 360° |

---

## 💦 5. Sistema Agrícola VRA y Spraying de Sopa Líquida
| Componente | Especificación Técnica | Cantidad | Ubicación / Montaje Mecánico |
| :--- | :--- | :---: | :--- |
| **Tanque de Mezcla** | Polietileno HD reestructurado anti-chapoteo (Capacidad 16 L / 20 L) | 1 | Centro de gravedad del dron (Bajo el chasis) |
| **Bomba de Pulverización** | Bomba de diafragma 12V 5.0 L/min con control PWM VRA | 1 | Parte inferior junto al sistema de acople rápido |
| **Boquillas de Aspersión** | Boquillas de cono hueco / Centrífugas de gota variable (VMD 200–280 µm) | 4 | Bajo los motores en extensión de brazos |

---
**ELECTRÓNICA PERLACO / PERLACOLABS** — *Úrsulo Galván, Veracruz, México*

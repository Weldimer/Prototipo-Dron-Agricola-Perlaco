# 🛠️ Lista Oficial de Materiales (BOM) Integral, Conectores y Datasheets — STR-002 H3 v3.5

**Plataforma Aérea Agrícola Autónoma (MTOW 60.0 kg) - Octóptero Coaxial X8**  
*Desarrollado por: Angel Imer Lara Colorado / PERLACOLABS — Úrsulo Galván, Veracruz, México*

---

## 📐 1. Dimensiones y Geometría General del Dron
* **Distancia Diagonal de Eje a Eje (Wheelbase):** $1,650	ext{ mm}$ ($1.65	ext{ m}$).
* **Dimensiones del Chasis Central (Placas Hexagonales):** Diámetro de $380	ext{ mm}$, espesor de $3.0	ext{ mm}$ con alvéolos de centrado P-01 ($arnothing 24.0	ext{ mm}$ H7).
* **Tren de Aterrizaje:** Altura libre al suelo de $450	ext{ mm}$, ancho de vía de $700	ext{ mm}$, construido con tubos de fibra de carbono pultruida de $arnothing 25	ext{ mm} 	imes 400	ext{ mm}$.
* **Brazos Principales:** 8 tubos de fibra de carbono bidireccional de $arnothing 50	ext{ mm}$, espesor de $2.0	ext{ mm}$ y longitud de $650	ext{ mm}$.

---

## ⚡ 2. Conectores de Potencia, Baja Potencia y Motores

| Ít. | Tipo de Conector / Subsistema | Especificación Técnica y Modelo | Cantidad | Función Principal |
| :--- | :--- | :--- | :--- | :--- |
| **2.1** | Conector de Batería Principal | **QS8-S Anti-Spark** (Pines de oro de $arnothing 8	ext{ mm}$ con resistencia de precarga) | 2 pares | Conexión segura de la batería HV 18S ($66.6	ext{ V}$) sin arcos eléctricos. |
| **2.2** | Conectores de Potencia de Motores | Conectores Bullet de Oro de $arnothing 4.0	ext{ mm}$ / MT60 trifásicos | 24 pzas | Enlace de alta corriente entre ESCs FOC y motores brushless coaxiales. |
| **2.3** | Conectores de Baja Potencia / PDB | JST-XH y Molex Micro-Fit 3.0 mm (multivía) | 12 juegos | Distribución de energía auxiliar de baja potencia ($12	ext{ V} / 5	ext{ V}$) para aviónica y bombas. |
| **2.4** | Cableado de Fuerza | Cable de cobre flexible de silicona **AWG 8 y AWG 10** | 6 metros | Conductores principales de alta capacidad de corriente desde la PDB hacia los ESCs. |

---

## 📚 3. Índice de Datasheets y Especificaciones de Componentes Clave

| Componente / Módulo | Fabricante / Modelo | Especificación Técnica Principal | Enlace a Documentación Interna |
| :--- | :--- | :--- | :--- |
| **Controlador de Vuelo** | Pixhawk Cube Orange+ | Procesador STM32H757 Dual Core, IMU redundante | [Ver Aviónica](investigacion_modulos.md) |
| **Sistema GNSS RTK** | u-blox ZED-F9P | Doble antena Moving Baseline (Precision 8-12 mm RMS) | [Ver Antenas RTK](investigacion_modulos.md) |
| **Control de Caudal VRA** | Pericope / Estimador Estocástico | Filtro Kalman 1D ($Q=0.01, R=0.25, f_s=50	ext{ Hz}$) | [Ver Firmware](vra_kalman.md) |
| **Cámara Edge AI** | Módulo Óptico / NVIDIA Jetson | Inferencia YOLOv8-FDA (2.96 MB, 19.2 FPS) | [Ver Visión AI](../borde_ai/yolo_entrenamiento.md) |
| **Radio de Telemetría** | Módulo LoRa / FANET | Banda ISM 915 MHz (Sin Wi-Fi ni Bluetooth) | [Ver Fail-Safe](../firmware/fail_safe_offgrid.md) |

---
*ELECTRÓNICA PERLACO / PERLACOLABS — Úrsulo Galván, Veracruz, México*

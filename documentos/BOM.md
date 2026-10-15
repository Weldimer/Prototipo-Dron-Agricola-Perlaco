# 🛠️ Lista Oficial de Materiales (BOM) Integral, Conectores y Datasheets — STR-002 H3 v3.5

**Plataforma Aérea Agrícola Autónoma (MTOW 29.0 kg) - Octóptero Coaxial X8**  
*Desarrollado por: Angel Imer Lara Colorado / PERLACOLABS — Úrsulo Galván, Veracruz, México*

---

## 📐 1. Dimensiones y Geometría General del Dron
* **Distancia Diagonal de Eje a Eje (Wheelbase):** $1,650\text{ mm}$ ($1.65\text{ m}$).
* **Dimensiones del Chasis Central (Placas Hexagonales):** Diámetro de $380\text{ mm}$, espesor de $3.0\text{ mm}$ con alvéolos de centrado P-01 ($\varnothing 24.0\text{ mm}$ H7).
* **Tren de Aterrizaje:** Altura libre al suelo de $450\text{ mm}$, ancho de vía de $700\text{ mm}$, construido con tubos de fibra de carbono pultruida de $\varnothing 25\text{ mm} \times 400\text{ mm}$.
* **Brazos Principales:** 8 tubos de fibra de carbono bidireccional de $\varnothing 50\text{ mm}$, espesor de $2.0\text{ mm}$ y longitud de $650\text{ mm}$.

---

## ⚡ 2. Conectores de Potencia, Baja Potencia y Motores

| Ít. | Tipo de Conector / Subsistema | Especificación Técnica y Modelo | Cantidad | Función Principal |
| :--- | :--- | :--- | :--- | :--- |
| **2.1** | Conector de Batería Principal | **QS8-S Anti-Spark** (Pines de oro de $\varnothing 8\text{ mm}$ con resistencia de precarga) | 2 pares | Conexión segura de la batería HV 18S ($66.6\text{ V}$) sin arcos eléctricos. |
| **2.2** | Conectores de Potencia de Motores | Conectores Bullet de Oro de $\varnothing 4.0\text{ mm}$ / MT60 trifásicos | 24 pzas | Enlace de alta corriente entre ESCs FOC y motores brushless coaxiales T-Motor P80 III. |
| **2.3** | Conectores de Baja Potencia / PDB | JST-XH y Molex Micro-Fit 3.0 mm (multivía) | 12 juegos | Distribución de energía auxiliar de baja potencia ($12\text{ V} / 5\text{ V}$) para aviónica y bombas. |
| **2.4** | Cableado de Fuerza | Cable de cobre flexible de silicona **AWG 8 y AWG 10** | 6 metros | Conductores principales de alta capacidad de corriente desde la PDB hacia los ESCs. |

---

## 📚 3. Índice de Datasheets y Especificaciones de Componentes Clave

| Componente / Módulo | Fabricante / Modelo | Especificación Técnica Principal | Enlace a Documentación Interna |
| :--- | :--- | :--- | :--- |
| **Controlador de Vuelo** | Pixhawk Cube Orange+ | Procesador STM32H757 Dual Core, IMU redundante | [Ver Aviónica](investigacion_modulos.md) |
| **Sistema GNSS RTK** | u-blox ZED-F9P | Doble antena Moving Baseline (Precisión 8-12 mm RMS) | [Ver Antenas RTK](investigacion_modulos.md) |
| **Control de Caudal VRA** | Pericope / Estimador Estocástico | Filtro Kalman 1D ($Q=0.01, R=0.25, f_s=50\text{ Hz}$) | [Ver Firmware](../firmware/vra_kalman.md) |
| **Cámara Edge AI** | Módulo Óptico / Jetson Nano | Inferencia YOLOv8-FDA (2.96 MB, 19.2 FPS) | [Ver Visión AI](../borde_ai/yolo_entrenamiento.md) |
| **Radio de Telemetría** | Módulo LoRa / FANET | Banda ISM 915 MHz (Sin Wi-Fi ni Bluetooth) | [Ver Fail-Safe](../firmware/fail_safe_offgrid.md) |

---
*ELECTRÓNICA PERLACO / PERLACOLABS — Úrsulo Galván, Veracruz, México*

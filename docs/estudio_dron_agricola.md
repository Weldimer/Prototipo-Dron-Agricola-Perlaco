# ESTUDIO TÉCNICO Y DE INGENIERÍA INTEGRAL — STR-002 H3 v3.0 / v2.5
**ELECTRÓNICA PERLACO — PERLACOLABS**  
**Autor e Inventor Principal:** Angel Imer Lara Colorado — *Úrsulo Galván, Veracruz, México*

---

## 1. Resumen Ejecutivo y Alcance del Prototipo
El prototipo **ELECTRÓNICA PERLACO STR-002 H3** es una plataforma aérea no tripulada (UAV) de categoría pesada (*Heavy-Lift*) diseñada para la aplicación agroquímica de alta precisión mediante asperjado de Tasa Variable (VRA).

* **Masa Máxima al Despegue (MTOW):** ~28.5 - 29.5 kg (Configuración v3.0 / escalable a 29 kg en v2.5-HV).
* **Capacidad de Carga Útil:** Estanque HDPE de 10.0 L con rompeolas dinámico.
* **Geometría Estructural:** Octocóptero Coaxial X8 con chasis central en Fibra de Carbono 3K (3.0 mm) y 8 brazos Ø50 mm con abrazaderas H3 en Aluminio 7075-T6.
* **Ecosistema de Aviónica:** Cube Orange+ (STM32H7), RTK Dual u-Blox ZED-F9P, Radar FMCW 77 GHz de altimetría y evasión 3D.

---

## 2. Arquitectura de Propulsión y Sistema Eléctrico 12S LiPo
* **Motopropulsores:** 8x Motores Brushless T-Motor P80 III KV120 con ESC T-Motor Alpha 80A HV.
* **Hélices:** Plegables de Fibra de Carbono 30x10.5".
* **Empuje Total Disponible:** 73.6 kg (Ratio Empuje/Peso nominal: 2.53:1).
* **Alimentación:** Paquete LiPo 12S 30,000 mAh (50.4 V pico) con conectores Anti-Spark QS8-S (R_precarga = 5.1 Ohm).
* **Gestión Térmica y BMS:** Monitoreo activo vía CAN/SMBus con límite térmico a 60 °C y corte RTL a 43.2 V (80% DoD).

---

## 3. Subsistema Hidráulico VRA y Control de Asperjado
* **Control de Caudal:** Caudalímetro YF-S201 (450 pulsos/L) con calibración dinámica por Lua (`flowmeter_calibration.lua`).
* **Corte Anti-Goteo:** 4x Electroválvulas Solenoides NC de 24V situadas en las puntas de los brazos con latencia de corte < 35 ms.
* **Regulación de Presión:** Control en lazo cerrado de 0 a 10 Bar (`nozzle_pressure_control.lua`) manteniendo el espectro de gota constante (200 - 300 µm).

---

## 4. Desarrollo Cloud-Native Móvil (PERLACOLABS)
El diseño, las simulaciones físicas (FFT Notch 45/90 Hz, respuesta inercial Z_CG, SAG de voltaje 12S), el modelado CAD/CAM vectorial DXF y la arquitectura de firmware Lua se desarrollaron de forma **100% cloud-native** utilizando un teléfono inteligente **Samsung Galaxy A04 (SM-A04)** acoplado a Google Colab y sincronización automatizada mediante la API de GitHub.

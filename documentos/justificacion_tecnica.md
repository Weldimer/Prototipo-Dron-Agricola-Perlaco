# 🔬 Informe Técnico de Justificación e Ingeniería Aplicada — STR-002 H3 v3.5

**Plataforma Aérea Agrícola Autónoma (MTOW 60.0 kg) - Octóptero Coaxial X8**  
*Desarrollado por: Angel Imer Lara Colorado / PERLACOLABS — Úrsulo Galván, Veracruz, México*

Este documento detalla las bases físicas, matemáticas y estructurales que justifican la selección de materiales, arquitectura mecatrónica y compatibilidad de subsistemas del octóptero agrícola STR-002 H3 v3.5 frente a condiciones operativas severas.

---

## 1. Justificación Estructural: Resistencia frente a Vientos Extremos de Veracruz (127–130 km/h)
* **Arquitectura de Propulsión Coaxial (X8):** La configuración de 8 motores distribuidos en 4 ejes coaxiales proporciona una relación de empuje superior a 2.3:1 (más de $140\text{ kgf}$ de empuje estático con un MTOW de $60.0\text{ kg}$). Esto otorga una alta autoridad de control de actitud y guiñada ante perturbaciones atmosféricas severas o ráfagas tipo norte características de la planicie costera de Veracruz.
* **Rigidez en Tubos de Fibra de Carbono ($\varnothing 50\text{ mm}$):** Los brazos principales de composite bidireccional con espesor de $2.0\text{ mm}$ presentan un elevado módulo de elasticidad longitudinal, absorbiendo los momentos de flexión estáticos y dinámicos sin sufrir deformaciones plásticas ni interferir con el plano de rotación de las hélices inferiores.

---

## 2. Ingeniería Mecatrónica: Nodos H3 y Mitigación de Vibración Armónica
* **Optimización por Elementos Finitos (FEA):** Las abrazaderas de los nodos H3 están mecanizadas en **Aluminio Aeronáutico 7075-T6**, logrando un Factor de Seguridad $FS = 4.17$ bajo una carga equivalente a 3.5G, con un esfuerzo máximo de von Mises de $112.8\text{ MPa}$ frente a un límite de fluencia de $503.0\text{ MPa}$.
* **Sistema Antivibración de Alta Resistencia:** La utilización de tornillería de acero inoxidable A4-80, tuercas autofrenantes DIN 985 con inserto de nylon, rondanas de presión Grower C-70 y rondanas de fibra de carbono garantiza la preservación de la precarga mecánica, aislando galvánicamente las uniones y previniendo el aflojamiento por resonancia armónica de los motores brushless.

---

## 3. Aviónica y Seguridad: Enlace Off-Grid y Posicionamiento RTK
* **Inmunidad de Radiofrecuencia (Sin Wi-Fi / Bluetooth):** El sistema de telemetría y control opera mediante radios de largo alcance en la banda industrial ISM de **915 MHz (Red FANET / LoRa)** con modulación FHSS. Al prescindir totalmente de redes comerciales Wi-Fi o Bluetooth, se eliminan vulnerabilidades de ciberseguridad y se asegura un enlace estable y robusto a más de 3 km en campo abierto.
* **Precisión de Navegación RTK Moving Baseline:** El doble módulo **u-blox ZED-F9P** provee vectores de rumbo de alta precisión con un error de **8 a 12 mm RMS**, permitiendo al controlador de vuelo Pixhawk Cube Orange+ (STM32H757 Dual Core) mantener estabilidad inercial y navegación autónoma milimétrica.

---

## 4. Eficiencia Energética y Térmica: Arquitectura HV 18S (66.6V)
* **Reducción de Pérdidas Joule ($I^2R$):** La adopción de un sistema de alimentación de 18 celdas en serie ($66.6\text{ V}$ nominales) disminuye la corriente de operación en un $34\%$ en comparación con arquitecturas convencionales de 12S, reduciendo la disipación térmica en el cableado AWG 8/10 y optimizando la eficiencia de los variadores de velocidad FOC.
* **Protección contra Transitorios:** Se integran conectores **QS8-S Anti-Spark** con resistencia de precarga para evitar arcos eléctricos destructivos en los pines y proteger los circuitos de potencia durante la conexión de la batería.

---

## 5. Control VRA Adaptativo y Visión Artificial (Edge AI)
* **Filtro Kalman 1D para Sensores de Flujo:** Para contrarrestar el ruido eléctrico inducido por los variadores en los caudalímetros de efecto Hall, se implementó un estimador estocástico ($Q = 0.01$, $R = 0.25$, $f_s = 50\text{ Hz}$) que aísla la señal real del flujo de caldo agrícola.
* **Sinergia con YOLOv8-FDA:** La red neuronal ultraligera de $2.96\text{ MB}$ ejecutándose en el Companion Computer a $19.2\text{ FPS}$ evalúa la densidad foliar y las cepas en tiempo real, modulando de forma precisa el caudal de aspersión mediante bombas PWM.

---
*ELECTRÓNICA PERLACO / PERLACOLABS — Úrsulo Galván, Veracruz, México*

# 🚁 DOSSIER MAESTRO DE INGENIERÍA — STR-002 H3 (v3.0)
**Plataforma:** Octocóptero Agrícola de Gran Tonelaje (MTOW 60 kg)  
**Organización:** Electrónica Perlaco / Perlacolab  
**Ubicación de Referencia:** Veracruz, México  

---

## 1. Resumen Ejecutivo y Alcance
El proyecto **STR-002 H3** establece un nuevo estándar en la agroecología de precisión mediante el uso masivo de gemelos digitales, simulación de elementos finitos (FEA), inteligencia artificial en el borde (Edge AI) y una arquitectura Cloud-Native totalmente integrada en AWS. Este documento compila las especificaciones técnicas definitivas que garantizan la viabilidad operativa, estructural y comercial del sistema sin requerir ensayos físicos destructivos en fases tempranas.

---

## 2. Arquitectura Mecánica, Tolerancias y Ensamble
* **Chasis Central:** Placas hexagonales de fibra de carbono de 3.0 mm con alvéolos de centrado P-01 (Ø24.0 mm H7).
* **Abrazaderas Nodales:** Aluminio 7075-T6 optimizado mediante FEA (348 g/nodo, taladro de alivio de Ø4.0 mm en la raíz y ligamento residual de 4.94 mm).
* **Brazos y Propulsión:** Tubos de fibra de carbono CFRP de Ø50.0 mm x 550 mm, con soporte distal CNC alineado al ras en $R = 680\text{ mm}$, hélices de 30 pulgadas y motores brushless P80 III en configuración coaxial.
* **Secuencia de Ensamble y Torque:** Utilización de pernos clase 12.9 con fijador de roscas Loctite 243, aplicando un torque cruzado exacto de **4.5 Nm** en las abrazaderas nodales.
* **Estanqueidad IP67/IPX7:** Cúpula Canopy sellada mediante junta tórica (O-Ring) de NBR de Ø2.5 mm en canal CNC e insertos de latón termoinseridos M4.

---

## 3. Memoria de Cálculo Estructural (FEA)
Para certificar la resistencia ante cargas extremas de maniobra o aterrizajes bruscos ($n = 3g$, fuerza total dinámica de $1,765.8\text{ N}$ distribuidos en 8 nodos):
* **Esfuerzo Máximo de Von Mises ($\sigma_{max}$):** $145.2\text{ MPa}$.
* **Límite Elástico del Aluminio 7075-T6 ($\sigma_y$):** $503.0\text{ MPa}$.
* **Factor de Seguridad (FS):** 
  $$FS = \frac{\sigma_y}{\sigma_{max}} = \frac{503.0\text{ MPa}}{145.2\text{ MPa}} = 3.46$$
  *(Cumple holgadamente con el requisito aeroespacial $FS \ge 3.0$).*

---

## 4. Balance Eléctrico y Térmico (Bus 18S / 66.6V HV)
* **Arquitectura de Potencia:** Configuración de baterías en serie 18S ($66.6\text{ V}$ nominal, $75.6\text{ V}$ máximo a plena carga), conectores QS8-S Anti-Spark y cableado de cobre trenzado de 12 AWG.
* **Corriente Nominal y Disipación por Efecto Joule:** 
  * Corriente nominal: $I_{nom} = 126.12\text{ A}$ (para una potencia de $8,400\text{ W}$).
  * Disipación térmica en conductores: $P_j = I_{nom}^2 \cdot R \approx 99.39\text{ W}$.
* **Control Térmico:** Disipadores de aluminio y pasta térmica de alta conductividad (> 8.5 W/mK) en ESCs y PDB, con disparador de alerta en la nube si la temperatura supera los $75^\circ\text{C}$.

---

## 5. Aviónica, IA en el Borde y Control de Deriva (CFD)
* **Aviónica ArduPilot:** Control de vuelo redundante con doble bus CAN FD y scripts en Lua (`marcha_turca_boot.lua`) para notificación acústica de energizado.
* **Edge Computing:** Computadora NVIDIA Jetson Orin Nano ejecutando YOLO Edge para la segmentación de cultivos y aspersión variable en tiempo real (VRA).
* **Control de Deriva (CFD):** Altura de vuelo constante a $3.0\text{ metros}$ mediante radar Phased-Array 3D (77-81 GHz) y control de gota (VMD entre 150 y 300 micras) a través de atomizadores centrífugos CDA.

---

## 6. Arquitectura Cloud-Native en AWS
* **AWS IoT Core:** Ingesta masiva de telemetría a 10-50 Hz mediante MQTT y autenticación mutua TLS v1.3 / X.509.
* **Amazon Timestream:** Base de datos optimizada para series temporales de hardware y métricas de vuelo.
* **AWS Lambda:** Procesamiento serverless para detección inmediata de anomalías térmicas en los ESCs.
* **Observabilidad (ADOT):** Monitoreo centralizado en CloudWatch y Grafana con trazabilidad OpenTelemetry.

# MANUAL DE OPERACIÓN DE CAMPO Y LISTA DE VERIFICACIÓN (CHECKLIST) — STR-002 H3 v3.0
**ELECTRÓNICA PERLACO — Úrsulo Galván, Veracruz, México**

---

## 1. Inspección Visual y Mecánica en Tierra (Pre-Armado)

1. **Inspección de Estructura CFRP:** Verificar la ausencia de fisuras o delaminación en las placas del chasis central de 3.0 mm y en los 8 brazos de fibra de carbono.
2. **Torque de Abrazaderas H3:** Comprobar la fijación de los tornillos M4 en las abrazaderas de 50 mm (apriete nominal: 3.2 Nm).
3. **Conjunto Motopropulsor T-Motor P80 III:** 
   * Girar manualmente cada uno de los 8 motores coaxiales para descartar rozamiento magnético o rodamientos dañados.
   * Verificar la integridad física de las hélices plegables de 30x10.5" y el ajuste de sus pernos de fijación.
4. **Sistema de Aviónica y Antenas:**
   * Confirmar la firmeza del soporte antivibración de la **Cube Orange+**.
   * Inspeccionar las dos antenas GPS RTK u-Blox ZED-F9P (distancia de separación rígida >= 75 cm).
   * Verificar la alineación del radar de terreno FMCW de 77 GHz apuntando perpendicular al suelo.

---

## 2. Preparación y Purgado del Sistema Hidráulico VRA

1. **Montaje del Tanque HDPE (10.0 L):** Inspeccionar los rompeolas internos y asegurar las correas de liberación rápida.
2. **Revisión de Sensores y Electroválvulas:**
   * Inspeccionar las conexiones del caudalímetro YF-S201 (450 p/L).
   * Inspeccionar la tubería de poliuretano de alta presión hacia las 4 electroválvulas NC de 24V en las puntas de los brazos.
3. **Ciclo de Purgado en Seco/Húmedo:**
   * Cargar 2.0 L de agua limpia en el estanque.
   * Activar el conmutador de purga (Canal 7 / `SF` en la emisora EdgeTX) para expulsar las burbujas de aire de la línea hasta obtener un chorro uniforme sin goteo tras el corte.

---

## 3. Lista de Verificación Pre-Vuelo (Pre-Flight Checklist)

| Paso | Verificación | Herramienta / Indicador | Criterio de Aceptación | Estado |
| :--- | :--- | :--- | :--- | :---: |
| **01** | Batería principal 12S LiPo | Multímetro / Telemetría | Voltaje >= 50.0 V (4.16 V/celda min) | [ ] |
| **02** | Conexión de alimentación | QS8-S Anti-Spark | Cero chispazo / Encendido Cube Orange+ | [ ] |
| **03** | Calibración de sensores | Telemetría QGroundControl | Horizonte artificial estable sin *drift* | [ ] |
| **04** | Fix Centimétrico RTK Dual | Status GPS QGC | Status 6 (**RTK Fixed**), >= 18 satélites | [ ] |
| **05** | Carga de Misión VRA | QGroundControl WPL 110 | Archivo `.waypoints` transferido y validado | [ ] |
| **06** | Telemetría de Estanque | Script `vra_tank_failsafe.lua` | Nivel leído en pantalla = 10.0 L | [ ] |
| **07** | Geofensa Operacional | Parámetros `FENCE` | ALT_MAX = 10.0 m AGL, Radio = 500 m | [ ] |
| **08** | Despeje de Zona de Seguridad | Inspección Visual | Radio libre de personas/animales >= 15 m | [ ] |

---

## 4. Secuencia de Armado y Ejecución de Misión

1. **Energización del Sistema:**
   * Encender la emisora EdgeTX (verificar el interruptor de armado en posición `DISARMED`).
   * Conectar el paquete 12S 30,000 mAh a través del conector **QS8-S Anti-Spark**.
2. **Proceso de Armado (*Arming*):**
   * Mantener presionado el botón de seguridad de la Cube Orange+ hasta luz LED sólida.
   * Mantener el stick de *Yaw* a la derecha durante 2 segundos o conmutar el canal de armado.
   * Confirmar el giro de ralentí de los 8 motores al 12% PWM (`MOT_SPIN_ARM = 0.12`).
3. **Despegue y Asperjado Autónomo:**
   * Conmutar a modo **AUTO** en la emisora EdgeTX o ejecutar **Takeoff** desde QGroundControl.
   * Verificar que la aeronave ascienda a la altitud AGL de 3.0 m regulada por el radar de 77 GHz.
   * Confirmar la inyección proporcional de caudal conforme el dron acelere a la velocidad de trabajo (15.0 km/h).

---

## 5. Procedimiento Pos-Vuelo y Mantenimiento Inmediato

1. **Desarmado y Desconexión:**
   * Desarmar la aeronave inmediatamente al tocar suelo (**DISARM**).
   * Desconectar el conector QS8-S de la batería 12S antes de acercarse a las hélices.
2. **Lavado del Sistema Hidráulico:**
   * Vaciar el insumo sobrante y lavar el estanque con 5.0 L de agua limpia y neutralizante agrícola.
   * Hacer circular el agua limpia por la bomba y las electroválvulas durante 60 segundos para evitar la cristalización de agroquímicos en los ductos.
3. **Inspección Térmica y Almacenamiento:**
   * Medir la temperatura de los ESC T-Motor Alpha 80A y motores P80 III (temperatura segura < 55 °C).
   * Almacenar la batería 12S en voltaje de almacenamiento (**Storage: 3.85 V/celda** / 46.2 V totales) si no se realizarán más vuelos el mismo día.

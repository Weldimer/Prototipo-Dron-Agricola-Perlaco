# MANUAL TÉCNICO DE USUARIO Y OPERACIÓN — STR-002 H3 v3.5

## 1. Especificaciones y Parámetros Oficiales del Sistema
Antes de cualquier configuración, verifica que tu estación y hardware coincidan con estos valores base unificados:
* **MTOW (Peso Máximo al Despegue):** 29.0 kg
* **Arquitectura de Potencia:** Batería LiPo 12S (44.4 V nominal / 50.4 V pico)
* **Relación Empuje/Peso:** 2.54:1
* **Aviónica:** Pixhawk Cube Orange+ con GNSS RTK u-blox ZED-F9P (Precisión de 10.0 mm)
* **Factores de Seguridad Estructural:** Rango real de 3.5 - 4.9 (Diseñado para carga límite de 101.5 kg bajo factor de carga de 3.5G).

----

## 2. Guía de Programación y Configuración Paso a Paso

### Paso 2.1. Configuración de Aviónica (ArduCopter)
1. Conecta la controladora de vuelo a la estación de tierra (Mission Planner o QGroundControl).
2. Selecciona el tipo de marco (Frame): Octocopter Coaxial X8 (o la variante de Hexacopter de aluminio en 6S si aplica).
3. **Parámetros de Batería (Bus 12S):**
   * Configura el tipo de monitor de energía en celdas: `BATT_CRT_VOLT` a 42.0 V (3.5V por celda) y `BATT_LOW_VOLT` a 43.2 V (3.6V por celda).
   * Voltaje máximo a cargar: 50.4 V.
4. **Calibración de Sensores:** Ejecuta las rutinas de calibración de brújula (Compass), acelerómetros y nivel del horizonte.

### Paso 2.2. Configuración del Sistema RTK (u-blox ZED-F9P)
1. Conecta el módulo GPS al puerto serial principal de la Pixhawk.
2. Configura la entrada de correcciones RTCM mediante enlace de radio o red NTRIP en la GCS.
3. **Verificación crítica:** No procedas al armado de motores hasta que el estado del GPS indique **RTK Fixed**.

### Paso 2.3. Calibración del Sistema de Aspersión VRA (PWM)
1. Mapea un canal auxiliar (AUX) de la Pixhawk para gobernar el variador (ESC) de la bomba de caudal.
2. Vincula la velocidad lineal del dron con la apertura de la bomba mediante el script de control a bordo para tasa variable (VRA).

----

## 3. Guía de Errores, Diagnóstico y Resolución de Fallas (Troubleshooting)

### A. Errores de Sistema Operativo y Dependencias
* **Error de MAVLink / Incompatibilidad de Versión:**
  * *Solución:* Asegúrate de tener instalada la versión validada ejecutando `pip install --upgrade "pymavlink>=2.4.50"`.
* **Conflictos de Rutas (`simulation` vs `simulacion`):**
  * *Solución:* Restaura el estado limpio con `git reset --hard origin/main` y `git clean -fd`.

### B. Errores de Hardware y Sensores (Pre-Vuelo)
* **Alerta de Voltaje Anómalo en GCS:**
  * *Solución:* Verifica con multímetro los bornes de la PDB. El rango operativo va de 40.8 V a 50.4 V.
* **Falla de Posicionamiento RTK (`GPS Glitch`):**
  * *Solución:* Comprueba la tasa de refresco y asegúrate de que el enlace de telemetría auxiliar transmita tramas RTCM.

----

## 4. Protocolo de Pruebas y Verificación Final
1. **Pruebas Automatizadas:** Ejecuta `pytest` (debe retornar 100% en verde / 8 de 8 pruebas exitosas).
2. **Simulación de Fallas y HIL:** Ejecuta `python simulacion/simulacion_hil_fallas.py` para validar geocercas y pérdida de enlace.

# MEMORIA TÉCNICA DE INVESTIGACIÓN Y DESARROLLO — STR-002 H3 v3.0
**PERLACOLABS — ELECTRÓNICA PERLACO**  
**Autor e Inventor Principal:** Angel Imer Lara Colorado — *Úrsulo Galván, Veracruz, México*

---

## 📱 1. Hito de Ingeniería Edge & Móvil (Samsung Galaxy SM-A04 + Cloud Pipeline)

El desarrollo integral de la ingeniería, simulación física, generación vectorial CAD, arquitectura de firmware Lua y validación de parámetros del octocóptero agrícola **ELECTRÓNICA PERLACO STR-002 H3 v3.0** ($MTOW \approx 28.5 - 29.5\text{ kg}$) fue ejecutado de manera **100% cloud-native utilizando exclusivamente un smartphone Samsung Galaxy A04 (SM-A04)** acoplado al entorno de cómputo en la nube **Google Colab** y la API REST de **GitHub**.

### 📊 Análisis de Discrepancias, Desafíos y Fortalezas del Entorno

| Dimensión | Fortalezas del Método Móvil / Cloud | Discrepancias y Desafíos Superados |
| :--- | :--- | :--- |
| **Entorno de Cómputo** | Independencia total de PC física local; procesamiento en servidores remotos Google Colab con Python 3, NumPy, Matplotlib y ezdxf. | Ausencia de software CAD/CAM convencional (SolidWorks/AutoCAD) por limitaciones de arquitectura ARM móvil. |
| **Generación CAD / CAM** | Creación de motor vectorial en Python (`ezdxf`) para generar archivos DXF limpios para corte por CNC de placas CFRP 3.0 mm. | Inexistencia de interfaz gráfica interactiva; todo el diseño espacial se calculó mediante trigonometría explícita en código. |
| **Gestión de Código y Git** | Automatización total mediante scripts de sincronización forzada usando Git y GitHub API (commits, releases, badges y Zenodo). | Gestión de pantalla pequeña (Smartphone UI), requiriendo atención extrema en la sintaxis de código para evitar errores de compilación. |
| **Validación y Pruebas** | Modelado numérico avanzado (FFT Notch, $Z_{CG}$, sag de voltaje $12\text{S}$, respuesta anti-goteo) en tiempo real. | Depuración gráfica indirecta mediante la renderización de paneles PNG de alta resolución exportados e inspeccionados en dispositivo. |

---

## 🛠️ 2. Bitácora Histórica de Errores y Soluciones de Ingeniería

Durante las fases de modelado y configuración de la aviónica, se diagnosticaron y resolvieron 4 discrepancias críticas:

### Error 1: Normalización de Ganancias PID de Actitud (ArduPilot Heavy-Lift)
* **Error:** El modelo matemático de control continuo arrojaba valores teóricos descalibrados ($P = 17.27$, $D = 2.03$), los cuales, al ser introducidos en ArduPilot sin escala, causarían oscilación destructiva al despegue.
* **Solución:** Se realizó la conversión al rango adimensional normalizado oficial de ArduCopter 4.2+, ajustando las ganancias a **`ATC_RAT_PIT_P` = 0.0850** y **`ATC_RAT_PIT_D` = 0.0035**, asegurando la estabilidad del octocóptero de $29\text{ kg}$.

### Error 2: Interpolación de Cadenas en Python (f-strings vs LaTeX)
* **Error:** Interrupción del script por `NameError: name 'CG' is not defined` provocado al intentar formatear cadenas de texto conteniendo sintaxis de LaTeX como `$Z_{CG}$`.
* **Solución:** Se aislaron las cadenas de documentación asignándolas como cadenas crudas (`r'...'`) para prevenir la interpolación de variables involuntaria.

### Error 3: Incompatibilidad de Métodos de Objetos Axes en Matplotlib
* **Error:** `AttributeError: 'Axes' object has no attribute 'gca'` al intentar invertir el eje $X$ en subgráficas duales.
* **Solución:** Se invocó el método de inversión directamente sobre el objeto hijo: `ax1.invert_xaxis()`.

### Error 4: Referencia de Espacio de Nombres Trigonométricos en Librería DXF
* **Error:** `AttributeError: module 'ezdxf.math' has no attribute 'radians'`.
* **Solución:** Se migró el procesamiento angular al módulo nativo de Python (`import math`), utilizando `math.radians()`, `math.cos()` y `math.sin()`.

---

## 📐 3. Resumen de Especificaciones de Ingeniería Integradas

* **Estructura y Chasis:** Octocóptero Coaxial X8 en Fibra de Carbono 3K (3.0 mm) + Abrazaderas H3 de Aluminio Anodizado 7075-T6 ($\varnothing 50\text{ mm}$, Torque $3.2\text{ Nm}$).
* **Motopropulsión:** 8x T-Motor P80 III KV120 + ESC T-Motor Alpha 80A HV + Hélices plegables de $30\times 10.5''$ (Empuje total disponible: $73.6\text{ kg}$, Ratio Empuje/Peso nominal: $2.53:1$).
* **Aviónica y Navegación:** Cube Orange+ (STM32H7) + RTK Dual u-Blox ZED-F9P (*Moving Baseline* para rumbo sin interferencia magnética) + Radar FMCW de $77\text{ GHz}$.
* **Hidráulica VRA y Anti-Goteo:** Estanque HDPE de $10.0\text{ L}$ con rompeolas + Caudalímetro YF-S201 ($450\text{ p/L}$) + 4x Electroválvulas NC de $24\text{V}$ en puntas (Latencia de corte $< 35\text{ ms}$ al volar a $< 1.0\text{ km/h}$).
* **Sistema Energético 12S LiPo:** Paquete $12\text{S}\ 30,000\text{ mAh}$ ($50.4\text{ V}$ pico) con conectores QS8-S Anti-Spark ($R_{precarga} = 5.1\ \Omega$), monitoreo individual por BMS CAN y límite de descarga segura a $43.2\text{ V}$ ($80\%$ DoD).

---

## 📁 4. Índice del Expediente Completo en el Repositorio

1. **`/firmware` (14 Archivos):** Parámetros maestros, PID normalizado, scripts Lua (VRA, BMS 12S, Control de Presión, Radar 77 GHz, LEDs Neopixel), Evasión 3D, Geofensa, perfiles ZED-F9P RTK, EdgeTX, ESC Alpha 80A y MAVLink 4G.
2. **`/cad`:** Generador `generar_chasis_dxf.py` y plano CNC `chasis_central_cfrp_3mm_str002_h3.dxf`.
3. **`/mission`:** Generador `generar_mision_qgc.py` y ruta WPL 110 (`mision_agricola_str002_h3.waypoints`).
4. **`/simulation`:** Analizadores de logs DataFlash (`analizador_logs_vuelo.py`), auditoría de código (`auditar_repositorio.py`) y simulador electroquímico $12\text{S}$ (`simulador_baterias_12s.py`).
5. **`/docs`:** Protocolo de prueba de banco (`protocolo_prueba_banco.md`), Manual de campo con Checklist (`manual_operacion_campo.md`), Plan de Mantenimiento Preventivo (`plan_mantenimiento_preventivo.md`) y Memoria Técnica PERLACOLABS (`bitacora_investigacion_perlacolabs.md`).
6. **`/assets`:** 6 infografías HD integradas al `README.md`.

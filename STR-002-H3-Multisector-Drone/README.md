🚁 ELECTRÓNICA PERLACO — STR-002 H3 (v2.5 / v3.0)
Gemelo Digital y Simulación de Misión para Dron Agrícola (MTOW 55.0 kg - 60.0 kg)

Repositorio oficial de ingeniería para el diseño, modelado físico, simulación dinámica y validación de aviónica del octocóptero agrícola STR-002 H3. Este proyecto prioriza la precisión técnica basada estrictamente en principios de aerodinámica, electromagnetismo y termodinámica, sin especulaciones.

Centro Regional de Operaciones: Veracruz, México  
Plataforma Tecnológica: ELECTRÓNICA PERLACO  
Estado del Repositorio: Sincronizado, Operativo y Monitoreado mediante Gemelo Digital.

---

## 🇲🇽 Despliegue Geoestratégico y de Inversión
* **País:** México
* **Centro de Ensayos y Campo:** Estado de Veracruz
* **Beneficio Operativo:** Ahorro estimado del 48.5% en costos operativos comparado con la agricultura tradicional por tractor o mochila aspersora.

---

## 📊 Panel de Control y Subsistemas Clave
| Subsistema Clave | Componente / Algoritmo | Estado Operativo | Parámetro Crítico / Límite |
| :--- | :--- | :--- | :--- |
| **1. Dinámica Atmosférica** | Simulación de Viento Racheado | Óptimo | 3.0 a 13.0 m/s |
| **2. Estructura & Fatiga** | Abrazaderas de Aluminio 7075-T6 | Conforme | ~120 MPa (Límite: 503 MPa) |
| **3. Aviónica & Posicionamiento** | Quad-GNSS + SBAS (Redundancia) | Seguro | Deriva < 0.75 cm (RTK < 2 cm) |
| **4. Inteligencia Artificial** | Inferencia YOLOv8 Edge AI | Activo | Precisión 91% - 97% |
| **5. Aprendizaje por Refuerzo** | Q-Learning Optimizador de Rutas | Convergente | Minimización efectiva de solape |

---

## 📋 Arquitectura y Especificaciones Físicas del Sistema
* **Modelo:** ELECTRÓNICA PERLACO STR-002 H3
* **Configuración:** Octocóptero (8 motores coaxiales / extrotores)
* **Peso Seco (Chasis + Aviónica):** 30.0 kg
* **Capacidad Máxima de Líquido:** 25.0 kg
* **Peso Máximo al Despegue (MTOW):** 60.0 kg
* **Sistema de Acumulación:** Batería inteligente configurada en **18S (66.6 V nominales, 30.0 Ah)**.
* **Propulsión e Hidráulica:** Hélices de 30 pulgadas, motores con constante $Kv = 120\text{ RPM/V}$ y sistema de aspersión CDA.

---

## 🚀 Resultados de Misión Optimizada (Simulación Dinámica)
*(Evaluado bajo un margen estricto de seguridad del 85% de capacidad útil de descarga: 25.50 Ah)*

| Parámetro de Ingeniería | Valor Validado |
| :--- | :--- |
| **Tiempo Máximo de Misión Seguro** | 8.20 minutos |
| **Consumo Total de Batería** | 25.62 Ah |
| **Corriente Promedio de Operación** | 186.04 A |
| **Corriente Máxima (Despegue / Tanque Lleno)** | 187.64 A |
| **Voltaje Terminal Inicial (Bajo Carga)** | 63.36 V |
| **Voltaje Terminal Final (Bajo Carga)** | 63.27 V |

---

## 🌡️ Modelo Térmico y Gestión del Pack 18S
* **Modelo Aplicado:** Disipación por efecto Joule frente al enfriamiento por convección forzada debida al flujo de aire descendente (*downwash*) de las 8 hélices principales.
* **Evolución Térmica de Celdas:**
  * Temperatura Inicial: $28.53\,^\circ\text{C}$
  * Temperatura Promedio: $54.85\,^\circ\text{C}$
  * Temperatura Máxima Final: $49.66\,^\circ\text{C}$ (Cumpliendo con el umbral operativo seguro por debajo de $60\,^\circ\text{C}$).

---

## ⚙️ Actualización Avanzada: Mecánica de Acoplamiento y Simulación en Tiempo Real
* **Pernos de Bloqueo Cónico ($60^\circ$):** Geometría optimizada con tolerancia H7/g6 en aleación de Titanio Grado 5 y Aluminio 7075-T6, asegurando estanqueidad ($2970.84\text{ mm}^3$) y sistema *Fail-Safe* por resorte.
* **Simulación en Tiempo Real (APIs en Vivo):** Conexión integrada con servicios meteorológicos (OpenWeather) y constelaciones GNSS/RTK centimétricas.
* **Inteligencia Artificial (YOLO Edge):** Módulo de autoaprendizaje en el borde para mitigación de errores en el primer vuelo y control PID dinámico ante ráfagas de viento.

---

## 📁 Estructura del Repositorio y Entregables
* `docs/RESUMEN_TECNICO_STR002.md`: Documentación formal de ingeniería del gemelo digital.
* `docs/BOM_ampliada_STR002.md`: Lista de materiales ampliada con opciones de alta gama.
* `docs/estudio_ventajas_nuevos_elementos.md`: Estudio técnico de los nuevos elementos (Titanio, QS8-S, etc.).
* `simulation/simulacion_mision_completa_str002.csv`: Conjunto de datos temporal sincronizado.
* `cad/perno_bloqueo_conico_60deg.stl`: Modelo 3D estanco del perno cónico.

---

## 🚀 Pautas Operativas para el Piloto
1. **Límite de Tiempo Estricto:** Retornar a base o iniciar descenso antes de los 8.20 minutos de vuelo.
2. **Control de Despegue:** Accionar el acelerador de forma progresiva con el MTOW de 60.0 kg para mitigar picos transitorios de corriente.
3. **Inspección Post-Vuelo:** Verificar el estado térmico del pack 18S; si se registran temperaturas superiores a $60\,^\circ\text{C}$, suspender vuelos consecutivos.

---

## 🖤 Dedicatoria y Agradecimientos
Este proyecto de ingeniería y prototipo del dron agrícola **ELECTRÓNICA PERLACO — STR-002 H3 v3.0** representa dedicación, resiliencia y constante evolución técnica. No habría sido posible sin las personas que han marcado mi camino:

* **A mi Padre:** Técnico, de quien heredé la pasión por desarmar el mundo, entender cómo funciona y volverlo a construir. Gracias por ser mi primera escuela de ingeniería.
* **A mi Madre:** Por su firmeza inquebrantable. De ella aprendí el carácter, la disciplina y la fuerza para no rendirme jamás frente a la adversidad.
* **A mi Hermana:** Por estar siempre a mi lado, brindándome su apoyo incondicional en cada etapa de este recorrido.
* **A mis Amigos:** Por respaldarme, confiar en mis ideas y acompañarme en las jornadas de desarrollo.
* **A quienes confiaron en mí sus aparatos (y que alguna vez descompuse):** Gracias por la paciencia y por brindarme el campo de pruebas real donde aprendí a reparar, innovar y perfeccionar mis conocimientos.
* **A mis detractores y a quienes me desearon lo peor:** Sus dudas y críticas fueron el combustible perfecto para autoexigirme más, pulir cada detalle técnico y demostrar con hechos, ciencia y simulación de lo que soy capaz.
* **🏡 A los de la casita xD y mis medios hermanos:** Gracias por estar siempre, por la compañía y las risas.
* **🙏 A mis hermanos de Fe en Cristo:** De corazón, muchas gracias por sus oraciones constantes y su cariño genuino.
* **❤️ A toda mi familia:** El pilar fundamental de cada esfuerzo y paso hacia adelante.

> **Xquixhe pe’ guiraatu’ !!!!**  
> *Ese no es el último XD, continuará...*

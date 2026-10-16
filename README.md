# 🚁 STR-002 H3 v3.0 — Sistema de Dron Agrícola de Alta Potencia (60 kg MTOW)

> **Centro Regional de Operaciones:** Veracruz, México  
> **Plataforma Tecnológica:** ELECTRÓNICA PERLACO  
> **Estado del Repositorio:** Sincronizado, Operativo y Monitoreado mediante Gemelo Digital.

Repositorio oficial de ingeniería para el diseño, modelado físico, simulación dinámica y validación de aviónica del octocóptero agrícola STR-002 H3. Este proyecto prioriza la precisión técnica basada estrictamente en principios de aerodinámica, electromagnetismo y termodinámica.

---

## 🇲🇽 Despliegue Geoestratégico y de Inversión
* **País:** México
* **Centro de Ensayos y Campo:** Estado de Veracruz
* **Beneficio Operativo:** Ahorro estimado del **48.5%** en costos operativos comparado con la agricultura tradicional por tractor o mochila aspersora.
* **Dashboard Gráfico Principal:** Disponible en la ruta [`docs/gemelo_digital_operacion/dashboard_gemelo_digital_master.png`](docs/gemelo_digital_operacion/dashboard_gemelo_digital_master.png).

---

## 📊 Panel de Control y Telemetría Multiárea en Tiempo Real

A continuación se detallan los módulos críticos del gemelo digital, integrando visión artificial, redes neuronales y análisis estructural bajo condiciones reales de operación:

| Subsistema Clave | Componente / Algoritmo | Estado Operativo | Parámetro Crítico / Límite | Evidencia / Gráfica en Repo |
| :--- | :--- | :--- | :--- | :--- |
| **1. Dinámica Atmosférica** | Simulación de Viento Racheado | Óptimo | 3.0 a 13.0 m/s | `docs/gemelo_digital_operacion/dashboard_gemelo_digital_master.png` |
| **2. Estructura & Fatiga** | Abrazaderas de Aluminio 7075-T6 | Conforme | ~120 MPa (Límite: 503 MPa) | `docs/gemelo_digital_operacion/dashboard_gemelo_digital_master.png` |
| **3. Aviónica & Posicionamiento**| Quad-GNSS + SBAS (Redundancia) | Seguro | Deriva < 0.75 cm (RTK < 2 cm) | `avionica/logs/reporte_fdir_gnss.json` |
| **4. Inteligencia Artificial** | Inferencia YOLOv8 Edge AI | Activo | Precisión 91% - 97% | `docs/gemelo_digital_operacion/dashboard_gemelo_digital_master.png` |
| **5. Aprendizaje por Refuerzo** | Q-Learning Optimizador de Rutas | Convergente | Minimización efectiva de solape | `ai/logs/reporte_rl_optimizacion.json` |

---

## 📋 Arquitectura y Especificaciones Físicas del Sistema
* **Modelo:** ELECTRÓNICA PERLACO STR-002 H3 v3.0
* **Configuración:** Octocóptero (8 extrotores)
* **Peso Seco (Chasis + Aviónica):** 30.0 kg
* **Capacidad Máxima de Líquido:** 25.0 kg
* **Peso Máximo al Despegue (MTOW):** 60.0 kg
* **Sistema de Acumulación:** Batería inteligente configurada en 18S (66.6 V nominales, 30.0 Ah).
* **Propulsión e Hidráulica:** Hélices de 30 pulgadas, motores brushless y sistema de aspersión CDA.

---

## 🚀 Resultados de Misión Optimizada (Simulación Dinámica)
* **Tiempo Máximo de Misión Seguro:** 8.20 minutos
* **Corriente Promedio de Operación:** 186.04 A
* **Voltaje Terminal Nominal:** 63.36 V
* **Modelo Térmico:** Disipación por efecto Joule frente al flujo de aire descendente (*downwash*), manteniendo las celdas por debajo de 50 °C.

---

## 📁 Estructura del Repositorio
* `docs/gemelo_digital_operacion/dashboard_gemelo_digital_master.png`: Dashboard gráfico industrial en tiempo real.
* `digital_twin/logs/reporte_operacion_gemelo.json`: Registros estructurados del gemelo digital.
* `digital_twin/logs/reporte_diagnostico_inteligente.json`: Métricas de YOLOv8, redes neuronales y fatiga mecánica.
* `ai/`: Módulos de optimización y aprendizaje por refuerzo.
* `avionica/`: Subsistemas FDIR y Quad-GNSS + SBAS.

---

## 🖤 Dedicatoria y Agradecimientos
Este proyecto de ingeniería y prototipo del dron agrícola ELECTRÓNICA PERLACO STR-002 H3 v3.0 representa dedicación, resiliencia y constante evolución técnica. No habría sido posible sin las personas que han marcado mi camino:
* **A mi Padre:** Técnico, de quien heredé la pasión por desarmar el mundo, entender cómo funciona y volverlo a construir. Gracias por ser mi primera escuela de ingeniería.
* **A mi Madre:** Por su firmeza inquebrantable. De ella aprendí el carácter, la disciplina y la fuerza para no rendirme jamás frente a la adversidad.
* **A mi Hermana:** Por estar siempre a mi lado, brindándome su apoyo incondicional en cada etapa de este recorrido.
* **A mis Amigos:** Por respaldarme, confiar en mis ideas y acompañarme en las jornadas de desarrollo.
* **A quienes confiaron en mí sus aparatos (y que alguna vez descompuse):** Gracias por la paciencia y por brindarme el campo de pruebas real donde aprendí a reparar, innovar y perfeccionar mis conocimientos.
* **A mis detractores y a quienes me desearon lo peor:** Sus dudas y críticas fueron el combustible perfecto para autoexigirme más, pulir cada detalle técnico y demostrar con hechos, ciencia y simulación de lo que soy capaz.
* **A los de la casita xD y mis medios hermanos:** Gracias por estar siempre, por la compañía y las risas.
* **A mis hermanos de Fe en Cristo:** Por sus oraciones constantes y su cariño genuino.
* **A toda mi familia:** El pilar fundamental de cada esfuerzo y paso hacia adelante.

> *Xquixhe pe’ guiraatu’ !!!!*  
> *Ese no es el último XD, continuará...*

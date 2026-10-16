# ELECTRÓNICA PERLACO — STR-002 H3 (v2.5 / v3.0)
**Gemelo Digital y Simulación de Misión para Dron Agrícola (MTOW 55.0 kg - 60.0 kg)**

Repositorio oficial de ingeniería para el diseño, modelado físico, simulación dinámica y validación de aviónica del octocóptero agrícola STR-002 H3. Este proyecto prioriza la precisión técnica basada estrictamente en principios de aerodinámica, electromagnetismo y termodinámica, sin especulaciones.

---

## 📋 1. Arquitectura y Especificaciones Físicas del Sistema
* **Modelo:** ELECTRÓNICA PERLACO STR-002 H3
* **Configuración:** Octocóptero (8 extrotores)
* **Peso Seco (Chasis + Aviónica):** 30.0 kg
* **Capacidad Máxima de Líquido:** 25.0 kg
* **Peso Máximo al Despegue (MTOW Inicial):** 55.0 kg
* **Sistema de Acumulación:** Batería inteligente configurada en 18S (66.6 V nominales, 30.0 Ah, resistencia interna $R_{int} = 18.0\text{ m}\Omega$).
* **Propulsión e Hidráulica:** Hélices de 30 pulgadas, motores con constante $K_v = 120\text{ RPM/V}$ y sistema de aspersión CDA con demanda estimada de 350 W.

---

## 📊 2. Resultados de Misión Optimizada (Simulación Dinámica)
Evaluado bajo un margen estricto de seguridad del 85% de capacidad útil de descarga (25.50 Ah):

| Parámetro de Ingeniería | Valor Validado |
| :--- | :--- |
| **Tiempo Máximo de Misión Seguro** | 8.20 minutos |
| **Consumo Total de Batería** | 25.62 Ah |
| **Corriente Promedio de Operación** | 186.04 A |
| **Corriente Máxima (Despegue / Tanque Lleno)** | 187.64 A |
| **Corriente Mínima (Aterrizaje / Tanque Vacío)** | 184.43 A |
| **Voltaje Terminal Inicial (Bajo Carga)** | 63.36 V |
| **Voltaje Terminal Final (Bajo Carga)** | 63.27 V |
| **Caída de Tensión Máxima ($V_{drop}$)** | 3.38 V |

---

## 🌡️ 3. Modelo Térmico y Gestión del Pack 18S
* **Modelo Aplicado:** Disipación por efecto Joule ($P_{loss} = I^2 \cdot R_{int}$) frente al enfriamiento por convección forzada debida al flujo de aire descendente (*downwash*) de las 8 hélices principales.
* **Coeficiente de Convección Optimizado:** Configurado a $28\text{ W/K}$ mediante la implementación de ductos de ventilación directa y aletas disipadoras en el chasis.
* **Evolución Térmica de Celdas:**
  * **Temperatura Inicial:** 28.53 °C
  * **Temperatura Promedio:** 54.85 °C
  * **Temperatura Máxima Final:** 49.66 °C *(Cumpliendo holgadamente con el umbral operativo seguro al mantenerse por debajo del límite crítico de 60 °C)*.

---

## 📁 4. Estructura del Repositorio y Entregables
* `docs/RESUMEN_TECNICO_STR002.md`: Documentación formal de ingeniería del gemelo digital.
* `simulation/simulacion_mision_completa_str002.csv`: Conjunto de datos temporal sincronizado con registros de tiempo, peso, corriente total, voltaje terminal, RPM de rotores y temperatura de celdas.

---

## 🚀 5. Pautas Operativas para el Piloto
1. **Límite de Tiempo Estricto:** Retornar a base o iniciar descenso antes de los 8.20 minutos de vuelo.
2. **Control de Despegue:** Accionar el acelerador de forma progresiva con el MTOW de 55.0 kg para mitigar picos transitorios de corriente.
3. **Inspección Post-Vuelo:** Verificar el estado térmico del pack 18S; si se registran temperaturas superiores a 60 °C, suspender vuelos consecutivos hasta el enfriamiento natural.

---

## 🖤 Dedicatoria y Agradecimientos

Este proyecto de ingeniería y prototipo del dron agrícola ELECTRÓNICA PERLACO STR-002 H3 v3.0 representa años de aprendizaje, resiliencia y constante evolución técnica. No habría sido posible sin las personas que han marcado mi camino:

* **A mi Padre:** Técnico con años de experiencia, de quien heredé la pasión por desarmar el mundo, entender cómo funciona y volverlo a construir. Gracias por ser mi primera escuela de ingeniería.
* **A mi Madre:** Por su firmeza inquebrantable. De ella aprendí el carácter, la disciplina y la fuerza para no rendirme jamás frente a la adversidad.
* **A mi Hermana:** Por estar siempre a mi lado, brindándome su apoyo incondicional en cada etapa de este recorrido.
* **A mis Amigos:** Por respaldarme, confiar en mis ideas y acompañarme en las largas jornadas de desarrollo.
* **A quienes confiaron en mí sus aparatos (y que alguna vez descompuse):** Gracias por la paciencia y por brindarme el campo de pruebas real donde aprendí a reparar, innovar y perfeccionar mis conocimientos.
* **A mis detractores y a quienes me desearon lo peor:** A aquellos que lo hicieron con educación y elegancia, les agradezco infinitamente. Sus dudas y críticas fueron el combustible perfecto para autoexigirme más, pulir cada detalle técnico y demostrar con hechos, ciencia y simulación de lo que soy capaz.

---

# ELECTRÓNICA PERLACO — STR-002 H3 (v2.5 / v3.0)
## Gemelo Digital y Simulación de Misión para Dron Agrícola (MTOW 55.0 kg - 60.0 kg)

Repositorio oficial de ingeniería para el diseño, modelado físico, simulación dinámica y validación de aviónica del octocóptero agrícola **STR-002 H3**. Este proyecto prioriza la precisión técnica basada estrictamente en principios de aerodinámica, electromagnetismo y termodinámica, sin especulaciones.

---

### 📋 1. Arquitectura y Especificaciones Físicas del Sistema
* **Modelo:** ELECTRÓNICA PERLACO STR-002 H3
* **Configuración:** Octocóptero ($8	ext{ rotores}$)
* **Peso Seco (Chasis + Aviónica):** $30.0	ext{ kg}$
* **Capacidad Máxima de Líquido:** $25.0	ext{ kg}$
* **Peso Máximo al Despegue (MTOW Inicial):** $55.0	ext{ kg}$
* **Sistema de Acumulación:** Batería inteligente configurada en **18S** ($66.6	ext{ V}$ nominales, $30.0	ext{ Ah}$, resistencia interna $R_{int} = 18.0	ext{ m}\Omega$).
* **Propulsión e Hidráulica:** Hélices de $30	ext{ pulgadas}$, motores con constante $K_v = 120	ext{ RPM/V}$ y sistema de aspersión CDA con demanda estimada de $350	ext{ W}$.

---

### 📊 2. Resultados de Misión Optimizada (Simulación Dinámica)
Evaluado bajo un margen estricto de seguridad del 85% de capacidad útil de descarga ($25.50	ext{ Ah}$):

| Parámetro de Ingeniería | Valor Validado |
| :--- | :--- |
| **Tiempo Máximo de Misión Seguro** | **$8.20	ext{ minutos}$** |
| **Consumo Total de Batería** | $25.62	ext{ Ah}$ |
| **Corriente Promedio de Operación** | $186.04	ext{ A}$ |
| **Corriente Máxima (Despegue / Tanque Lleno)** | $187.64	ext{ A}$ |
| **Corriente Mínima (Aterrizaje / Tanque Vacío)** | $184.43	ext{ A}$ |
| **Voltaje Terminal Inicial (Bajo Carga)** | $63.36	ext{ V}$ |
| **Voltaje Terminal Final (Bajo Carga)** | $63.27	ext{ V}$ |
| **Caída de Tensión Máxima ($V_{drop}$)** | $3.38	ext{ V}$ |

---

### 🌡️ 3. Modelo Térmico y Gestión del Pack 18S
* **Modelo Aplicado:** Disipación por efecto Joule ($P_{loss} = I^2 \cdot R_{int}$) frente al enfriamiento por convección forzada debida al flujo de aire descendente (*downwash*) de las 8 hélices principales.
* **Coeficiente de Convección Optimizado:** Configurado a **$28	ext{ W/K}$** mediante la implementación de ductos de ventilación directa y aletas disipadoras en el chasis.
* **Evolución Térmica de Celdas:**
  * *Temperatura Inicial:* $28.53	ext{ °C}$
  * *Temperatura Promedio:* $54.85	ext{ °C}$
  * *Temperatura Máxima Final:* **$49.66	ext{ °C}$** (Cumpliendo holgadamente con el umbral operativo seguro al mantenerse por debajo del límite crítico de $60	ext{ °C}$).

---

### 📁 4. Estructura del Repositorio y Entregables
* `docs/RESUMEN_TECNICO_STR002.md`: Documentación formal de ingeniería del gemelo digital.
* `str002_mision_completa_simulacion.csv`: Dataset temporal sincronizado con registros de tiempo, peso, corriente total, voltaje terminal, RPM de rotores y temperatura de celdas.

---

### 🚀 5. Pautas Operativas para el Piloto
1. **Límite de Tiempo Estricto:** Retornar a base o iniciar descenso antes de los **8.20 minutos** de vuelo.
2. **Control de Despegue:** Accionar el acelerador de forma progresiva con el MTOW de $55.0	ext{ kg}$ para mitigar picos transitorios de corriente.
3. **Inspección Post-Vuelo:** Verificar el estado térmico del pack 18S; si se registran temperaturas superiores a $60	ext{ °C}$, suspender vuelos consecutivos hasta el enfriamiento natural.

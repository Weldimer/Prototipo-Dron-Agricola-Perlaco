# 🌾 Estudio Comparativo: Planificación de Rutas ArduPilot, Evasión y Módulo Dual

**ELECTRÓNICA PERLACO — STR-002 H3 v3.5** | *Análisis de Eficiencia Operativa y Automatización*  
**Autor:** Angel Imer Lara Colorado / **PERLACOLABS** — *Úrsulo Galván, Veracruz, México*

---

## 🚁 1. Validación de la Pila ArduPilot + Mission Planner
Tomando como marco de referencia el estudio agronómico de la ESPOL (Colcha & Tumbaco, 2019):

* **Autonomía y Precisión Boustrophedon:** Validación de la estabilidad de vuelo autónomo a baja altura (**2.0 m sobre el dosel**) a velocidades constantes de **4.0 a 5.5 m/s**.
* **Mitigación de Riesgo Humano:** Eliminación del riesgo de intoxicación por agroquímicos en operadores al automatizar el 100 % de la trayectoria de aspersión.
* **Evasión Dinámica de Obstáculos:** Habilidad de esquivar postes y árboles en los lindantes de las parcelas sin perder la referencia geodésica del plan de vuelo, retomando la línea de aspersión gracias al sistema **RTK Moving Baseline (±8-12 mm RMS)**.

---

## 📊 2. Benchmarking de Cobertura Agrónoma
* **Línea Base Arroz (Dron Cuatrorotor Small):** Cobertura promedio de $1.52\text{ ha}$ por batería de 20 min ($4.56\text{ ha/h}$).
* **Plataforma Cañera STR-002 H3 v3.5 (Octocóptero X8 Heavy):** Cobertura extendida de hasta **$14.5\text{ ha}$ por parcela** debido al ancho de franja de **6.0 m**, velocidad de **5.5 m/s** y caudal regulado por el bucle cerrado **PWM / Filtro de Kalman 1D**.

---

## 🔄 3. Versatilidad Dual (Líquidos VRA & Sólidos Granulados)
* La arquitectura del STR-002 permite el desacoplamiento rápido del sistema hidráulico CDA mediante los racores **CPC PLC Series** para integrar el distribuidor rotativo de sólidos granulados en la fase de brote vegetativo (*Plantilla*).

---
**ELECTRÓNICA PERLACO / PERLACOLABS** — *Automatización Agrícola Autónomas.*

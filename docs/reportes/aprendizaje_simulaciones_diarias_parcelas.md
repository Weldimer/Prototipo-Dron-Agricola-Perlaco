# APRENDIZAJE Y JUSTIFICACIÓN DE SIMULACIONES DIARIAS EN DIFERENTES PARCELAS — STR-002 H3 v3.0
**PERLACOLABS — ELECTRÓNICA PERLACO**  
**Autor e Inventor Principal:** Angel Imer Lara Colorado — *Úrsulo Galván, Veracruz, México*

---

## 🎯 1. ¿Por Qué son Necesarias las Simulaciones Diarias Automatizadas?

El prototipo **ELECTRÓNICA PERLACO — STR-002 H3 v3.0** opera en entornos microclimáticos cambiantes e hiperlocales en el estado de Veracruz. La ejecución autómata de simulaciones diarias (2x/día vía GitHub Actions Cron) responde a cuatro pilares fundamentales de ingeniería y agronomía de precisión:

1. **Aprendizaje Terrestre y Mapeo Microclimático Continuo:**
   * Las condiciones de viento racheado de los 'Nortes' (>127 km/h), temperatura, humedad relativa y radiación solar varían drásticamente entre zonas. Evaluar diariamente parcelas de **Caña de Azúcar** (Úrsulo Galván) y **Cítricos** (Paso de Ovejas / Actopan) entrena los modelos numéricos en lazo cerrado sin arriesgar la aeronave física.
2. **Calibración Dinámica de la Dosis VRA y Espectro de Gota (VMD):**
   * La tasa de aplicación de la 'sopa' (herbicidas, fungicidas, bioestimulantes) y el tamaño de gota del atomizador centrífugo CDA ($180 - 280\ \mu\text{m}$) se ajustan dinámicamente según el Índice de Evaporación Delta-T ($\Delta T$) y la deriva eólica para evitar pérdidas por evaporación.
3. **Evaluación de Inmunidad Electromagnética (EMI) y Batería 12S:**
   * Mide el comportamiento de la corriente continua ($>300\text{ A}$) e inducción magnética ($\mu\text{T}$) sobre la línea de potencia $12\text{S}$, validando la estabilidad del rumbo por **Doble GNSS Moving Baseline RTK** (sin brújula) frente a la salinidad del suelo y la carga aerodinámica.
4. **Acumulación de Base de Datos de Telemetría (Big Data Agrícola):**
   * Almacena históricamente los registros en `simulation/historical_learning_log.csv`, refinando el factor adaptativo $K_{\text{VRA}}$ mediante la ingesta en tiempo real de servicios web gratuitos (Open-Meteo y NASA POWER).

---

## 🌾 2. Definición de Parcelas, Variantes de Cultivo y Formulación ('Sopa')

| Parámetro / Variable | Parcela A (Úrsulo Galván, Ver.) | Parcela B (Paso de Ovejas / Actopan, Ver.) |
| :--- | :--- | :--- |
| **Cultivo y Variante** | Caña de Azúcar (*CP 72-2086 / Caña Maura*) | Cítricos (*Limón Persa Injertado*) |
| **Superficie** | $12.5\text{ ha}$ | $8.2\text{ ha}$ |
| **Formulación ('Sopa')** | Herbicida Nicosulfurón + Coadyuvante Siliconado | Fungicida Foliar + Bioestimulante Zn-B + Buffer pH |
| **Conductividad Eléctrica (CE)**| $1.8\text{ dS/m}$ (Salinidad Moderada) | $2.4\text{ dS/m}$ (Salinidad Elevada) |
| **Altura de Canopia Densa**| $2.80\text{ m}$ (Dosel cerrado) | $1.90\text{ m}$ (Arbolado denso) |

---

## 📐 3. Ecuaciones Físicas y Dinámica del Vuelo

* **Diámetro de Gota Volumétrico (VMD µm - Atomizador CDA):**
$$VMD = \begin{cases} 280\ \mu\text{m} & \text{si } V_{\text{viento}} > 4.0\text{ m/s} \text{ o } \Delta T > 8.0^\circ\text{C} \quad (\text{Anti-Deriva}) \\ 180\ \mu\text{m} & \text{en condiciones estables} \quad (\text{Alta Cobertura Foliar}) \end{cases}$$

* **Volumen Total de Sopa Requerido (L):**
$$V_{\text{total}}(\text{L}) = \text{Superficie}(\text{ha}) \times \left[ \text{Dosis}_{\text{nominal}} \times K_{\text{VRA}} \right]$$

* **Inducción Magnética Parásita 12S:**
$$B_{\text{inducido}}(\mu\text{T}) = 0.42 \times I_{12\text{S}}(\text{A})$$

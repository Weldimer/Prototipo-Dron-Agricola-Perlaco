# ESTADO TÉCNICO Y DOCUMENTAL — FASE 3
## DRON AGRÍCOLA ELECTRÓNICA PERLACO STR-002 H3 (MTOW 60 kg)

* **Documento P-11:** VERIFICADO / CERRADO (Alineado con Gemelo Digital 18S)
* **Documento P-12:** VERIFICADO / ACTUALIZADO
* **BOM (Lista de Materiales):** LIBERADO PARA FASE DE BANCO (TRL 5)

---

### 1. Condiciones de Contorno Comunes (Arquitectura Eléctrica Unificada)
* **Paquete de Batería Principal:** Sistema inteligente en configuración **18S**.
* **Tensión Nominal del Pack:** $66.6\text{ V}$ (Tensión máxima de carga completa: $75.6\text{ V}$).
* **Capacidad Útil / Nominal:** $30.0\text{ Ah}$ (con límite estricto de descarga al 85% = $25.5\text{ Ah}$).
* **Energía Nominal Teórica Instalada:** $1,998\text{ Wh}$ ($\approx 2.0\text{ kWh}$ por pack principal).
* **Configuración Propulsora:** 8 motores T-Motor P80 III KV120 con hélices G30×10.5" CF.

### 2. Modelado Analítico de Distribución Energética y Carga
* **Resistencia Interna de Referencia ($R_{int}$):** $18.0\text{ m}\Omega$ a $22.0\text{ m}\Omega$ bajo estrés térmico máximo.
* **Gestión de Corriente y Caída de Tensión ($V_{drop}$):** Validada mediante simulación temporal de misión (Autonomía segura óptima: $8.20\text{ min}$ nominal / $6.85\text{ min}$ bajo estrés extremo a $42\text{ °C}$).

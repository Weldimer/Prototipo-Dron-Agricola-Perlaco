# REPORTE DE SIMULACIÓN TÉCNICA E INTEGRAL DE MISIÓN AGRÍCOLA — STR-002 H3 v3.0
**PERLACOLABS — ELECTRÓNICA PERLACO**  
**Autor e Inventor Principal:** Angel Imer Lara Colorado — *Úrsulo Galván, Veracruz, México*

---

## 🛸 1. Resumen de Ejecución de Vuelo y Telemetría

Se ha ejecutado una simulación física de alta fidelidad para el octocóptero **STR-002 H3 v3.0** ($MTOW \approx 28.5 - 29.5\text{ kg}$), modelando un ciclo operativo completo de $12.0\text{ minutos}$ de asperjado autónomo en parcela:

| Variable Operativa | Valor Inicial / Configuración | Valor Final / Mínimo | Estado de Seguridad |
| :--- | :---: | :---: | :---: |
| **Altitud de Trabajo AGL** | $0.0\text{ m}$ (Rampa de Despegue) | $3.0\text{ m AGL}$ (Radar $77\text{ GHz}$) | Nominal / Estable |
| **Velocidad Groundspeed** | $0.0\text{ km/h}$ | $15.0\text{ km/h}$ (Nominal VRA) | En Rango |
| **Volumen de Estanque HDPE** | $10.0\text{ L}$ ($100\%$) | $0.5\text{ L}$ ($5\%$ Reserva RTL) | Failsafe Exitoso |
| **Tensión de Bus 12S LiPo** | $50.4\text{ V}$ (Pico) | $45.1\text{ V}$ (Con Sag @ $65\text{A}$) | $> 43.2\text{ V}$ Safe |
| **Capacidad SOC Batería** | $100.0\%$ ($30,000\text{ mAh}$) | $58.3\%$ Remanente | Margen de Sobrevuelo OK |

---

## 📊 2. Ecuaciones del Bucle Hidráulico y Energético

### A. Tasa de Inyección Hidráulica VRA ($L/\text{min}$)
$$\text{Caudal}(t) = \left( \frac{v_{\text{groundspeed}}(t)}{15.0\text{ km/h}} \right) \times 0.78\text{ L/min}$$

### B. Caída de Tensión por Resistencia Interna (*Voltage Sag*)
$$V_{\text{bus}}(t) = V_{\text{ocv}}(SOC) - \left( I_{\text{hover}} \times R_i \right) \quad \text{donde } R_i = 24.0\text{ m}\Omega$$

---

## 🖼️ 3. Panel de Resultados y Visualización Gráfica
El archivo numérico detallado ha sido exportado en `simulation/log_telemetria_mision_real.csv` y la infografía HD en `assets/simulacion_mision_agricola_hd.png`.

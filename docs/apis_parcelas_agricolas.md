# CONEXIÓN DE APIS PÚBLICAS Y GESTIÓN DE PARCELAS — STR-002 H3 v3.0
**PERLACOLABS — ELECTRÓNICA PERLACO**  
**Autor e Inventor Principal:** Angel Imer Lara Colorado — *Úrsulo Galván, Veracruz, México*

---

## 🛰️ 1. Fuentes de Datos Agroclimáticos e Imágenes Satelitales Abiertas

El sistema de planificación de misiones de asperjado VRA integra servicios web públicos de acceso gratuito que no requieren hardware físico conectado:

1. **Open-Meteo Agrometeorology API:**
   * **Endpoint:** `https://api.open-meteo.com/v1/forecast`
   * **Parámetros Ingeridos:** Humedad del suelo ($0-1\text{ cm}$), Temperatura superficial y Evapotranspiración de referencia $\text{ET}_0$ FAO-56.
   * **Ubicación Centroide:** $19.4031^\circ\text{ N}, -96.3533^\circ\text{ W}$ (Úrsulo Galván, Veracruz).

2. **NASA POWER API & Copernicus Sentinel STAC:**
   * Proporciona la radiación solar incidente ($\text{ALLSKY\_SWRAD\_DAILY}$) e índices multiespectrales de vegetación (NDVI) para ajustar la tasa de descarga hidráulica ($L/\text{ha}$) a la condición del cultivo.

---

## 📊 2. Algoritmo de Ajuste Dinámico de Dosis VRA

$$\text{Dosis\_Ajustada} = \text{Dosis\_Base}(NDVI) \times \left(1.0 + 0.15 \times \text{ET}_0 - 0.5 \times \text{Humedad\_Suelo}\right)$$

* **Inyección en Tiempo Real:** El valor final calculado se traduce en una consigna MAVLink/PWM que ajusta las 4 electroválvulas NC de $24\text{V}$ y la bomba principal para mantener el rango entre $3.0\text{ L/ha}$ y $15.0\text{ L/ha}$.

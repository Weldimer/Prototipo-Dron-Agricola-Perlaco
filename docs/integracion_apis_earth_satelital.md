# INTEGRACIÓN DE APIS SATELITALES Y GOOGLE EARTH ENGINE — STR-002 H3 v3.0
**PERLACOLABS — ELECTRÓNICA PERLACO**  
**Autor e Inventor Principal:** Angel Imer Lara Colorado — *Úrsulo Galván, Veracruz, México*

---

## 🛰️ 1. Arquitectura de Conexión Earth-to-Drone (Copernicus / Sentinel-2 / Earth Engine)

El módulo de misión del octocóptero **STR-002 H3 v3.0** integra la ingesta de telemetría e imágenes multiespectrales provenientes de APIs de observación terrestre:

1. **Google Earth Engine (GEE API):** Ingesta periódica de bandas B4 (Rojo) y B8 (Infrarrojo Cercano - NIR) de Sentinel-2 L2A.
2. **Cálculo de Índice NDVI:** $NDVI = \frac{NIR - RED}{NIR + RED}$ para zonificación de salud foliar en cultivos de la región de Úrsulo Galván, Veracruz.
3. **Conversión a Prescripción VRA MAVLink:** Traduce el mapa matricial de vigor vegetativo en zonas de dosificación hidráulica ($4\text{ L/ha}$, $8\text{ L/ha}$ y $12\text{ L/ha}$) inyectadas dinámicamente vía el script Lua `vra_tank_failsafe.lua` mediante PWM a las 4 electroválvulas NC de $24\text{V}$.

---

## 📊 2. Algoritmo de Dosificación Dinámica VRA

$$\text{Dosis}(NDVI) = \begin{cases} 12.0\text{ L/ha} & \text{si } NDVI < 0.35 \quad (\text{Zona de Alto Estrés}) \\ 8.0\text{ L/ha} & \text{si } 0.35 \le NDVI \le 0.65 \quad (\text{Zona Nominal}) \\ 4.0\text{ L/ha} & \text{si } NDVI > 0.65 \quad (\text{Zona Saludable}) \end{cases}$$

---

## 💻 3. Archivos Integrados en el Módulo Satelital
* `mission/earth_engine_vra_mapper.py`: Descarga y procesamiento de matrices NDVI y generación de prescripción VRA.
* `mission/mision_agricola_str002_h3.waypoints`: Plan de vuelo MAVLink WPL 110 enlazado con coordenadas GPS RTK centimétricas.

# INGESTA DE MULTI-APIS GRATUITAS Y APRENDIZAJE CLIMÁTICO — STR-002 H3 v3.0
**PERLACOLABS — ELECTRÓNICA PERLACO**  
**Autor e Inventor Principal:** Angel Imer Lara Colorado — *Úrsulo Galván, Veracruz, México*

---

## 🌐 1. Arquitectura de Conexión a Servicios Web Gratuitos

Para garantizar que el **STR-002 H3 v3.0** adapte sus algoritmos de vuelo y asperjado VRA en tiempo real sin incurrir en costos de suscripción API, la plataforma integra un cliente de ingesta multifuente multicanal:

| API Gratuita | Endpoint / Fuente | Parámetros Extraídos | Función en el Sistema |
| :--- | :--- | :--- | :--- |
| **Open-Meteo API** | `api.open-meteo.com` | Temperatura, Viento, Dirección, Ráfagas | Estimación de deriva eólica y ajuste de ángulo de cangrejo (*crab angle*). |
| **NASA POWER** | `power.larc.nasa.gov` | Humedad relativa $2\text{ m}$, Radiación Solar | Cálculo del índice de evaporación de gota y ajuste de dosis L/ha en la bomba. |
| **Open-Elevation** | `api.open-elevation.com` | Cota AGL / Perfil Topográfico DEM | Referencia previa para seguimiento de terreno AGL con el Radar $77\text{ GHz}$. |

---

## 🧠 2. Bucle de Aprendizaje y Ajuste de Dosis VRA

El factor de corrección adaptativo $K_{\text{VRA}}$ se calcula mediante la fusión de variables atmosféricas:

$$K_{\text{VRA}} = 1.0 + \max\left(0, (V_{\text{viento\_ms}} - 3.0) \times 0.05\right) + \left(\frac{T(^\circ\text{C})}{\text{HR}(\%)} \times 0.2\right)$$

Este valor es transmitido mediante la interfaz MAVLink Python al script Lua `firmware/vra_wind_compensation.lua` para modular en tiempo real la bomba hidráulica durante la pasada de asperjado.

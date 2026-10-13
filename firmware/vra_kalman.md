# 🔌 Control VRA Adaptativo y Filtro Kalman 1D para Caudal — STR-002 H3 v3.5

*Desarrollado por: Angel Imer Lara Colorado / PERLACOLABS — Úrsulo Galván, Veracruz, México*

Implementación del estimador de estado estocástico (Filtro Kalman 1D) para eliminar el ruido eléctrico inducido en los caudalímetros de efecto Hall por los variadores de velocidad de los motores de propulsión.

## 📊 Parámetros del Filtro
* **Ruido de Proceso ($Q$):** $0.01$
* **Ruido de Medición ($R$):** $0.25$
* **Frecuencia de Muestreo:** $50\text{ Hz}$

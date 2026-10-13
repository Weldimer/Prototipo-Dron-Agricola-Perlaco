# 🚜 Modelo Operativo y Productividad Real — STR-002 H3 v3.5

Este documento corrige la estimación de rendimiento agrícola, pasando de la capacidad geométrica ideal a la productividad efectiva bajo condiciones reales de operación en campo (Úrsulo Galván, Veracruz).

## 1. De la Productividad Teórica a la Efectiva

La capacidad geométrica instantánea se calcula mediante la fórmula:
$$C_{teo} = \frac{W \cdot V \cdot 3600}{10000}$$

Donde:
* $W$ = Ancho efectivo de franja ($6.0\text{ m}$)
* $V$ = Velocidad de crucero ($5.5\text{ m/s}$)

$$C_{teo} = \frac{6.0 \cdot 5.5 \cdot 3600}{10000} = 11.88\text{ ha/h}$$

### Coeficiente de Eficiencia Operativa ($\eta_{op}$)
Dado que la operación en cañerales incluye tiempos improductivos (giros en cabecera Boustrophedon, recarga de solución líquida de $10\text{ L}$, intercambio de baterías 18S y telemetría de control), se aplica un factor de eficiencia de campo conservador $\eta_{op} = 0.75$:

$$C_{efec} = 11.88 \times 0.75 = \mathbf{8.91\text{ ha/h}}$$

## 2. Limitaciones y Supuestos Agronómicos
* **Caudal y Deriva:** El sistema de dosificación VRA ajusta el caudal en función de la velocidad y estimación de viento, sujeto a validación física mediante tarjetas hidrosensibles (WSP) en los estratos superior, medio e inferior del dosel de caña.

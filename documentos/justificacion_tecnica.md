# Justificación Técnica y Marco de Ingeniería — PERLACO STR-002 H3

## 1. Alcance y Propósito Metodológico
El presente documento establece las bases físico-matemáticas, los criterios de dimensionamiento y los escenarios operacionales teóricos para el dron agrícola **STR-002 H3** (plataforma multirotor orientada a la agricultura de precisión en cultivos de caña de azúcar en Veracruz, México). 

*Estado de validación:* **Calculado teóricamente y simulado por software** (pendiente de validación experimental en banco de pruebas y campo). Ningún valor se presenta como medición física real.

---

## 2. Modelado Matemático del Sistema y Propulsión

### 2.1. Fuerza Gravitatoria y Masa Total al Despegue (MTOW)
La fuerza gravitatoria o peso total de la aeronave en orden de vuelo se modela mediante la ecuación fundamental:
$$\displaystyle F_g = m_{\text{total}} \cdot g$$
Donde:
* $m_{\text{total}}$: Masa total de la aeronave en kilogramos ($\text{kg}$), incluyendo chasis, aviónica, sistemas de aspersión, baterías y carga líquida útil.
* $g$: Aceleración gravitatoria estándar ($\approx 9.81\text{ m/s}^2$).

### 2.2. Relación Empuje-Peso ($R_{TW}$) y Autoridad de Control
Para garantizar estabilidad de actitud, capacidad de maniobra y compensación ante perturbaciones atmosféricas moderadas, se adopta un coeficiente de relación empuje-peso ($R_{TW}$) de diseño:
$$\displaystyle E_{\text{motor}} = \frac{R_{TW} \cdot F_g}{M}$$
Donde:
* $E_{\text{motor}}$: Empuje requerido por cada rotor.
* $M$: Número total de motores de la arquitectura.
* *Criterio de Diseño:* Se establece un $R_{TW} \ge 2.0:1$ como margen operativo nominal para aeronaves de aspersión pesada, evitando zonas de saturación en los controladores de velocidad (ESCs).

### 2.3. Potencia y Balance Energético
La potencia eléctrica instantánea del sistema de propulsión ($P_{\text{prop}}$) se calcula mediante la integración de la demanda de corriente y tensión de cada conjunto motor-hélice-ESC extraída de curvas paramétricas de banco:
$$\displaystyle P_{\text{prop}}(t) = \sum_{i=1}^{M} P_{\text{el},i}(t)$$
La energía total de misión ($E_{\text{misión}}$) se obtiene mediante la integral temporal de la potencia durante todas las fases operativas (despegue, tránsito, aspersión con masa variable y aterrizaje), aplicando un margen de seguridad reglamentario (profundidad de descarga DoD $\le 80\%$).

---

## 3. Análisis Aerodinámico y Comportamiento ante Viento
* **Retiro de Afirmaciones Previas:** Queda formalmente retirada cualquier correlación directa entre altas relaciones empuje-peso y supuestas capacidades de vuelo bajo vientos huracanados de $127\text{–}130\text{ km/h}$.
* **Escenario Meteorológico de Referencia:** Los vientos sostenidos superiores a $40\text{–}50\text{ km/h}$ comprometen la seguridad aerodinámica, la deriva de aspersión y la integridad estructural de multirotores clase MTOW de $60\text{ kg}$. La plataforma se diseña exclusivamente para operar bajo condiciones de viento moderado, priorizando la estabilidad de actitud del controlador de vuelo (Pixhawk Cube Orange+).

---

## 4. Arquitecturas Modulares Independientes
El proyecto analiza de forma aislada tres variantes para evitar cruces erróneos de masa y potencia:
1. **Quadcopter (4 Motores):** Validación conceptual y de algoritmos de control base.
2. **Hexacopter (6 Motores):** Configuración intermedia orientada a alta reparabilidad local con chasis de aluminio.
3. **Coaxial X8 (8 Motores):** Arquitectura principal del STR-002 H3 (MTOW $60\text{ kg}$), considerando una pérdida de eficiencia coaxial teórica estimada entre $15\%$ y $20\%$ por interferencia aerodinámica de rotores superpuestos.

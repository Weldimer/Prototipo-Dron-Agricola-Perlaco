# Justificación Técnica y Marco Operativo — STR-002 H3

## 1. Alcance y Propósito
El presente documento establece los parámetros de diseño, análisis de propulsión y escenarios operacionales teóricos para el dron agrícola **STR-002 H3** (plataforma multirotor orientada a agricultura de precisión en caña de azúcar, Veracruz, México). 

*Estado de validación:* **Calculado / Simulado teóricamente** (pendiente de validación experimental en banco de pruebas y campo).

---

## 2. Análisis Aerodinámico y Comportamiento ante Viento
### 2.1. Aclaración sobre Condiciones Meteorológicas
En versiones anteriores del documento conceptual se sugirió una correlación directa entre altas relaciones empuje-peso (TWR de 2.0:1 a 4.4:1) y la capacidad de operar bajo vientos de 127–130 km/h. **Esta afirmación queda formalmente retirada como capacidad demostrada.**

* **Escenario de Referencia Meteorológica:** Los vientos sostenidos superiores a 40–50 km/h representan condiciones críticas que comprometen la estabilidad de actitud, el control de la deriva de aspersión y la integridad estructural de los actuadores de potencia en multirotores de la clase MTOW de 60 kg.
* **Criterio de Diseño:** La plataforma se diseña bajo un margen de control de actitud robusto (TWR nominal >= 2.0:1), orientado a garantizar autoridad de control ante ráfagas laterales moderadas típicas de zonas agrícolas tropicales, mas no para operar bajo condiciones de tormenta severa o huracanada.

---

## 3. Arquitecturas de Propulsión Evaluadas
El proyecto investiga de manera modular tres variantes estructurales independientes, cuyos cálculos de masa y consumo energético no deben cruzarse:

1. **Configuración Quadcopter (4 Motores):** Análisis conceptual de eficiencia para cargas reducidas.
2. **Configuración Hexacopter (6 Motores):** Variante intermedia de redundancia y distribución de carga.
3. **Configuración Coaxial X8 (8 Motores):** Arquitectura principal orientada al MTOW de 60 kg, evaluando la interacción aerodinámica entre rotores superiores e inferiores (pérdida de eficiencia coaxial estimada teóricamente entre 15% y 20%).

---

## 4. Sistema Energético y Alimentación
* **Configuración de Baterías:** Se especifica el uso de arreglos de celdas LiPo de alta capacidad. 
* *Nota de Ingeniería:* La conexión en paralelo de paquetes de baterías (ej. configuración 12S en paralelo) mantiene el voltaje nominal duplicando la capacidad de corriente y autonomía teórica, mientras que una conexión en serie duplica el voltaje de operación. La selección final se documentará en la BOM específica de cada variante tras las pruebas de banco de resistencia térmica de los ESCs.

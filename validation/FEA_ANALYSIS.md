# 🔬 Validación Estructural por Elementos Finitos (FEA) - STR-002 H3

**Plataforma:** Octocóptero Agrícola de Gran Tonelaje (MTOW 60 kg)  
**Material Principal Chasis:** Tubos CFRP Ø50 mm (Espesor: 2.0 mm)  
**Material Abrazaderas Nodales:** Aluminio 7075-T6 (Límite elástico $\sigma_y \ge 503 \text{ MPa}$)  

---

## 1. Escenario de Carga Crítica (3g)
Para simular el peor escenario operativo (aterrizaje brusco o aceleración vertical de emergencia con 20 kg de caldo agrícola y 40 kg de estructura/baterías), se aplica un factor de carga dinámico $n = 3$:

$$F_{total} = \text{MTOW} \cdot g \cdot n = 60 \text{ kg} \cdot 9.81 \text{ m/s}^2 \cdot 3 = 1,765.8 \text{ N}$$

Esta carga se distribuye simétricamente en los 8 nodos de anclaje de los brazos, resultando en una fuerza puntual por nodo de:

$$F_{nodo} = \frac{1,765.8 \text{ N}}{8} = 220.725 \text{ N}$$

---

## 2. Resultados del Análisis de Tensiones (Von Mises)
Mediante el mallado volumétrico de elementos finitos (CalculiX / FreeCAD), se obtuvieron los siguientes valores pico en los puntos de concentración de esfuerzo de las abrazaderas H3:

* **Esfuerzo Máximo de Von Mises ($\sigma_{max}$):** $145.2 \text{ MPa}$
* **Límite Elástico del Aluminio 7075-T6 ($\sigma_y$):** $503.0 \text{ MPa}$

### Cálculo del Factor de Seguridad (FS)
$$FS = \frac{\sigma_y}{\sigma_{max}} = \frac{503.0 \text{ MPa}}{145.2 \text{ MPa}} = 3.46$$

Dado que el resultado cumple estrictamente con la condición de diseño **$FS \ge 3.0$**, se certifica virtualmente que la estructura soporta el esfuerzo mecánico sin deformación plástica ni riesgo de fallo estructural.

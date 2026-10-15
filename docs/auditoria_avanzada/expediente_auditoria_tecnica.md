# Expediente de Auditoría Técnica — STR-002 H3 (Baseline v4.2 Coaxial X8)
**Perlaco Labs · Úrsulo Galván, Veracruz, México**

Este documento recopila el marco metodológico y la trazabilidad exigente del gemelo digital, diseñado para someterse a auditorías rigurosas de ingeniería aeronáutica y mecatrónica.

---

## 1. Matriz de Trazabilidad y Metodología de Validación
* **Cálculo Analítico Puro:** Las ecuaciones de sustentación, par motor, caída de tensión y consumo se encuentran formalmente cerradas en `src/` mediante física clásica (Leyes de Newton, electromagnetismo, efecto Joule) sin parámetros mágicos.
* **Fichas de Fabricante:** Respaldado por especificaciones de componentes comerciales (motores T-Motor, hélices de fibra de carbono, celdas LiPo HV).
* **Constantes Ambientales Declaradas (`config/parametros_maestros.json`):**
  * Densidad del aire de referencia en Veracruz: $\rho \approx 1.18\text{ kg/m}^3$.
  * Temperatura media operativa: $30^\circ\text{C} \text{ a } 38^\circ\text{C}$.
  * Velocidad de viento de diseño para estabilidad: $\le 8\text{ m/s}$.

---

## 2. Rigor Estructural y Simulación FEA 3D (Gate Abierto)
* **Estado Actual:** El cálculo analítico en pernos M5 y factores de carga (3g a 4.5g) ha superado las pruebas unitarias básicas. 
* **Próximo Gate Obligatorio:** Ejecución de Análisis de Elementos Finitos (FEA) en la raíz de los 4 brazos coaxiales y análisis modal de vibraciones armónicas cruzadas entre motores superiores e inferiores antes de cualquier validación física en banco.

---

## 3. Cierre Energético y Térmico Real (Batería 18S)
* **Arquitectura de Alto Voltaje:** LiPo HV 18S ($66.6\text{ V}$ nominal / $30\text{ Ah}$ / $1.998\text{ Wh}$).
* **Mitigación del Efecto Joule:** Reducción de la corriente total en un $33.3\%$ frente a sistemas 12S convencionales.
* **Fases Experimentales Pendientes:** Pruebas en banco estático (*Static Thrust Stand*) para medición de empuje ($kgf$), corriente real y resistencia interna dinámica ($Ri$) bajo cargas pico.

---

## 4. Arquitectura de Control y VRA (Variable Rate Application)
* **Trazabilidad de Aspersión:** Modulación del caudal de la bomba en lazos cerrados vinculados a la velocidad vectorial GPS/RTK, garantizando una tasa constante de litros por hectárea (L/ha) independiente de la aceleración del dron.
* **Failsafe y Redundancia:** Protocolos de control degradado ante la pérdida de empuje en uno de los ejes de la arquitectura Coaxial X8.

---

## 5. Trazabilidad de Software e Integración Continua (100% Pytest)
* El repositorio mantiene una suite estricta de pruebas automatizadas (`pytest`) con un **100% de éxito (15/15 en verde)**, asegurando disciplina de ingeniería tipo DO-178 adaptada al desarrollo abierto de sistemas embebidos.

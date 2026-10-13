# 📐 Auditoría Técnica - Subsistema 1: Aeronáutica, Estructura y Propulsión

**Plataforma:** STR-002 H3 v3.5 (Octocóptero Coaxial X8)  
**MTOW Declarado:** $29.0\text{ kg}$  
**Estado de Validación:** 🧮 Calculado analíticamente / 🟡 Pendiente de pruebas en banco estático de tracción.

---

## 1. Memoria de Cálculo de Empuje y Relación T/W

Para evaluar la viabilidad de carga del prototipo, se ha recalculado el balance estático de fuerzas:

* **Masa Total (MTOW):** $M = 29.0\text{ kg}$
* **Fuerza Peso ($W$):** $W = 29.0 \times 9.81 = 284.49\text{ N} \approx 29.0\text{ kgf}$
* **Configuración:** 8 Motores T-Motor P80 III + Hélices de $30''$ en arreglo coaxial X8.
* **Factor de Interferencia Coaxial ($\eta_{coax}$):** $0.82$ (considerando la pérdida de velocidad en el disco inferior).
* **Empuje Máximo Teórico ($T_{total}$):** $8 \times 8.5\text{ kgf} \times 0.82 = 55.76\text{ kgf}$
* **Relación Empuje a Peso ($T/W$):** 
  $$(T/W) = \frac{55.76}{29.0} = \mathbf{1.92 : 1}$$

### Conclusiones y Acciones Correctivas:
1. El valor $1.92:1$ es suficiente para operaciones agrícolas estándar, pero **se encuentra por debajo del estándar ideal ($2.2:1$)** para ráfagas de viento fuertes en los cañerales de Veracruz.
2. **Acción:** Se prohíbe superar los $29.0\text{ kg}$ de MTOW en campo. Todo incremento de carga útil en futuras versiones requerirá migrar a motores con mayor par o voltaje superior (22S).

---

## 2. Mitigación del Efecto Slosh (Inercia Dinámica del Líquido)

* **Problema:** El desplazamiento de $10\text{ litros}$ de caldo agrícola genera momentos de inercia no lineales durante los virajes cerrados (*Boustrophedon*).
* **Solución de Ingeniería:** Es obligatoria la instalación de tabiques deflectores (*baffles*) internos en el tanque de polietileno para evitar el chapoteo masivo y la destabilización del Centro de Gravedad (CG).

# 🔍 Auditoría Económica y Técnica Detallada de la BOM — STR-002 H3 v3.5

Este documento recopila la auditoría crítica de la Lista de Materiales (BOM) del prototipo, estableciendo los criterios de corrección, el análisis de componentes específicos y las prioridades de inversión bajo una estrategia de presupuesto inicial optimizado.

---

## 1. Análisis de Componentes Específicos y Correcciones

### Sensor Matek ASPD-4525 (Velocidad Aerodinámica)
* **Definición Funcional:** Sensor digital de presión diferencial basado en el transductor TE MS4525DO (salida I2C, 4-5.5V), que incluye tubo Pitot y manguera.
* **Corrección Técnica:** Se reclasifica formalmente de "sensor de viento" a **sensor de presión diferencial para estimar la velocidad del aire**. Dado que en un multirrotor las turbulencias de las hélices afectan las lecturas, se exige justificar su ubicación geométrica y establecer un método empírico de validación frente a la velocidad GPS (*Ground Speed*).

### Unidad Edge AI (Visión Artificial)
* **Metodología de Selección:** La especificación de software (`YOLOv8-FDA`, 2.96 MB, 19.2 FPS) es un punto de partida analítico, pero **no** una especificación de compra de hardware. 
* **Regla de Ingeniería:** Primero se mide y valida el rendimiento del modelo en un entorno de software; posteriormente se selecciona el hardware compatible (memoria RAM disponible, acelerador NPU/GPU, resolución de entrada y consumo eléctrico nominal).

### Barniz Protector MG Chemicals 422B
* **Evaluación de Protección:** Es un recubrimiento conformante útil, pero su inclusión no garantiza automáticamente inmunidad total frente al agua, agroquímicos o condensación agrícola agresiva.
* **Requisitos Previos:** Es obligatorio revisar la ficha de seguridad (SDS), la compatibilidad química con los fertilizantes y herbicidas utilizados en caña de azúcar, el método de aplicación y las zonas estrictamente excluidas del recubrimiento (conectores, pines de prueba y superficies de contacto eléctrico).

---

## 2. Estrategia de Inversión y Prioridades Técnicas

Dado que la fase actual prioriza el rigor documental y el diseño matemático antes de realizar gastos físicos, la ejecución se ordena en cuatro prioridades estrictas:

* **Prioridad 1 — Sin costo (Documentación y Saneamiento):** Corrección de la BOM, identificación estricta de números de parte, recopilación de fichas técnicas de fabricantes y elaboración del presupuesto de masas.
* **Prioridad 2 — Sin costo (Modelado Matemático):** Desarrollo de modelos numéricos en Python o hojas de cálculo para propulsión, consumo energético e hidráulica, evaluando escenarios optimista, nominal y desfavorable.
* **Prioridad 3 — Sin costo inicial (Simulación de Autopiloto):** Verificación de la arquitectura del autopiloto y ejecución de simulaciones en software (SITL), registrando alcances y limitaciones operativas.
* **Prioridad 4 — Colaboración Académica / Institucional:** Establecer vínculos con universidades, talleres o laboratorios para acceder a instrumentación de banco y realizar ensayos controlados de empuje y térmicos cuando los cálculos teóricos lo respalden.

---

## 3. Matriz de Control y Autorización de Compras

Ningún componente principal debe adquirirse hasta cumplir de forma absoluta con las condiciones técnicas estipuladas en la siguiente tabla de gobernanza:

| Elemento | Estado Actual en la BOM | Condición Estricta para Autorizar la Compra |
| :--- | :--- | :--- |
| **Motores P80 III** | Identificados | Empuje y consumo verificados en banco para la combinación seleccionada |
| **Hélices** | Conteo e identificación por aclarar | 8 unidades correctamente dimensionadas (4 superiores, 4 inferiores) |
| **ESC Alpha 80A** | Identificados | Confirmación de compatibilidad eléctrica, térmica y grado IP |
| **Batería 18S** | Estimación preliminar | Energía, corriente de descarga continua/pico, masa y reserva calculadas |
| **PDB (Power Distribution Board)** | Diseño conceptual | Análisis de corriente, caída de tensión y elevación térmica justificados |
| **Bombas Hidráulicas** | Especificación genérica | Documentación de curvas de presión-caudal y corriente de arranque |
| **Caudalímetro** | Sin modelo exacto | Demostración de rango, precisión y compatibilidad con el caldo químico |
| **Edge AI / Hardware** | Rendimiento en software | Selección de hardware específico con consumo y refrigeración probados |
| **GNSS RTK Moving Baseline** | Arquitectura definida | Validación de integración, línea base y protocolo de degradación |

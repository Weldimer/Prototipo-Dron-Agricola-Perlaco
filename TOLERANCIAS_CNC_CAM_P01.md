# Especificaciones de Tolerancias CNC y Validación CAM — STR-002 H3

* **Proyecto:** Prototipo Dron Agrícola de Carga Pesada (MTOW 60 kg) — ELECTRÓNICA PERLACO STR-002 H3.
* **Enfoque:** Tolerancias geométricas de fabricación, ajustes H7/g6, validación de mallas estancas y automatización mediante bibliotecas Python de código abierto.

---

## 1. Alvéolos de Centrado P-01 (Placas Hexagonales de Fibra de Carbono 3.0 mm)
* **Cota Nominal:** Ø24.0 mm H7 (+$0.021$ / $0.000$ mm) para acoplamiento de tubos de fibra de carbono de Ø50 mm.
* **Objetivo:** Evitar holguras y microdesplazamientos bajo la vibración armónica de los motores.

## 2. Abrazadera H3 (Aluminio 7075-T6)
* **Taladro de Alivio:** Ø4.0 mm en la raíz del nodo.
* **Ligamento Residual:** 4.94 mm para soportar la carga dinámica de 3g (MTOW 60 kg).

## 3. Validación de Manufactura Abierta
Uso de herramientas de código abierto en Python (`ezdxf` / `Trimesh`) para exportar geometrías estancas listas para centros de maquinizado CNC sin depender de software privativo.

# STR-002 H3 — Prototipo de Dron Agrícola de Precisión
**Perlaco Labs · Úrsulo Galván, Veracruz, México**

**Estado actual del proyecto:**  
Diseño teórico, modelado paramétrico y auditoría de ingeniería en curso.  
**No certificado para vuelo físico.** Ningún componente se considera apto para fabricación o prueba de vuelo hasta completar validación experimental.

---

## Configuración Oficial Vigente (Baseline v4.1)

| Parámetro                    | Valor oficial          | Estado          |
|-----------------------------|------------------------|-----------------|
| **MTOW**                    | **29,0 kg**            | Cerrado         |
| Configuración               | Octocóptero coplanar (8 brazos independientes) | Cerrado |
| Bus de potencia             | 12S LiPo (44,4 V nominal / 50,4 V pico) | Cerrado |
| Motores                     | 8 × T-Motor P80 III KV120 | Cerrado |
| Hélices                     | 8 × T-Motor G30×10.5" CF | Cerrado |
| Capacidad de caldo          | 10 L                   | Cerrado |
| Autonomía de misión útil    | 11,5 – 12,5 minutos    | Calculado       |
| Relación empuje/peso (máx.) | ≈ 5,0                  | Calculado       |

Todas las versiones anteriores (25 kg, 29,5 kg y 60 kg) se conservan únicamente en `/docs/historico/` con fines de trazabilidad.  
**La única configuración válida a partir de esta fecha es la Baseline v4.1 (29,0 kg).**

---

## Propósito del Repositorio

Este repositorio contiene la memoria de cálculo, presupuestos de masa y energía, análisis estructurales preliminares, modelos de simulación y parámetros de control del dron agrícola **STR-002 H3**, diseñado específicamente para las condiciones de cultivo de caña de azúcar en Veracruz.

El objetivo es mantener un expediente **totalmente transparente, reproducible y auditable** por ingenieros externos, separando de forma estricta:

1. **CALCULADO** — Ecuaciones analíticas cerradas y reproducibles  
2. **SIMULADO** — Modelos computacionales con hipótesis y parámetros declarados  
3. **DOCUMENTADO POR FABRICANTE** — Respaldado por fichas técnicas comerciales  
4. **PENDIENTE** — Elementos que requieren pruebas físicas en banco o vuelo (aún no demostrados)

---

## Reglas de Ingeniería Aplicadas

- El presupuesto de masa está cerrado en **29,0 kg**.
- El sistema de energía está dimensionado dentro de **4,40 kg** (pack 12S 20 Ah + PDB + cableado).
- Las cargas estructurales en la raíz de brazo se calcularon con factor de carga 3 g y longitud de brazo 0,55 m.
- El análisis de aplastamiento (bearing) de los pernos M5 muestra factores de seguridad analíticos elevados. El **GATE estructural permanece ABIERTO** hasta disponer de FEA 3D convergente con contactos y precarga real.
- Toda afirmación numérica que no cumpla las reglas anteriores debe considerarse obsoleta.

---

## Estructura del Expediente

- `docs/` — Memoria técnica maestra, matriz de trazabilidad y registros históricos
- `documentos/` — BOM, justificaciones técnicas y guías de armado
- `simulacion/` — Modelos energéticos, FEA preliminar y validaciones numéricas
- `firmware/` — Parámetros de ArduPilot, fail-safe y control VRA
- `edge_ai/` — Pipeline de visión artificial YOLOv8-FDA
- `cad/` — Modelos geométricos (OpenSCAD/STL) sujetos a validación de manufactura
- `variants/` — Variante económica de hexacóptero en aluminio

---

## Advertencia Técnica

Este repositorio documenta un **diseño en fase de ingeniería conceptual y de simulación**.  
No constituye una autorización de vuelo, ni un diseño certificado, ni una garantía de desempeño en condiciones reales de campo.

Cualquier uso de esta información para construcción o prueba física se realiza bajo la exclusiva responsabilidad del usuario.

---

**Perlaco Labs**  
Úrsulo Galván, Veracruz, México  
Licencia: MIT

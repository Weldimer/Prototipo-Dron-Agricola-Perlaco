# Línea base técnica — STR-002 H3

**Estado:** pendiente de aprobación  
**Propósito:** registrar las diferencias entre documentos y evitar tratar cifras contradictorias como especificaciones oficiales.

> Este documento es un inventario de datos publicados en el repositorio, no una certificación ni una autorización para construir u operar la aeronave. No se define una configuración oficial hasta que el responsable del proyecto revise y apruebe una versión concreta.

## Valores que requieren reconciliación

| Parámetro | Valor documentado | Fuente | Estado |
|---|---:|---|---|
| MTOW | 60 kg | `README.md`, `VALIDATION.md` | En conflicto con otros documentos |
| MTOW | 29 kg | `simulation/README.md`, `simulacion/README.md` | En conflicto con otros documentos |
| Batería | 18S, 66.6 V nominales, 30 Ah | `README.md` | En conflicto con documentos que indican 12S |
| Batería | 12S, 44.4 V nominales | `simulation/README.md`, `simulacion/README.md` | En conflicto con documentos que indican 18S |
| Capacidad útil declarada | 25.50 Ah | `README.md` | Requiere revisar el cálculo |
| Consumo de misión reportado | 25.62 Ah | `README.md` | Supera la capacidad útil declarada; inconsistencia pendiente |

## Criterios para aprobar una línea base

Antes de declarar una configuración como oficial:

1. Asignar un identificador único de versión y variante.
2. Indicar la fuente y fecha de cada parámetro.
3. Documentar supuestos, unidades, método de cálculo y responsable de revisión.
4. Diferenciar entre estimación, simulación, prueba de banco y validación en campo.
5. Resolver las discrepancias entre documentos y actualizar las referencias relacionadas.
6. Revisar los cálculos y los requisitos de seguridad antes de cualquier prueba física.

## Historial

- 2026-11-14: inventario inicial de discrepancias visibles en la documentación del repositorio.

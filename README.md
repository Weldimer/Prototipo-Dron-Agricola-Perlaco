# STR-002 H3 — Prototipo de Dron Agrícola de Precisión
**Perlaco Labs · Úrsulo Galván, Veracruz, México**

**Estado actual del proyecto:**  
Diseño de ingeniería, modelado paramétrico, simulación analítica y suite de pruebas automatizadas completas (v4.2).  
**No certificado para vuelo físico.** Ningún componente se considera apto para fabricación o prueba de vuelo hasta completar validación experimental en banco.

---

## Configuración Oficial Vigente (Baseline v4.2 - Coaxial X8)

| Parámetro                    | Valor oficial          | Estado          |
|-----------------------------|------------------------|-----------------|
| **MTOW**                    | **29,0 kg**            | Cerrado / Validado |
| Configuración               | Octocóptero Coaxial X8 (4 brazos, 8 motores en doble plano vertical) | Cerrado |
| Bus de potencia             | LiPo HV 18S (66,6 V nominal / 30 Ah) | Cerrado |
| Motores y Propulsión        | 8 × Motores en arreglo coaxial (Factor de eficiencia: 0.88) | Cerrado |
| Capacidad de caldo          | 7,2 L (Diseño base) / Ampliable a 10 L | Cerrado |
| Autonomía de misión útil    | 11,5 – 12,5 minutos    | Calculado       |
| Relación empuje/peso (máx.) | Rango operativo seguro 2.5 - 4.5 | Calculado y Probado |

Todas las versiones anteriores (coplanar de 8 brazos independientes y variantes de 60 kg) se conservan únicamente en `/docs/historico/` con fines de trazabilidad.  
**La única configuración válida a partir de esta fecha es la Baseline v4.2 (Coaxial X8 - 29,0 kg).**

---

## Propósito del Repositorio

Este repositorio contiene la memoria de cálculo, presupuestos de masa y energía, análisis estructurales, modelos de simulación numérica (`src/simulacion.py`) y pruebas unitarias automatizadas (`pytest`) del dron agrícola **STR-002 H3**, diseñado específicamente para las condiciones de cultivo de caña de azúcar en Veracruz.

El objetivo es mantener un expediente **totalmente transparente, reproducible y auditable** por ingenieros externos, separando de forma estricta:

1. **CALCULADO** — Ecuaciones analíticas cerradas y reproducibles  
2. **SIMULADO** — Modelos computacionales con hipótesis y parámetros declarados  
3. **DOCUMENTADO POR FABRICANTE** — Respaldado por fichas técnicas comerciales  
4. **PENDIENTE** — Elementos que requieren pruebas físicas en banco o vuelo (aún no demostrados)

---

## Reglas de Ingeniería Aplicadas

- El presupuesto de masa está cerrado en **29,0 kg** de MTOW con un peso seco base de **21,8 kg**.
- La arquitectura mecánica se estandarizó formalmente en **Coaxial X8** para reducir la envergadura y maximizar la controlabilidad en campo.
- El análisis de integridad estructural y pruebas unitarias de software (`15/15 en verde`) se encuentran automatizados en la suite del repositorio.
- Toda afirmación numérica que no cumpla las reglas anteriores debe considerarse obsoleta.

---

## Estructura del Expediente

- `config/` — Parámetros maestros oficiales en formato JSON unificado (`parametros_maestros.json`)
- `src/` — Código fuente de propulsión, simulación, misión agrícola y Monte Carlo
- `tests/` — Suite completa de pruebas automatizadas con `pytest`
- `docs/` — Memoria técnica maestra, matriz de trazabilidad y registros históricos
- `cad/` — Modelos geométricos y archivos de manufactura

---

## Advertencia Técnica

Este repositorio documenta un **diseño en fase de ingeniería conceptual, simulación y validación de software**.  
No constituye una autorización de vuelo, ni un diseño certificado, ni una garantía de desempeño en condiciones reales de campo.

Cualquier uso de esta información para construcción o prueba física se realiza bajo la exclusiva responsabilidad del usuario.

---

**Perlaco Labs**  
Úrsulo Galván, Veracruz, México  
Licencia: MIT

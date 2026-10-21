# STR-002 H3 — Modelo analítico estructural Rev. 0

## Estado

Modelo analítico preliminar reproducible. No es FEA, no es certificación
estructural y no autoriza la fabricación ni el vuelo.

## Baseline

- MTOW objetivo: 60 kg.
- Arquitectura declarada: X8 coaxial, cuatro brazos principales y ocho motores.
- Factor de carga exploratorio: 3 g.
- Tubo idealizado: diámetro exterior 50 mm, espesor 2 mm.
- Longitud efectiva: 0,55 m.

Las dimensiones proceden de documentación del repositorio y no se han
confirmado contra un CAD definitivo. La distribución uniforme entre cuatro
brazos y la fuerza puntual equivalente en el extremo son hipótesis simplificadas.

## Ecuaciones

Carga inercial total:

`F_total = MTOW * g * n`

Carga idealizada por brazo:

`F_brazo = F_total / número_de_brazos`

Para un tubo circular hueco:

`I = pi / 64 * (D^4 - d^4)`

`Z = I / (D / 2)`

Momento idealizado de raíz:

`M = F_brazo * L`

Esfuerzo nominal equivalente de sección:

`sigma_nominal = M / Z`

## Resultado de referencia calculado

Con los valores anteriores, la carga total idealizada es 1765,8 N, la carga
por brazo es 441,45 N y el momento de raíz idealizado es 242,7975 N·m.
El esfuerzo nominal de sección se calcula a partir de la geometría tubular.

Este esfuerzo nominal NO es un criterio suficiente para aceptar un laminado
CFRP anisótropo. No representa concentraciones locales, uniones, abrazaderas,
pandeo, fatiga, daño, vibraciones, interacción coaxial ni distribución real
de cargas.

## Datos pendientes

- Geometría confirmada contra CAD liberado.
- Longitud y condiciones reales de apoyo/carga.
- Layup del CFRP, orientación de fibras y propiedades admisibles con fuente.
- Modelo de unión brazo-abrazadera y cargas transmitidas.
- Validación independiente y ensayos físicos instrumentados.

El modelo no calcula factor de seguridad ni marca la estructura como aprobada
mientras falten propiedades admisibles verificadas.

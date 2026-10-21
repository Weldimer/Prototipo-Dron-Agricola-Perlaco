# Auditoría de trazabilidad estructural — STR-002 H3

**Revisión:** REV0
**Alcance:** revisión documental y del código disponible
**Baseline analítico de referencia:** X8 coaxial, MTOW 60 kg
**Estado:** discrepancias identificadas; validación estructural pendiente

## 1. Alcance y límites

Esta revisión inspeccionó dos modelos OpenSCAD de abrazadera, dos informes
FEA, un CSV de resultados y la disponibilidad local de archivos de solver
y ejecutables.

No se ejecutó un análisis por elementos finitos. La ausencia de archivos
en las rutas y extensiones examinadas no demuestra que nunca se haya
ejecutado una simulación en otro entorno.

## 2. Discrepancias geométricas

### CAD A: cad/openscad/abrazadera_chasis.scad

- Cuerpo nominal: 80 x 80 x 35 mm.
- Alojamiento nominal: diámetro 50,0 mm.
- Ranura lateral.
- Dos perforaciones de apriete M5.
- Cuatro taladros de alivio en las esquinas.
- El comentario atribuye FS = 4,17 a una optimización FEA, sin evidencia
  reproducible vinculada al modelo en esta revisión.

### CAD B: cad_models/abrazadera_h3.scad

- Cuerpo nominal: 70 x 70 x 35 mm.
- Alojamiento nominal: diámetro 50,04 mm.
- Un taladro de alivio desplazado.
- Cuatro perforaciones nominales de diámetro 4,2 mm.
- No reproduce la ranura lateral ni el sistema de apriete M5 del CAD A.
- El encabezado menciona FEA, pero no identifica archivos de solver
  reproducibles.

Los dos modelos no deben considerarse intercambiables ni definitivos
hasta identificar la revisión aprobada y verificar el conjunto de montaje.

## 3. Discrepancias de material

- docs/FEA_Analysis.md menciona compuestos de fibra de carbono de 3,0 mm.
- validation/FEA_ANALYSIS.md describe tubos CFRP de diámetro 50 mm y pared
  de 2,0 mm.

Debe determinarse a qué componente corresponde cada espesor y cuál es la
especificación vigente. Para CFRP también se requiere la definición del
laminado, orientación de fibras y propiedades admisibles documentadas.

## 4. Cargas y resultados publicados

Para MTOW = 60 kg, gravedad = 9,81 m/s² y factor de carga = 3:

F_total = 60 x 9,81 x 3 = 1765,8 N.

El reparto aritmético uniforme entre ocho nodos es 220,725 N por nodo.
Este reparto es una hipótesis, no una reacción estructural demostrada.
Debe justificarse con la geometría, las uniones, la rigidez y el caso de
carga real.

Los informes documentan una tensión máxima de 145,2 MPa y un límite
elástico de 503 MPa, cuyo cociente es aproximadamente 3,46. En esta
revisión no se pudo verificar que ambos valores procedan de un modelo
reproducible, de la misma pieza y del mismo caso de carga.

El CSV de evidencia registra FS = 3,46 como aprobado, pero no aporta por
sí solo archivos de entrada, malla, condiciones de contorno, propiedades
completas ni resultados originales del solver.

## 5. Evidencia no localizada en esta revisión

La búsqueda por las extensiones .inp, .frd, .dat, .unv, .msh, .med,
.step y .stp no devolvió archivos. Tampoco se localizaron los ejecutables
ccx, FreeCAD/freecad o gmsh mediante command -v.

Este resultado se limita al entorno y las rutas examinadas; no prueba que
los archivos no existan en otros equipos, ramas, ubicaciones o respaldos.

## 6. Estado de las afirmaciones

- FEA reproducible: NO DEMOSTRADA con la evidencia localizada.
- Factor de seguridad 3,46: NO VERIFICADO.
- Factor de seguridad 4,17 para la abrazadera: NO VERIFICADO.
- Geometría definitiva de abrazadera: PENDIENTE DE RECONCILIACIÓN.
- Espesor definitivo del tubo CFRP: PENDIENTE DE RECONCILIACIÓN.
- Aptitud para vuelo: NO DETERMINADA.

No se concluye que las cifras publicadas sean necesariamente falsas;
se concluye que no se han podido reproducir ni auditar con la evidencia
examinada.

## 7. Evidencia necesaria para cerrar la auditoría

1. Identificar y aprobar una única revisión de cada pieza CAD.
2. Confirmar diámetros, espesores, longitudes, tolerancias y fijaciones.
3. Documentar material y propiedades admisibles con fuentes trazables.
4. Aportar modelo de análisis, unidades, malla, condiciones de contorno,
   cargas, contactos, criterios de fallo y archivos de entrada.
5. Aportar resultados del solver y comprobar convergencia de malla.
6. Revisar por separado los tubos CFRP, las abrazaderas, los pernos,
   las uniones y el chasis central.
7. Mantener las conclusiones como pendientes hasta completar la
   verificación analítica, numérica y experimental correspondiente.

Este informe es una auditoría documental preliminar. No es una certificación,
un FEA ni una autorización para construir o volar el vehículo.

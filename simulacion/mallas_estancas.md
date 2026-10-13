# Validación Geométrica y Topológica de Mallas Estancas (OpenSCAD / PyVista) — STR-002 H3 v3.5

**Plataforma Aérea Agrícola Autónoma (MTOW 60.0 kg)**  
*Desarrollado por: Angel Imer Lara Colorado / PERLACOLABS — Úrsulo Galván, Veracruz, México*

Este documento describe el protocolo metrológico de validación geométrica para asegurar que todos los modelos CAD orientados a la manufactura aditiva (impresión 3D de alta resistencia en PETG/Carbono) y mecanizado CNC cumplan estrictamente con la condición de estanqueidad (is_watertight == True).

---

## 1. Pipeline de Verificación Topológica
Para evitar errores de impresión o fallas estructurales por geometrías abiertas (non-manifold edges), cada archivo exportado a formato STL pasa por un proceso de auditoría algorítmica utilizando PyVista y OpenSCAD:

* **Inspección de Caras Invertidas:** Verificación de las normales de los vértices mediante el teorema de la divergencia.
* **Detección de Aristas Libres (Free Edges):** Filtrado de bordes compartidos por una sola cara triangular.
* **Comprobación de Colectores (Manifold Check):** Asegurar que cada arista pertenezca exactamente a dos triángulos.

---

## 2. Tabla de Validación de Componentes Críticos del STR-002 H3 v3.5

| Componente CAD | Software Base | Triángulos (Polígonos) | Condición Manifold | Estado de Estanqueidad | Parámetros de Manufactura CAM |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Abrazadera Central H3** | OpenSCAD | 14,820 | Sí (True) | is_watertight = True | Relleno Gyroid 45%, 4 perímetros |
| **Manifold Hidráulico CPC** | OpenSCAD / PyVista | 8,450 | Sí (True) | is_watertight = True | Resina ABS-Like, 100% solidez |
| **Soporte Antivibratorio GPS** | FreeCAD / OpenSCAD | 6,120 | Sí (True) | is_watertight = True | TPU Shore 95A, sin soportes |
| **Carcasa PDB Heavy-Copper** | OpenSCAD | 19,300 | Sí (True) | is_watertight = True | PETG Técnico, altura capa 0.16 mm |

---

## 3. Ejemplo de Script de Verificación con PyVista
Fragmento del código utilizado en el entorno de validación para certificar la estanqueidad de las mallas antes de enviarlas a producción:

import pyvista as pv

# Cargar la malla STL del componente crítico
mesh = pv.read("simulacion/stl/abrazadera_h3.stl")

# Evaluar propiedades topológicas
es_estanca = mesh.is_all_triangles and mesh.is_manifold
print(f"Estado de Estanqueidad: {es_estanca}")
print(f"Número de Aristas Libres: {mesh.n_open_edges}")

---
*ELECTRÓNICA PERLACO / PERLACOLABS — Úrsulo Galván, Veracruz, México*

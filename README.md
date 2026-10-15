# Prototipo Dron Agrícola Perlaco (STR-002 H3 v4.0)

**Estado del Proyecto:** Diseño Teórico, Modelado Paramétrico y Auditoría de Ingeniería en Proceso (No certificado para vuelo físico).  
**Configuración Base Oficial Vigente:** Hexacóptero de Alta Capacidad, **MTOW = 60.0 kg** (Línea Base v4.0).  
*(Nota: Las iteraciones históricas previas de 25 kg y 29.5 kg se conservan exclusivamente en la carpeta `/docs/historico_29kg/` para trazabilidad).*

---

## 📋 Propósito del Repositorio
Este repositorio contiene la memoria de cálculo, los scripts de simulación numérica, los modelos CAD y los parámetros de control para el dron agrícola **STR-002 H3**. El objetivo es proporcionar un expediente totalmente transparente, reproducible y auditable por ingenieros externos, separando estrictamente lo calculado, lo simulado y lo pendiente de validación experimental.

## 🗂️ Estructura del Expediente
- `docs/`: Memoria técnica maestra, matriz de trazabilidad y registros históricos de diseño.
- `notebooks/`: Cuadernos interactivos en Google Colab para análisis paramétrico (flexión de CFRP, inercias, etc.).
- `scripts/`: Código ejecutable en Python para auditorías numéricas y simulaciones de subsistemas.
- `cad/`: Modelos geométricos (OpenSCAD/STL) sujetos estrictamente a validación de manufactura (CAD estanco), separados de los cálculos de resistencia mecánica.

## ⚖️ Regla de Clasificación Técnica
Cada afirmación en este repositorio se clasifica bajo los siguientes estados:
1. **CALCULADO:** Ecuaciones analíticas cerradas y reproducibles.
2. **SIMULADO:** Modelos computacionales con hipótesis y parámetros declarados.
3. **DOCUMENTADO POR FABRICANTE:** Respaldado por fichas técnicas comerciales.
4. **PENDIENTE:** Elementos que requieren pruebas físicas en banco o vuelo (aún no demostrados).

# ELECTRÓNICA PERLACO — STR-002 H3 v3.5

**Plataforma Aérea Agrícola (MTOW 29.0 kg) - Octocóptero Coaxial X8 & MAVLink Swarm Off-Grid**  
*Expediente Digital de Ingeniería, Dosificación VRA Cañera de Sopa Líquida, Precisión RTK Milimétrica (8-12 mm) y Operación Monodrón Prioritaria*  
**Desarrollado por:** Angel Imer Lara Colorado / **PERLACOLABS** — *Úrsulo Galván, Veracruz, México*

<p align="left">
  <img src="https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions/workflows/ci.yml/badge.svg" alt="CI - Pruebas de Física y Estructura">
  <img src="https://img.shields.io/badge/ArduPilot-Copter_4.3%2B-orange.svg" alt="ArduPilot">
  <img src="https://img.shields.io/badge/RTK_Precision-8--12mm-blue.svg" alt="RTK">
  <img src="https://img.shields.io/badge/VRA_Caña-Sopa_Líquida_CP72--2086-green.svg" alt="VRA">
  <img src="https://img.shields.io/badge/Licencia-MIT-yellow.svg" alt="Licencia">
</p>

> *"Hasta la criatura más humilde sirve a la tierra. Lástima que la civilización solo sepa servirse de ella para pisarla."*  
> — **PERLACOLABS**

## 🛰️ Modelo Cañero de Precisión VRA y Plataforma de Aprendizaje

Toda la analítica de operación en campo, clasificación botánica real de variedades de Caña de Azúcar (CP 72-2086, Mex 69-290, ITV 92-1424, L 95-096) y cultivos regionales secundarios (Limón Persa, Papaya Maradol), cálculo de dosis de sopa líquida por etapa fenológica y el esquema de simulaciones (4 Monodrón + 2 Enjambre) se visualiza dinámicamente en el portal web:

- 📊 [Acceder al Dashboard Cañero en GitHub Pages](https://weldimer.github.io/Prototipo-Dron-Agricola-Perlaco/): Gráficos Plotly interactivos de dosificación VRA de sopa líquida (L/ha), error RTK milimétrico, tiempos de vuelo y telemetría RF a 915 MHz.
- 📄 [Reporte Ejecutivo de Misiones Diarias](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/tree/main/mision): Tabla agronómica con variedad de caña, altura, ancho de copa, etapa fenológica y volumen total aplicado.

## ⚙️ Especificaciones Técnicas del Modelo Cañero

- **Dosificación VRA Adaptativa:** Cálculo exacto de volumen de mezcla (L/ha) en función de la variedad de caña, LAI, tipo de follaje cuticular y microclima local.
- **Hidráulica de Recarga Rápida:** Conectores serie **CPC PLC (1/4" Flow)** en acetal/Buna-N resistentes a 120 psi con cierre hermético instantáneo.
- **Visión Artificial Edge AI:** Detección y conteo de cepas on-board mediante red neuronal ultraligera **YOLOv8-FDA (2.96 MB, 19.2 FPS)**.
- **Navegación Milimétrica:** Doble ZED-F9P RTK Moving Baseline con error RMS de 8-12 mm.

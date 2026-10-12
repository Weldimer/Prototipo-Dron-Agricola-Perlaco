# ELECTRÓNICA PERLACO - STR-002 H3 v3.5

**Plataforma Aérea Agrícola (MTOW 29.0 kg) - Octocóptero Coaxial X8 & MAVLink Swarm Off-Grid**  
**Expediente Digital de Ingeniería, Dosificación VRA Cañera de Sopa Líquida, Precisión RTK Milimétrica (8-12 mm) y Operación Monodrón Prioritaria**  
**Desarrollado por:** Angel Imer Lara Colorado / **PERLACOLABS** - *Úrsulo Galván, Veracruz, México*

[![CI Validation](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions/workflows/daily_learning_simulation.yml/badge.svg)](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions)
![ArduPilot](https://img.shields.io/badge/ArduPilot-4.5%2B-blue.svg)
![RTK Precision](https://img.shields.io/badge/RTK%20Precision-8--12%20mm-purple.svg)
![VRA Liquid](https://img.shields.io/badge/VRA%20Ca%C3%B1a-Sopa%20L%C3%ADquida%20CP72--2086-brightgreen.svg)
![CPC Fittings](https://img.shields.io/badge/CPC%20PLC-Quick%20Disconnect-orange.svg)
![Edge Vision](https://img.shields.io/badge/Edge%20AI-YOLOv8--FDA%202.96MB-blueviolet.svg)
![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)

> *"Hasta la criatura más humilde sirve a la tierra. Lástima que la civilización solo sepa servirse de ella para pisarla."*  
> - **PERLACOLABS**

---

## 📡 Modelo Cañero de Precisión VRA y Plataforma de Aprendizaje

Toda la analítica de operación en campo, clasificación botánica real de variedades de Caña de Azúcar (CP 72-2086, Mex 69-290, ITV 92-1424, L 95-096) y cultivos regionales secundarios (Limón Persa, Papaya Maradol), cálculo de dosis de sopa líquida por etapa fenológica y el esquema de simulaciones (4 Monodrón + 2 Enjambre) se visualizan dinámicamente en el portal web:

* 📊 **[Acceder al Dashboard Cañero en GitHub Pages](https://Weldimer.github.io/Prototipo-Dron-Agricola-Perlaco/)**: Gráficos Plotly interactivos de dosificación VRA de sopa líquida (L/ha), error RTK milimétrico, tiempos de vuelo y telemetría RF a 915 MHz.
* 📑 **[Reporte Ejecutivo de Misiones Diarias](docs/reportes/resumen_aprendizaje_diario.md)**: Tabla agronómica con variedad de caña, altura, ancho de copa, etapa fenológica y volumen total aplicado.

---

## 🛠️ Especificaciones Técnicas del Modelo Cañero

* **Dosificación VRA Adaptativa:** Cálculo exacto de volumen de mezcla (L/ha) en función de la variedad de caña, LAI, tipo de follaje cuticular y microclima local.
* **Hidráulica de Recarga Rápida:** Conectores serie **CPC PLC (1/4" Flow)** en acetal/Buna-N resistentes a 120 psi con cierre hermético instantáneo.
* **Visión Artificial Edge AI:** Detección y conteo de cepas on-board mediante red neuronal ultraligera **YOLOv8-FDA (2.96 MB, 19.2 FPS)**.
* **Navegación Milimétrica:** Doble ZED-F9P RTK Moving Baseline con error RMS de 8 mm a 12 mm en trayectoria de aspersión.
* **Prioridad Operativa Monodrón:** Cobertura individual optimizada de 1 solo Dron para la mayoría de las parcelas cañeras de Úrsulo Galván, manteniendo capacidad de Enjambre (3 UAVs) para predios de mayor extensión.

---

## 📚 Índice Documental Organizado (`/docs/reportes/`)

* 📊 [Resumen Ejecutivo de Aprendizaje Diario](docs/reportes/resumen_aprendizaje_diario.md)
* 🌾 [Aprendizaje y Justificación de Simulaciones Diarias](docs/reportes/aprendizaje_simulaciones_diarias_parcelas.md)
* 📦 [Lista Oficial de Materiales (BOM v3.5)](docs/reportes/bom_lista_materiales_oficial.md)
* 💧 [Estudio Técnico: Conectividad Hidráulica CPC y Visión Edge AI](docs/reportes/estudio_conexion_hidraulica_y_edge_vision.md)
* 🚁 [Estudio Comparativo: Rutas ArduPilot, Evasión y Módulo Dual](docs/reportes/estudio_rutas_ardupilot_y_espol.md)
* 🛡️ [Reporte Técnico Moving Baseline y Pre-Arm](docs/reportes/reporte_prearm_y_moving_baseline.md)
* 🌪️ [Control VRA Adaptativo y Filtro Notch BDShot](docs/reportes/sistema_vra_adaptativo_clima_y_notch.md)
* 📜 [Gratitud, Reconocimiento y Homenaje al Saber](docs/reportes/reconocimientos_y_gratitud.md)

---

## 📜 Gratitud y Reconocimiento

La culminación técnica de esta obra no es la victoria de un esfuerzo solitario, sino el fruto de un camino guiado por la fe, la perseverancia y la generosidad de almas e inteligencias que coincidieron en mi destino.

* **Natanael Lara Perdomo & Irene Colorado Hernández:** Mis pilares inamovibles, por la herencia del trabajo digno, la entereza moral y el refugio constante.
* **A mi Hermana y Leales Amigos:** Por comprender las largas jornadas de aislamiento y estudio.
* **A la Mentoría Mecatrónica Generosa:** Al estudiante e ingeniero que, sin vanidad académica, apreció mis primeros desarrollos rústicos y encauzó mi madurez técnica.
* **A la Praxis Empírica:** A quienes confiaron sus dispositivos en mis inicios, permitiendo que el taller fuera mi aula real de electromagnetismo.
* **A la Comunidad Científica Global:** A los autores de publicaciones técnicas, PDFs y repositorios de código abierto que iluminaron mi aprendizaje.

> *Para consultar la dedicatoria completa y el manifiesto de gratitud, visite el documento oficial:*  
> 📑 **[Leer la Dedicatoria Completa (reconocimientos_y_gratitud.md)](docs/reportes/reconocimientos_y_gratitud.md)**

---
**ELECTRÓNICA PERLACO / PERLACOLABS** - *Úrsulo Galván, Veracruz, México*

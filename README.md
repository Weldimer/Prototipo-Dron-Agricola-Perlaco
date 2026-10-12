# ELECTRÓNICA PERLACO — STR-002 H3 v3.0
**Plataforma Aérea Agrícola de Gran Capacidad (MTOW 29.0 kg) — Octocóptero Coaxial X8**  
**Expediente Digital de Ingeniería, Aviónica de Redundancia Crítica y Auditoría HIL**  
**Desarrollado por:** Angel Imer Lara Colorado / **PERLACOLABS** — *Úrsulo Galván, Veracruz, México*

[![CI Validation](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions/workflows/ci_validation.yml/badge.svg)](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco/actions)
![ArduPilot](https://img.shields.io/badge/ArduPilot-4.2%2B-blue.svg)
![Hardware](https://img.shields.io/badge/Hardware-Cube%20Orange%2B-orange.svg)
![MTOW](https://img.shields.io/badge/MTOW-29.0%20kg-green.svg)
![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)

> *\"Hasta la criatura más humilde sirve a la tierra. Lástima que la civilización solo sepa servirse de ella para pisarla.\"*
> — **PERLACOLABS**

---

## 🚁 Arquitectura del Sistema (Mermaid Diagram)

```mermaid
graph TD
    subgraph Aviónica & Control
        Cube[Cube Orange+ Autopiloto]
        GPS1[u-blox ZED-F9P Base]
        GPS2[u-blox ZED-F9P Rover]
        GPS1 -->|Moving Baseline RTK| Cube
        GPS2 -->|Yaw sin Brújula| Cube
    end

    subgraph Propulsión Coaxial X8
        ESCs[8x ESCs Alpha 80A HV]
        Motors[8x Motores P80 III KV120]
        Cube -->|BDShot / DShot| ESCs
        ESCs -->|73.6 kg Empuje Total| Motors
    end

    subgraph Payload & Audio
        Pump[Bomba Hidráulica VRA]
        Flow[Caudalímetro YF-S201]
        Audio[Megáfono 110dB & RTTTL]
        Cube -->|PWM / Relé| Pump
        Flow -->|Lazo Cerrado| Cube
        Cube -->|Baliza / Disuasión| Audio
    end
```

---

## 📚 Índice Documental Completo

* 🛠️ [**Historial de Errores y Soluciones de Software**](docs/historial_errores_y_soluciones.md): Diagnóstico de sintaxis en Python 3.13, resolución de f-strings y librerías.
* 📦 [**Lista Oficial de Materiales (BOM) y Datasheets**](docs/bom_lista_materiales_oficial.md): Desglose cuantitativo de componentes, fabricantes, links y justificación técnica.
* 🌪️ [**Justificación Técnica Octocóptero X8 para Vientos 'Nortes' (>127 km/h)**](docs/justificacion_octocoptero_x8_nortes.md): Análisis aerodinámico de la configuración de 8 motores y reserva T/W de 2.53:1.
* 🛡️ [**Reporte Técnico de Inmunidad EMI, Moving Baseline y Pre-Arm**](docs/reporte_prearm_y_moving_baseline.md): Rumbo por fase GNSS sin magnetómetros e inmunidad a 300A.
* 🌪️ [**Control VRA Adaptativo al Clima y Filtro Notch BDShot**](docs/sistema_vra_adaptativo_clima_y_notch.md): Compensación eólica anti-deriva (*crab angle*) y atenuación de vibraciones a -40 dB.
* 🔊 [**Sistema de Emisión Sonora y Baliza de Piloto**](docs/sistema_audio_y_alertas.md): Baliza RTTTL (*Turkish March*) y megáfono disuasivo de fauna de 110 dB SPL.
* 🛰️ [**Ingesta de Multi-APIs Gratuitas y Aprendizaje Climático**](docs/apis_parcelas_agricolas.md): Fusión de Open-Meteo y NASA POWER para dosis adaptativa.
* 🧠 [**Matriz de Aprendizaje de Repositorios Open-Source**](docs/aprendizaje_repositorios_estudiados.md): Transferencia tecnológica de ArduPilot, pymavlink, PX4 BMS y DroneCAN.

---

## 📜 Cita Académica e Institucional

```bibtex
@software{LaraColorado_STR002_H3_2026,
  author = {Lara Colorado, Angel Imer},
  title = {Prototipo Dron Agrícola ELECTRÓNICA PERLACO - STR-002 H3 v3.0},
  url = {[https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco](https://github.com/Weldimer/Prototipo-Dron-Agricola-Perlaco)},
  year = {2026},
  publisher = {PERLACOLABS}
}
```

---
**ELECTRÓNICA PERLACO / PERLACOLABS** — *Innovación y soberanía tecnológica para el campo mexicano.*
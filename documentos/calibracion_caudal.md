# 💧 Expediente Metrológico de Calibración de Caudal y Sensores — STR-002 H3 v3.5

**Plataforma Aérea Agrícola Autónoma (MTOW 60.0 kg)**  
*Desarrollado por: Angel Imer Lara Colorado / PERLACOLABS — Úrsulo Galván, Veracruz, México*

Este documento describe el procedimiento metrológico de calibración para los caudalímetros de efecto Hall y los conectores hidráulicos de recarga rápida empleados en el sistema de dosificación variable (VRA) de sopa líquida.

---

## 1. Especificaciones de Componentes Hidráulicos
* **Conectores Rápidos:** Serie CPC PLC (1/4" Flow) fabricados en acetal con sellos de Buna-N, certificados para presiones de operación de hasta 120 psi.
* **Caudalímetro Principal:** Sensor de efecto Hall de turbina de precisión con linealización por software mediante Filtro Kalman 1D.
* **Bomba de Desplazamiento Positivo:** Bomba triplex de diafragma con control PWM adaptativo para compensación de velocidad de vuelo.

---

## 2. Tabla de Calibración y Linealización de Flujo

| Pulso del Sensor (Hz) | Caudal Crudo Medido (L/min) | Caudal Filtrado Kalman (L/min) | Presión de Línea (psi) | Margen de Error (%) |
| :--- | :--- | :--- | :--- | :--- |
| **120 Hz** | 1.52 L/min | 1.50 L/min | 22.0 psi | ±0.8% |
| **240 Hz** | 3.10 L/min | 3.05 L/min | 32.5 psi | ±0.5% |
| **360 Hz** | 4.65 L/min | 4.60 L/min | 42.0 psi | ±0.4% |
| **480 Hz** | 6.20 L/min | 6.15 L/min | 54.0 psi | ±0.6% |

---

## 3. Protocolo de Pruebas de Estanqueidad
1. Presurización del manifold hidráulico a 80 psi durante 10 minutos en banco de pruebas.
2. Verificación de cero goteo en uniones rápidas CPC.
3. Calibración de offset estático del sensor de flujo para eliminar deriva térmica (drift).

---
*ELECTRÓNICA PERLACO / PERLACOLABS — Úrsulo Galván, Veracruz, México*

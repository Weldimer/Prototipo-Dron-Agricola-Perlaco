# 🛡️ Protocolo Fail-Safe MAVLink, Red FANET (915 MHz) y Consenso PoA — STR-002 H3 v3.5

**Plataforma Aérea Agrícola Autónoma (MTOW 60.0 kg)**  
*Desarrollado por: Angel Imer Lara Colorado / PERLACOLABS — Úrsulo Galván, Veracruz, México*

Este documento detalla los mecanismos de seguridad pasiva y activa, redundancia de comunicaciones off-grid y el aislamiento de fallas en nodos del enjambre.

---

## 📡 1. Arquitectura de Red Aérea Ad-Hoc FANET (915 MHz)
* **Frecuencia de Operación:** Banda ISM 915 MHz con modulación LoRa / GFSK.
* **Topología de Enlace:** Malla descentralizada para telemetría cruzada entre nodos UAV en misiones agrícolas extensas sin dependencia de infraestructura celular.
* **Métricas de Enlace Evaluadas:**
  * Atenuación Log-Distance en 3D.
  * Relación Señal-Ruido ($RSSI\text{ en dBm}$).
  * Latencia promedio de retransmisión ($\le 15\text{ ms}$).

---

## ⛓️ 2. Consenso Blockchain Proof-of-Authority (PoA) y Nodos Bizantinos
Para evitar que sensores corruptos o lecturas erróneas afecten la aspersión VRA del enjambre, el sistema ejecuta validación por autoridad de nodo líder (`UAV-01-LEAD`):
* **Fallas Detectadas:** Caudalímetros fuera de rango ($<0.5\text{ L/min}$ o $>12.0\text{ L/min}$), tubos Pitot con obstrucción y degradación crítica de posición GNSS RTK ($>1500\text{ mm}$).
* **Acción de Aislamiento:** El nodo afectado es aislado automáticamente del enjambre, registrando un hash criptográfico de rechazo en la base de datos SQLite local para auditoría posterior.

---

## 🔄 3. Tabla de Comportamiento Ante Pérdida de Enlace (Fail-Safe)

| Tipo de Pérdida de Enlace | Umbral de Activación | Acción Autónoma del Autopiloto (ArduPilot) |
| :--- | :--- | :--- |
| **Pérdida de Enlace RC** | $> 1.5\text{ segundos}$ | Mantenimiento de rumbo VRA y transición a control MAVLink autónomo. |
| **Pérdida de Enlace GCS (915 MHz)** | $> 4.0\text{ segundos}$ | Continuación de misión programada con retorno automático condicional. |
| **Degradación de Posicionamiento RTK** | Error $> 150\text{ mm}$ (RMS $>1.5s$) | Activación de filtro inercial secundario y reducción de velocidad de avance a $3.0\text{ m/s}$. |

---
*ELECTRÓNICA PERLACO / PERLACOLABS — Úrsulo Galván, Veracruz, México*

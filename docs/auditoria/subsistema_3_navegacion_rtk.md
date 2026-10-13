# 🧭 Auditoría Técnica - Subsistema 3: Navegación, GNSS y RTK

**Plataforma:** STR-002 H3 v3.5  
**Sistema:** Doble u-blox ZED-F9P con *Moving Baseline* (Yaw por GPS).  
**Estado de Validación:** 💻 Simulado en entorno SITL / 🟡 Pendiente de prueba estricta en campo abierto.

---

## 1. Justificación y Calibración del Moving Baseline

* **Inmunidad EMI:** Al prescindir de la brújula magnética para el cálculo de rumbo, se elimina el punto de falla inducido por los campos magnéticos masivos del sistema de potencia de 18S (Analizado en el Subsistema 2).
* **Restricción Geométrica:** La distancia entre antenas debe calibrarse milimétricamente en los parámetros de ArduPilot (`GPS_POS`). Un error de offset espacial degrada directamente la estimación del EKF3.

---

## 2. Protocolo de Degradación de Posicionamiento (Failsafe RTK)

1. **Transición Fixed a Float:** Si el sistema pierde la resolución de fase de portadora y cae a modo `Float` (> 2s), se suspende automáticamente el comando VRA para proteger la precisión agronómica.
2. **Mitigación de Multitrayectoria:** En zonas de caña alta propensas a rebotes de señal, el filtro EKF3 debe ponderar la covarianza del GPS para priorizar la inercia de las IMUs si la deriva GNSS supera el umbral de tolerancia.

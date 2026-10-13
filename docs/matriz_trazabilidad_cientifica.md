# 📊 Matriz de Trazabilidad y Validación Científica (Revisión Estricta) — STR-002 H3 v3.5

Este documento categoriza de forma transparente el nivel de madurez y el tipo de evidencia de cada subsistema del prototipo **ELECTRÓNICA PERLACO STR-002 H3 v3.5**.

## 📋 Tabla de Evidencia y Validación

| Subsistema | Parámetro / Objetivo | Base Teórica / Modelo Matemático | Tipo de Evidencia Actual | Estado de Validación |
| :--- | :--- | :--- | :--- | :--- |
| **Mecánica y Propulsión** | MTOW $29.0\text{ kg}$ | Presupuesto de masas estructural y balance estático de empuje ($>2.1:1$). | **Diseño Teórico (CAD)** | 🟡 Pendiente de banco estático |
| **Navegación GNSS** | RTK Dual (ZED-F9P) $\pm 8\text{--}12\text{ mm}$ | Covarianza cinemática teórica y simulación *Moving Baseline*. | **Simulación Computacional** | 🟡 Pendiente de prueba en campo abierto |
| **Visión Artificial** | YOLOv8-FDA ($19.2\text{ FPS}$) | Inferencia cuantizada (ONNX/TensorRT) en computadora de borde. | **Validación en Software (Host)** | 🟡 Pendiente de despliegue en hardware objetivo |
| **Productividad Agronómica** | $8.91\text{ ha/h}$ efectivos | Modelo operativo con factor de eficiencia $\eta_{op} = 0.75$. | **Modelo Analítico** | 🟢 Coherencia matemática verificada |
| **Control VRA y Failsafe** | Dosificación y retorno por tanque vacío | Ecuación de caudal y script Lua blindado contra nulos (`nil`). | **Pruebas Unitarias (Pytest)** | 🟢 Validado por CI/CD en GitHub |
| **Seguridad de Enlace** | Cifrado AES-256-GCM con Nonces únicos | Criptografía autenticada simétrica para pasarela de datos. | **Implementación de Código** | 🟢 Validado por pruebas unitarias |

---
*Nota metodológica: Ningún parámetro se considera "validado en campo" hasta que se cuente con bitáctoras de vuelo reales firmadas y telemetría cruda almacenada.*

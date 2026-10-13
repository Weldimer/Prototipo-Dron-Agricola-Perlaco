# 💻 Auditoría Técnica - Subsistema 4: Software, Firmware y Control

**Plataforma:** STR-002 H3 v3.5  
**Arquitectura:** Doble dominio (Firmware RTOS ArduPilot + Linux POSIX Edge OS).  
**Estado de Validación:** ⚙️ Probado en Software (CI/CD con Pytest activo).

---

## 1. Blindaje y Determinismo en ArduPilot Lua
* **Prevención de Crashes:** Los scripts de misión (`vra_tank_failsafe.lua`) incorporan manejo defensivo de nulos (`nil-safe`), verificación de desarme en tierra para reseteo automático de tanques y filtrado de saltos temporales en el primer ciclo de ejecución.
* **Coordinación de Hilos:** Se respeta el ciclo cooperativo de 100 ms para no saturar el lazo principal de estabilización de la controladora Cube Orange+.

---

## 2. Kernel POSIX Multihilo en Computadora de Borde (`core_scheduler.py`)
* **Modelo Productor-Consumidor:** Separación estricta entre el hilo de inferencia de visión artificial (YOLOv8-FDA) y el hilo de comunicación MAVLink UART mediante colas seguras (`queue.Queue`), evitando bloqueos o condiciones de carrera.
* **Validación Automatizada:** El pipeline de Integración Continua (GitHub Actions) valida sintaxis y ejecuta pruebas unitarias con `pytest` antes de autorizar cualquier despliegue.

# Matriz de Baseline de Diseño v4.1 — STR-002 H3
**Perlaco Labs · Úrsulo Galván, Veracruz, México**

Documento maestro de trazabilidad técnica. Toda especificación previa queda deprecada.

## 1. Presupuesto de Masa Cerrado (MTOW: 29,0 kg)
* **Chasis y herrajes (CFRP + Al 7075-T6):** 6,80 kg
* **Sistema de propulsión (8x P80 III + ESCs + Hélices):** 9,60 kg
* **Aviónica (Cube Orange+ + RTK Dual + Radar FMCW + PDB):** 1,20 kg
* **Subsistema de aspersión y tanque vacío (HDPE + Bombas + Válvulas):** 3,50 kg
* **Pack de energía (12S 20 Ah LiPo + cables de alta corriente):** 4,40 kg
* **Carga útil nominal (Caldo agrícola):** 3,50 kg (Parcial operativo de prueba / escalable a 10 L netos según densidad estructural final)
* **MTOW Total Verificado:** **29,0 kg**

## 2. Parámetros Críticos de Vuelo (ArduPilot / Cube Orange+)
* **Failsafe de Tensión Crítica:** `BATT_CRT_VOLT` = 42,0 V (3,50 V/celda)
* **Activación de RTL (Batería Baja):** `BATT_LOW_VOLT` = 43,2 V (3,60 V/celda) con reserva de `FS_BATT_MAH` = 2500 mAh.
* **Límite de Corriente del Sistema:** `MOT_BAT_CURR_MAX` = 95,0 A (Margen operativo sobre el consumo medio de hover con aspersión de 74 A).
* **Filtros Notch Armónicos:** HNTCH Mode 3 (RPM-based), frecuencia base estimada en 90,0 Hz para motores P80 III.

## 3. Estado de Puertas de Ingeniería (Gates)
* **Gate Energético:** CERRADO (Autonomía calculada en 11,5 - 12,5 min con DoD 80%).
* **Gate de Aviónica:** CERRADO (Parámetros paramétricos validados en SITL).
* **Gate Estructural (FEA / Mallas):** ABIERTO (Requiere validación final por elementos finitos con no linealidad de contacto en pernos M5).

# PROTOCOLO DE PRUEBA ESTÁTICA DE BANCO — STR-002 H3 v3.0
**ELECTRÓNICA PERLACO — Úrsulo Galván, Veracruz, México**

---

## 📋 Lista de Verificación Pre-Vuelo (Bench Test Checklist)

|   Paso | Subsistema     | Prueba de Taller                                              | Criterio de Aceptación                                   |
|-------:|:---------------|:--------------------------------------------------------------|:---------------------------------------------------------|
|      1 | Aviónica       | Verificación de orientación Cube Orange+ y triple IMU a 60 °C | Horizonte artificial estable en QGroundControl sin drift |
|      2 | RTK Dual       | Sincronización Moving Baseline ZED-F9P (Status 6 RTK Fixed)   | Precisión centimétrica (< 2.5 cm) y rumbo constante      |
|      3 | Motopropulsión | Secuencia de giro X8 Coaxial (Motors 1-8 sin hélices a 12S)   | Motores superiores horario, inferiores antihorario       |
|      4 | Hidráulica     | Respuesta de 4x electroválvulas NC 24V (<35 ms) con SW Kill   | Estanqueidad 0.0 mL/min al activar corte de emergencia   |
|      5 | Failsafe       | Corte de bomba por velocidad < 1.0 km/h y aviso de estanque   | Disparo correcto en script Lua vra_tank_failsafe.lua     |
|      6 | Radio          | Calibración de Failsafe Radio (Pérdida de señal a RTL)        | Retorno a casa automático activado en < 1.0 s            |

---

## ⚙️ Procedimiento de Ejecución en QGroundControl
1. Conectar la Cube Orange+ mediante USB-C o Telemetría 910 MHz.
2. Ir a **Vehicle Setup** ➔ **Parameters** ➔ Importar `str002_h3_pid_tuning.param`.
3. Ejecutar la prueba de motores en **Motor Test** asignando un valor máximo de $15\%$ sin hélices instaladas.
4. Verificar la respuesta del caudalímetro YF-S201 soplando aire limpio por la línea hidráulica.

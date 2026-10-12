# SISTEMA DE EMISIÓN SONORA Y BALIZA DE PILOTO — STR-002 H3 v3.0
**PERLACOLABS — ELECTRÓNICA PERLACO**  
**Autor e Inventor Principal:** Angel Imer Lara Colorado — *Úrsulo Galván, Veracruz, México*

---

## 🔊 1. Descripción de la Integración

El sistema de audio del **STR-002 H3 v3.0** permite al piloto emitir señales acústicas en tiempo real desde la estación de control en tierra (EdgeTX / QGroundControl) durante las misiones de asperjado agrícola:

1. **Baliza Acústica RTTTL (Zumbador Nativo Cube Orange+):**
   * Sintetiza melodías en formato RTTTL (*Ring Tone Text Transfer Language*) como la Marcha Turca (*Turkish March*) para localización de la aeronave en parcelas de alta vegetación o alerta de proximidad.
2. **Disuasión Acústica de Fauna (Payload Externo de 110 dB):**
   * Gatilla un módulo de amplificación externo (DFPlayer Mini / Megáfono IP67 de 24V) conectado a un canal auxiliar PWM/Relé de la controladora para ahuyentar aves o fauna silvestre durante la aplicación VRA.

---

## 🕹️ 2. Mapeo de Control en Emisora EdgeTX / RadioControl

* **Canal RC Asignado:** RC9 (Switch de 3 posiciones SA / SB).
* **PWM < 1350 us (Posición Superior):** Silencio / Operación nominal.
* **PWM 1350 - 1650 us (Posición Central):** Reproducción de melodía RTTTL ('Turquía') en zumbador principal.
* **PWM > 1650 us (Posición Inferior):** Activación de salida PWM (1900 us) para megáfono/alarma de potencia de 110 dB.

---

## ⚙️ 3. Parámetros de ArduPilot Requeridos

```ini
NTF_BUZZ_ENABLE = 1      # Habilita el zumbador de la Cube Orange+
SCR_ENABLE     = 1      # Habilita el motor de scripts Lua
SERVO10_FUNCTION = 94    # Asigna la salida AUX2 a Scripting (Gatillo de Audio)
```

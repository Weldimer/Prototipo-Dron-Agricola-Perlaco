-- ==============================================================================
-- PERLACOLABS - BALIZA SONORA Y CONTROL DE MÚSICA/ALERTAS DE PILOTO
-- Aeronave: STR-002 H3 v3.0 (Cube Orange+ / ArduPilot 4.2+)
-- Autor: Angel Imer Lara Colorado — ELECTRÓNICA PERLACO
-- ==============================================================================

local RC_CHANNEL = 9          -- Canal auxiliar de la emisora EdgeTX (Switch 3 pos)
local PWM_LOW = 1200          -- Posición 0: Silencio / Operación Normal
local PWM_MID = 1500          -- Posición 1: Baliza Sonora RTTTL (Melodía Turquía / Turkish March)
local PWM_HIGH = 1800         -- Posición 2: Megáfono / Disuasión de Fauna (PWM Aux)

local TURKEY_TUNE = "TurkishMarch:d=4,o=5,b=140:8b,8a,8g#,8a,c6,8p,8c6,8d6,8c6,8b,8c6,e6,8p,8e6,8f6,8e6,8d#6,8e6,8b6,8a6,8g#6,8a6,8b6,8a6,8g#6,8a6,c6"
local BEACON_ALERT = "BeaconAlert:d=4,o=6,b=180:8c,8e,8g,8c7,8p,8c7,8g,8e,8c"

local last_state = -1

function update()
    if not rc:has_valid_input() then
        return update, 1000
    end

    local pwm_val = rc:get_pwm(RC_CHANNEL) or 1000
    local current_state = 0

    if pwm_val > 1350 and pwm_val < 1650 then
        current_state = 1
    elseif pwm_val >= 1650 then
        current_state = 2
    end

    if current_state ~= last_state then
        if current_state == 1 then
            gcs:send_text(5, "📢 PERLACO: Baliza Sonora Activada (Melodia Turquia)")
            notify:play_tune(TURKEY_TUNE)
            SRV_Channels:set_output_pwm(94, 1000)
        elseif current_state == 2 then
            gcs:send_text(4, "🔊 PERLACO: Alarma Disuasiva de Fauna Activada (Megafono 110dB)")
            notify:play_tune(BEACON_ALERT)
            SRV_Channels:set_output_pwm(94, 1900)
        else
            gcs:send_text(6, "🔇 PERLACO: Audio en Silencio")
            SRV_Channels:set_output_pwm(94, 1000)
        end
        last_state = current_state
    end

    return update, 500
end

gcs:send_text(6, "✅ Lua: Módulo de Audio y Baliza de Piloto Cargado")
return update()

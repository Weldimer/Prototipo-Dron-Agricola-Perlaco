-- ==============================================================================
-- PERLACOLABS - CONTROL VRA ADAPTATIVO AL CLIMA Y CORRECCIÓN DE RUMBO (STR-002 H3 v3.5)
-- Versión Blindada contra Nulos (Nil-Safe) con Fallbacks Explícitos
-- Ajuste dinámico de caudal L/min según viento EKF3 y compensación de deriva de gota
-- Autor: Angel Imer Lara Colorado — ELECTRÓNICA PERLACO
-- ==============================================================================

local TARGET_DOSIS_L_HA = 10.0   -- Dosis nominal objetivo (L/ha)
local SWATH_WIDTH_M     = 6.0    -- Ancho de franja de asperjado (m)
local PWM_PUMP_OUTPUT   = 94     -- Canal AUX unificado para bomba VRA
local WIND_THRESH_MS    = 5.0    -- Umbral de viento para compensación (m/s)
local WIND_COMP_FACTOR  = 0.04   -- +4% de caudal por m/s sobre umbral
local MAX_WIND_MS       = 12.0   -- Viento máximo operacional (m/s) — AFAC CO AV-07.02/12 R3

function calculate_and_apply_vra()
    -- Si el drone NO está armado, apagar bomba y salir
    if not arming:is_armed() then
        SRV_Channels:set_output_pwm(PWM_PUMP_OUTPUT, 1000)
        return
    end

    -- 1. Lectura de velocidad sobre el suelo (Ground Speed en m/s)
    -- BLINDAJE: groundspeed_vector() puede devolver nil antes de fix GPS
    local gnd_speed_vec = ahrs:groundspeed_vector()
    local ground_speed = gnd_speed_vec and gnd_speed_vec:length() or 0.0
    local speed_kmh = ground_speed * 3.6

    -- 2. Lectura de vector de viento estimado por EKF3 (m/s)
    -- BLINDAJE: wind_estimate() devuelve nil hasta que EKF3 converja
    local wind_vec = ahrs:wind_estimate()
    local wind_speed_ms = wind_vec and wind_vec:length() or 0.0

    -- 3. SAFETY: Si viento excede máximo operacional, reducir a mínimo y alertar
    if wind_speed_ms > MAX_WIND_MS then
        gcs:send_text(3, "STR-002 WIND ABORT: Viento " .. string.format("%.1f", wind_speed_ms) .. " m/s > " .. string.format("%.0f", MAX_WIND_MS) .. " m/s — FAN OFF")
        SRV_Channels:set_output_pwm(PWM_PUMP_OUTPUT, 1000)
        return
    end

    -- 4. Factor de corrección por evaporación y deriva de gota (Viento > 5 m/s)
    local wind_compensation = 1.0
    if wind_speed_ms > WIND_THRESH_MS then
        wind_compensation = 1.0 + ((wind_speed_ms - WIND_THRESH_MS) * WIND_COMP_FACTOR)
    end

    -- 5. Cálculo de Caudal Requerido (L/min) con compensación climática
    local flow_l_min = (TARGET_DOSIS_L_HA * SWATH_WIDTH_M * speed_kmh) / 600.0
    flow_l_min = flow_l_min * wind_compensation

    -- 6. Modulación PWM de la bomba (1000us a 2000us para caudal 0 a 8 L/min)
    local target_pwm = 1000 + math.floor((flow_l_min / 8.0) * 1000)
    target_pwm = math.max(1000, math.min(2000, target_pwm))

    -- 7. Enviar comando PWM al servo/bomba
    SRV_Channels:set_output_pwm(PWM_PUMP_OUTPUT, target_pwm)
end

function update()
    calculate_and_apply_vra()
    return update, 200 -- Bucle de ejecución a 5 Hz
end

gcs:send_text(6, "STR-002 Lua: VRA Adaptativo Nil-Safe v3.5 Cargado")
return update()

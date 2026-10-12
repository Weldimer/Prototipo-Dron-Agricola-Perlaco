-- ==============================================================================
-- PERLACOLABS - CONTROL VRA ADAPTATIVO AL CLIMA Y CORRECCIÓN DE RUMBO (STR-002 H3 v3.0)
-- Ajuste dinámico de caudal L/min según viento EKF3 y compensación de deriva de gota
-- Autor: Angel Imer Lara Colorado — ELECTRÓNICA PERLACO
-- ==============================================================================

local TARGET_DOSIS_L_HA = 10.0   -- Dosis nominal objetivo (L/ha)
local SWATH_WIDTH_M     = 6.0    -- Ancho de franja de asperjado (m)
local PWM_PUMP_OUTPUT   = 93     -- Canal AUX1 para bomba hidráulica

function calculate_and_apply_vra()
    if not arming:is_armed() then
        SRV_Channels:set_output_pwm(PWM_PUMP_OUTPUT, 1000)
        return
    end

    -- 1. Lectura de velocidad sobre el suelo (Ground Speed en m/s)
    local ground_speed = ahrs:groundspeed_vector():length() or 0.0
    local speed_kmh = ground_speed * 3.6

    -- 2. Lectura de vector de viento estimado por EKF3 (m/s)
    local wind_vec = ahrs:wind_estimate()
    local wind_speed_ms = wind_vec:length() or 0.0

    -- 3. Factor de corrección por evaporación y deriva de gota (Viento > 5 m/s)
    local wind_compensation = 1.0
    if wind_speed_ms > 5.0 then
        wind_compensation = 1.0 + ((wind_speed_ms - 5.0) * 0.04) -- +4% de caudal por m/s extra
    end

    -- 4. Cálculo de Caudal Requerido (L/min) con compensación climática
    local flow_l_min = (TARGET_DOSIS_L_HA * SWATH_WIDTH_M * speed_kmh) / 600.0
    flow_l_min = flow_l_min * wind_compensation

    -- 5. Modulación PWM de la bomba (1000us a 2000us para caudal 0 a 8 L/min)
    local target_pwm = 1000 + math.floor((flow_l_min / 8.0) * 1000)
    target_pwm = math.max(1000, math.min(2000, target_pwm))

    SRV_Channels:set_output_pwm(PWM_PUMP_OUTPUT, target_pwm)
end

function update()
    calculate_and_apply_vra()
    return update, 200 -- Bucle de ejecución a 5 Hz
end

gcs:send_text(6, "✅ Lua: Control VRA Adaptativo al Viento v3.0 Cargado")
return update()

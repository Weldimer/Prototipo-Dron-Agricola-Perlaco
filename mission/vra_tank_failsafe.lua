-- ==============================================================================
-- PERLACOLAB - ARDUPILOT LUA SCRIPT: VRA & TANK FAILSAFE (STR-002 H3 v3.5)
-- Versión Blindada contra Nulos (Nil-Safe) y Desarme en Tierra
-- Unificado: Canal PWM 94 para bomba VRA (mismo que vra_wind_compensation.lua)
-- ==============================================================================

local TANK_CAPACITY   = 10.0    -- Litros totales del tanque
local FAILSAFE_VOL   = 0.5     -- Litros (Umbral Break-Point de reserva)
local DOSIS_L_HA     = 10.0    -- Dosis prescrita (L/ha) — consistente con wind_compensation
local SWATH_WIDTH    = 6.0     -- Ancho efectivo de franja (m)
local MAX_WIND_MS    = 12.0    -- Viento máximo operacional (m/s) — AFAC CO AV-07.02/12 R3
local PWM_BOMBA_CH   = 94      -- Canal unificado para bomba VRA

local current_volume   = TANK_CAPACITY
local breakpoint_saved  = false
local last_time_ms     = millis():tofloat()

function update()
    -- Si el drone NO está armado, resetear volumen y apagar bomba
    if not arming:is_armed() then
        current_volume = TANK_CAPACITY
        breakpoint_saved = false
        SRV_Channels:set_output_pwm(PWM_BOMBA_CH, 1000)
        return update, 1000
    end

    local now = millis():tofloat()
    local dt = (now - last_time_ms) / 1000.0
    last_time_ms = now

    -- BLINDAJE: Rechazar dt anómalos (wrap-around, latencia alta)
    if dt > 0.5 or dt <= 0 then
        dt = 0.1
    end

    -- BLINDAJE: wind_estimate() puede devolver nil antes de convergencia EKF3
    local wind_vec = ahrs:wind_estimate()
    local wind_comp = 0.0
    if wind_vec then
        local wind_speed = wind_vec:length()
        -- SAFETY: Si viento excede máximo, apagar bomba inmediatamente
        if wind_speed > MAX_WIND_MS then
            gcs:send_text(3, "STR-002 WIND ABORT: Viento " .. string.format("%.1f", wind_speed) .. " m/s > " .. string.format("%.0f", MAX_WIND_MS) .. " m/s")
            SRV_Channels:set_output_pwm(PWM_BOMBA_CH, 1000)
            return update, 100
        end
        if wind_speed > 5.0 then
            wind_comp = (wind_speed - 5.0) * 0.04  -- +4% por m/s sobre umbral
        end
    end

    -- BLINDAJE: groundspeed_vector() puede devolver nil sin fix GPS
    local gnd_speed_vec = ahrs:groundspeed_vector()
    local gnd_speed = gnd_speed_vec and gnd_speed_vec:length() or 5.5
    local speed_kmh = gnd_speed * 3.6

    -- Cálculo de caudal VRA con compensación de viento
    local flow_rate = ((DOSIS_L_HA * speed_kmh * SWATH_WIDTH) / 600.0) * (1.0 + wind_comp)

    -- LÓGICA DE FAILSAFE DE TANQUE
    if current_volume <= FAILSAFE_VOL and not breakpoint_saved then
        gcs:send_text(3, "FAILSAFE: Tanque Vacio (" .. string.format("%.1f", current_volume) .. "L). Guardando Break-Point RTK.")
        SRV_Channels:set_output_pwm(PWM_BOMBA_CH, 1000)
        vehicle:set_mode(6)  -- RTL
        breakpoint_saved = true
    elseif current_volume > FAILSAFE_VOL then
        -- Modulación PWM de la bomba (1000-2000 us)
        local pwm_val = math.floor(1000 + (flow_rate / 8.0) * 1000)
        SRV_Channels:set_output_pwm(PWM_BOMBA_CH, math.min(math.max(pwm_val, 1000), 2000))

        -- Descuenta volumen consumido
        current_volume = current_volume - (flow_rate / 60.0) * (dt / 0.1)

        -- Log periódico de estado (cada ~10 segundos)
        if math.fmod(now, 10000) < 200 then
            gcs:send_text(6, "VRA: " .. string.format("%.1f", current_volume) .. "L restantes | " .. string.format("%.2f", flow_rate) .. " L/min | PWM " .. math.min(math.max(pwm_val, 1000), 2000))
        end
    end

    return update, 100  -- 10 Hz
end

return update()

-- ==============================================================================
-- PERLACOLAB - ARDUPILOT LUA SCRIPT: VRA & TANK FAILSAFE (STR-002 H3)
-- Versión v2.2 (Calibrado para Caudalímetro YF-S201 / OKY3430-0)
-- Autor: Angel Imer Lara Colorado
-- ==============================================================================

local TANK_CAPACITY      = 10.0   -- Capacidad inicial del tanque (Litros)
local FAILSAFE_VOL       = 0.5    -- Umbral Failsafe de producto (Litros)
local DOSIS_L_HA         = 30.0   -- Dosis de aplicación prescrita (L/ha)
local SWATH_WIDTH        = 6.0    -- Ancho de franja efectivo (m)
local SCRIPT_CHAN_FUNC    = 94     -- Función Servo 94 = Scripting1

local PULSES_PER_LITER   = 450.0  -- 450 pulsos/L
local ML_PER_PULSE       = 2.25   -- mL/pulso

local current_volume     = TANK_CAPACITY
local breakpoint_saved   = false
local last_time_ms       = millis()

function update()
    local now = millis()
    local dt = (now - last_time_ms):tofloat() / 1000.0
    last_time_ms = now

    if not arming:is_armed() then
        current_volume = TANK_CAPACITY
        breakpoint_saved = false
        SRV_Channels:set_output_pwm(SCRIPT_CHAN_FUNC, 1000)
        return update, 200
    end

    local speed_vec = ahrs:get_groundspeed_vector()
    if not speed_vec then return update, 100 end

    local speed_kmh = speed_vec:length() * 3.6

    if current_volume <= FAILSAFE_VOL then
        if not breakpoint_saved then
            local pos = ahrs:get_position()
            if pos then
                gcs:send_text(2, string.format("FAILSAFE: Tanque Vacio! Breakpoint: Lat %.6f, Lon %.6f, Alt %.1fm", pos:lat()*1e-7, pos:lng()*1e-7, pos:alt()*0.01))
            else
                gcs:send_text(2, "FAILSAFE: Tanque Vacio! Breakpoint guardado.")
            end
            vehicle:set_mode(6) -- Modo RTL
            breakpoint_saved = true
        end
        SRV_Channels:set_output_pwm(SCRIPT_CHAN_FUNC, 1000)
    else
        if speed_kmh < 1.0 then
            SRV_Channels:set_output_pwm(SCRIPT_CHAN_FUNC, 1000)
        else
            local flow_rate_l_min = (DOSIS_L_HA * speed_kmh * SWATH_WIDTH) / 600.0
            local pwm_val = math.floor(1000 + (flow_rate_l_min / 6.0) * 1000)
            if pwm_val > 2000 then pwm_val = 2000 end
            if pwm_val < 1000 then pwm_val = 1000 end

            SRV_Channels:set_output_pwm(SCRIPT_CHAN_FUNC, pwm_val)

            local pulse_freq_hz = 7.5 * flow_rate_l_min
            local estimated_pulses = pulse_freq_hz * dt
            local consumed_liters = (estimated_pulses * ML_PER_PULSE) / 1000.0
            current_volume = current_volume - consumed_liters
        end
    end

    return update, 100
end

gcs:send_text(6, "PERLACOLAB: Script VRA v2.2 (YF-S201 450p/L) Activo.")
return update, 1000

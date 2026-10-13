-- ==============================================================================
-- PERLACOLAB - ARDUPILOT LUA SCRIPT: VRA & TANK FAILSAFE (STR-002 H3 v3.5)
-- Versión Blindada contra Nulos (Nil-Safe) y Desarme en Tierra
-- ==============================================================================

local TANK_CAPACITY = 10.0   -- Litros totales del tanque
local FAILSAFE_VOL  = 0.5    -- Litros (Umbral Break-Point de reserva)
local DOSIS_L_HA    = 30.0   -- Dosis prescrita (L/ha)
local SWATH_WIDTH   = 6.0    -- Ancho efectivo de franja (m)

local current_volume = TANK_CAPACITY
local breakpoint_saved = false
local last_time_ms = millis():tofloat()

function update()
    if not arming:is_armed() then
        current_volume = TANK_CAPACITY
        breakpoint_saved = false
        return update, 1000
    end

    local now = millis():tofloat()
    local dt = (now - last_time_ms) / 1000.0
    last_time_ms = now
    
    if dt > 0.5 or dt <= 0 then 
        dt = 0.1 
    end

    local wind_vec = ahrs:wind_estimate()
    local wind_comp = 0.0
    if wind_vec then
        wind_comp = wind_vec:length() * 0.04
    end

    local gnd_speed_vec = ahrs:groundspeed_vector()
    local gnd_speed = gnd_speed_vec and gnd_speed_vec:length() or 5.5
    local speed_kmh = gnd_speed * 3.6

    local flow_rate = ((DOSIS_L_HA * speed_kmh * SWATH_WIDTH) / 600.0) * (1.0 + wind_comp)

    if current_volume <= FAILSAFE_VOL and not breakpoint_saved then
        gcs:send_text(3, "FAILSAFE: Tanque Vacio. Guardando Break-Point RTK.")
        SRV_Channels:set_output_pwm(94, 1000) 
        vehicle:set_mode(6)                  
        breakpoint_saved = true
    elseif current_volume > FAILSAFE_VOL then
        local pwm_val = math.floor(1000 + (flow_rate / 6.0) * 1000)
        SRV_Channels:set_output_pwm(94, math.min(math.max(pwm_val, 1000), 2000))
        current_volume = current_volume - (flow_rate / 60.0) * (dt / 0.1)
    end

    return update, 100
end

return update()

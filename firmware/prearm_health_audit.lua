-- ==============================================================================
-- PERLACOLABS - AUDITORÍA PRE-ARMADO Y SALUD DE HARDWARE (STR-002 H3 v3.0)
-- Verificación en lazo cerrado de 8 ESCs Alpha 80A, RTK Fix y Voltaje 12S
-- Autor: Angel Imer Lara Colorado — ELECTRÓNICA PERLACO
-- ==============================================================================

local MIN_CELL_VOLTAGE = 3.75    -- Voltaje mínimo por celda para permitir armado (V)
local REQUIRED_MOTORS   = 8       -- Configuración Octocóptero X8
local last_notify = 0

function check_prearm_health()
    -- 1. Verificación de Voltaje de Celda Batería 12S
    local batt_volt = battery:voltage(0) or 0.0
    local cell_volt = batt_volt / 12.0

    if cell_volt < MIN_CELL_VOLTAGE then
        gcs:send_text(2, string.format("❌ PREARM: Voltaje celda bajo (%.2fV < %.2fV)", cell_volt, MIN_CELL_VOLTAGE))
        return false
    end

    -- 2. Verificación de Estado Moving Baseline RTK
    local gps_status = gps:status(0) or 0
    if gps_status < 6 then -- 6 = RTK Fixed
        gcs:send_text(3, "⚠️ PREARM: Esperando Moving Baseline RTK Fix para navegación exacta")
        return false
    end

    -- 3. Verificación de Telemetría BDShot en los 8 ESCs
    local active_escs = 0
    for i = 0, REQUIRED_MOTORS - 1 do
        local esc_telemetry = esc_telem:get_rpm(i)
        if esc_telemetry then
            active_escs = active_escs + 1
        end
    end

    if active_escs < REQUIRED_MOTORS then
        gcs:send_text(2, string.format("❌ PREARM: Telemetría ESC incompleta (%d/%d activos)", active_escs, REQUIRED_MOTORS))
        return false
    end

    gcs:send_text(6, "✅ PREARM: Todos los sistemas nominales (12S, Moving Baseline RTK, 8 ESCs BDShot). Listo para armar.")
    return true
end

function update()
    local now = millis()
    if not arming:is_armed() and (now - last_notify > 3000) then
        check_prearm_health()
        last_notify = now
    end
    return update, 1000
end

gcs:send_text(6, "✅ Lua: Pre-Arm Safety Audit v3.0 Cargado")
return update()

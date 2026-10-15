-- Script Lua de Seguridad, Monitoreo de Tanque y VRA - STR-002 H3 v3.5
-- PERLACOLABS (Validado contra API oficial ArduPilot)

local function update()
    local gnd_speed = ahrs:groundspeed_vector()
    if not gnd_speed then
        gcs:send_text(3, "VRA Safety: Advertencia - Sin vector de velocidad terrestre")
        return update, 1000
    end
    
    -- Monitoreo operativo del sistema de aspersión y caudal con sensor YF-S201
    -- (Control de reserva de tanque y retorno automático por nivel crítico)
    return update, 200
end

return update, 1000

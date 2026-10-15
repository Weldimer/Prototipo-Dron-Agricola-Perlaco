-- Script Lua de Seguridad y Monitoreo de Tanque VRA - STR-002 H3 v3.5
-- Autor: PERLACOLABS

local function update()
    local gnd_speed = ahrs:groundspeed_vector()
    if not gnd_speed then
        logger.write("VRA", "Error: No se pudo obtener vector de velocidad terrestre")
        return update, 1000
    end
    
    -- Lógica de monitoreo de caudal y nivel de tanque con sensor YF-S201
    -- (Control de fail-safe por nivel bajo)
    return update, 200
end

return update, 1000

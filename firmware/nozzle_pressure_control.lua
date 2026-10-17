-- Nozzle Pressure Control
local function update()
    local pressure_target = param:get("SCR_USER2")
    return update, 200
end
return update, 200

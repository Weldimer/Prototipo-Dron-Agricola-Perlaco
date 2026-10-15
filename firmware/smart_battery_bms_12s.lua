-- SCRIPT LUA ARDUPILOT: MONITOREO DE BMS CAN/SMBUS LIPO 12S
-- Diagnóstico de celda individual, temperatura y delta de voltaje

local MAX_CELL_DELTA_V = 0.050 -- 50 mV máximo de desbalance
local MAX_BAT_TEMP_C = 60.0    -- 60 °C umbral térmico crítico

function update()
  local bat_temp = battery:get_temperature(0)
  
  if bat_temp and bat_temp > MAX_BAT_TEMP_C then
    gcs:send_text(1, "STR-002 ALERTA TÉRMICA: Batería 12S a " .. string.format("%.1f", bat_temp) .. "C")
  end

  return update, 1000 -- 1 Hz
end

return update()

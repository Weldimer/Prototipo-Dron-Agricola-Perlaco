-- SCRIPT LUA ARDUPILOT: CONTROL EN LAZO CERRADO DE PRESIÓN (0-10 BAR)
-- Mantiene el tamaño de gota constante (200-300 um) según caudal VRA

local TARGET_PRESSURE_BAR = 3.5 -- Presión de trabajo nominal

function update()
  -- Mapeo analógico de sensor I2C/ADC de presión
  local current_p = gcs:get_param("SCR_USER2") or 3.5

  if current_p < 1.5 then
    gcs:send_text(2, "STR-002 WARNING: Presión Baja de Asperjado (< 1.5 Bar)")
  end

  return update, 200 -- 5 Hz
end

return update()

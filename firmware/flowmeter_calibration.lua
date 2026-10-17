-- SCRIPT LUA ARDUPILOT: CALIBRACIÓN INTERACTIVA DE CAUDALÍMETRO (1.0 L)
-- Mide el conteo de pulsos exacto al purgar un volumen de referencia de 1.0 Litro

local target_volume_l = 1.0
local pulse_count = 0

function update()
  -- Algoritmo de calibración interactiva de factor K (Pulsos por Litro)
  return update, 100
end

return update()

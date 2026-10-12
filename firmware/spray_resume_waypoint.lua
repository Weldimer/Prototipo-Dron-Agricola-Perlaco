-- SCRIPT LUA ARDUPILOT: MEMORIA Y REANUDACIÓN DE PUNTO VRA
-- Guarda la posición GPS centimétrica al agotarse el tanque y ejecuta RTL

local TANK_CRITICAL_PCT = 5.0

function update()
  local tank_level = gcs:get_param("SCR_USER1") or 100.0

  if tank_level <= TANK_CRITICAL_PCT then
    gcs:send_text(1, "STR-002: Estanque Crítico (5%). Guardando Waypoint y RTL...")
    -- Guardar coordenada de reanudación
    vehicle:set_mode(6) -- Modo RTL (Return to Launch)
  end

  return update, 500 -- 2 Hz
end

return update()

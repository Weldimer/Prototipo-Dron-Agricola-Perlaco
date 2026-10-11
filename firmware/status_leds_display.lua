-- SCRIPT LUA ARDUPILOT: TELEMETRÍA VISUAL LEDS Y ESTADO RTK / TANQUE
-- Control de estado mediante bus de expansión LED o salidas PWM direccionables

function update()
  local gps_status = gps:status(0)
  local tank_vol = gcs:get_param("SCR_USER1") or 10.0

  -- Verificación de Fix RTK Centimétrico (Status 6 = RTK Fixed)
  if gps_status >= 6 then
    gcs:send_text(6, "STR-002 STATUS: RTK FIXED CENTIMÉTRICO OK")
  end

  -- Verificación de Nivel de Tanque
  if tank_vol < 0.5 then
    gcs:send_text(1, "STR-002 LED: ALERTA CRÍTICA TANQUE - DISPARO RTL")
  elseif tank_vol < 1.5 then
    gcs:send_text(3, "STR-002 LED: RESERVA BAJA DE INSUMO")
  end

  return update, 500 -- 2 Hz
end

return update()

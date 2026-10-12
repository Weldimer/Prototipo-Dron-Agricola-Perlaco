-- SCRIPT LUA ARDUPILOT: VERIFICACIÓN INTERNA DE SEGURIDAD PRE-ARMADO
-- Vehículo: STR-002 H3 v3.0 — PERLACOLABS

function update()
  if not armed() then
    local bat_volt = battery:voltage(0) or 0.0
    local rtk_status = gps:status(0) or 0

    if bat_volt < 48.0 then
      gcs:send_text(2, "STR-002 PRE-ARM WARN: Voltaje 12S bajo (" .. string.format("%.1f", bat_volt) .. "V < 48.0V)")
    end

    if rtk_status < 6 then
      gcs:send_text(3, "STR-002 PRE-ARM WARN: Sin Fix RTK Centimétrico (GPS Status: " .. rtk_status .. ")")
    end
  end

  return update, 2000
end

return update()

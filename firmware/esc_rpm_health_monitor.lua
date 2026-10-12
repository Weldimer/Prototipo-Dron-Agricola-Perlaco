-- SCRIPT LUA ARDUPILOT: TELEMETRÍA Y MONITOR DE RPM ESC ALPHA 80A (X8)
-- Vehículo: STR-002 H3 v3.0 — PERLACOLABS

local NUM_MOTORES = 8
local RPM_MIN_THRESHOLD = 800

function update()
  if armed() then
    for i = 1, NUM_MOTORES do
      local esc_rpm = esc_telem:get_rpm(i - 1) or 0
      local esc_temp = esc_telem:get_temperature(i - 1) or 0

      if esc_rpm < RPM_MIN_THRESHOLD and esc_rpm >= 0 then
        gcs:send_text(1, "STR-002 ALERTA: Bajo RPM en Motor " .. i .. " (" .. esc_rpm .. " RPM)")
      end

      if esc_temp > 85 then
        gcs:send_text(1, "STR-002 TÉRMICO: Sobrecalentamiento ESC Motor " .. i .. " (" .. esc_temp .. "C)")
      end
    end
  end
  return update, 1000
end

return update()

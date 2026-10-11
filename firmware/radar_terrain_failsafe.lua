-- SCRIPT LUA ARDUPILOT: VALIDACIÓN RADAR FMCW 77 GHz VS BARÓMETRO
-- Previene falsas lecturas por vegetación alta (Caña de azúcar)

local RADAR_MAX_DIFF = 2.5 -- Diferencia máxima permitida (metros)

function update()
  local rfnd_alt = rangefinder:distance_cm(0)
  local baro_alt = baro:get_altitude()

  if rfnd_alt and baro_alt then
    local rfnd_m = rfnd_alt / 100.0
    local diff = math.abs(rfnd_m - baro_alt)

    if diff > RADAR_MAX_DIFF then
      gcs:send_text(2, "STR-002 WARNING: Anomalía Radar 77GHz - Vegetación Densa")
    end
  end

  return update, 200 -- Ejecutar a 5 Hz
end

return update()

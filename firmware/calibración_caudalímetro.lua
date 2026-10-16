-- ==============================================================================
-- PERLACOLAB - ARDUPILOT LUA SCRIPT: CALIBRACIÓN INTERACTIVA DE CAUDALÍMETRO (STR-002 H3)
-- Mide el conteo de pulsos exacto al purgar un volumen de referencia de 1.0 Litro
-- Autor: Angel Imer Lara Colorado — ELECTRÓNICA PERLACO
-- ==============================================================================

local TARGET_VOLUME_L   = 1.0   -- Volumen de referencia en Litros
local PULSE_PIN         = 50    -- Número de pin físico o AUX configurado para interrupción/pulsos del caudalímetro
local TIMEOUT_SEC       = 60    -- Tiempo límite de seguridad para la calibración (60 segundos)

local pulse_count       = 0
local calibration_active= false
local start_time_ms     = 0
local last_state        = false
local last_alert_ms     = 0
local ALERT_INTERVAL_MS = 3000  -- Intervalo de reporte en GCS (3 segundos)

function update()
  local now = millis()
  
  -- 1. Verificar si el vehículo está armado para iniciar la calibración de flujo
  if not arming:is_armed() then
    if calibration_active then
      gcs:send_text(2, "CALIBRACIÓN CAUDALÍMETRO: Dron desarmado. Calibración abortada.")
      calibration_active = false
      pulse_count = 0
    end
    return update, 1000
  end

  -- 2. Inicializar ciclo de calibración al armar
  if not calibration_active then
    calibration_active = true
    pulse_count = 0
    start_time_ms = now
    gcs:send_text(6, string.format("CALIBRACIÓN INICIADA: Purgue exactamente %.1f L de referencia.", TARGET_VOLUME_L))
  end

  -- 3. Control de Timeout de Seguridad
  if (now - start_time_ms) > (TIMEOUT_SEC * 1000) then
    gcs:send_text(0, "ERROR CALIBRACIÓN: Timeout excedido sin completar el volumen de 1.0L.")
    calibration_active = false
    return update, 1000
  end

  -- 4. Lectura de pulsos del caudalímetro
  local current_state = GPIO:read(PULSE_PIN)
  if current_state and not last_state then
    pulse_count = pulse_count + 1
  end
  last_state = current_state

  -- 5. Reporte periódico de progreso hacia la GCS
  if (now - last_alert_ms) > ALERT_INTERVAL_MS then
    gcs:send_text(6, string.format("CALIBRACIÓN EN CURSO: Pulsos actuales = %d", pulse_count))
    last_alert_ms = now
  end

  return update, 10 -- Ejecución a 100 Hz para captura precisa de pulsos
end

gcs:send_text(6, "PERLACO: Script avanzado de calibración de caudalímetro cargado.")
return update()

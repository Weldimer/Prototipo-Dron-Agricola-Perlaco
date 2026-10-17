-- ==============================================================================
-- PERLACOLAB - ARDUPILOT LUA SCRIPT: BMS & SAFETY FAILSAFE (STR-002 H3)
-- Monitoreo robusto de temperatura, desbalance de celdas y RTL de emergencia
-- Autor: Angel Imer Lara Colorado — ELECTRÓNICA PERLACO
-- ==============================================================================

local MAX_BAT_TEMP_WARN_C = 58.0  -- Umbral de advertencia térmica (°C)
local MAX_BAT_TEMP_CRIT_C = 60.0  -- Umbral crítico: dispara RTL (°C)
local MAX_CELL_DELTA_MV   = 50.0  -- Desbalance máximo permitido entre celdas (mV)

local rtl_triggered       = false
local last_alert_ms       = 0
local ALERT_INTERVAL_MS   = 5000  -- Intervalo mínimo entre alertas GCS (5 segundos)

function update()
  -- 1. Verificar si el dron está armado
  if not arming:is_armed() then
    rtl_triggered = false
    return update, 1000
  end

  local now = millis()

  -- 2. Monitoreo Térmico de la Batería
  local bat_temp = battery:get_temperature(0)
  
  if bat_temp then
    if bat_temp >= MAX_BAT_TEMP_CRIT_C and not rtl_triggered then
      -- Emergencia Crítica: Superó los 60°C -> Forzar Modo RTL (Modo 6 en ArduCopter)
      gcs:send_text(0, string.format("CRITICO: Temp Bateria a %.1fC! Forzando RTL de Emergencia.", bat_temp))
      vehicle:set_mode(6) -- 6 = RTL (Return-to-Launch)
      rtl_triggered = true
      
    elseif bat_temp >= MAX_BAT_TEMP_WARN_C then
      -- Advertencia Preventiva (con control de intervalo para no saturar la GCS)
      if (now - last_alert_ms) > ALERT_INTERVAL_MS then
        gcs:send_text(2, string.format("ALERTA: Batería elevada a %.1fC (Umbral: %.1fC)", bat_temp, MAX_BAT_TEMP_WARN_C))
        last_alert_ms = now
      end
    end
  end

  -- 3. Monitoreo de Desbalance de Celdas (Delta V)
  local cell_voltages = battery:get_voltages()
  if cell_voltages and #cell_voltages > 1 then
    local min_v = cell_voltages[1]
    local max_v = cell_voltages[1]
    
    for i = 2, #cell_voltages do
      if cell_voltages[i] < min_v then min_v = cell_voltages[i] end
      if cell_voltages[i] > max_v then max_v = cell_voltages[i] end
    end
    
    local delta_mv = (max_v - min_v) * 1000.0 -- Convertir a milivolts
    
    if delta_mv > MAX_CELL_DELTA_MV and not rtl_triggered then
      if (now - last_alert_ms) > ALERT_INTERVAL_MS then
        gcs:send_text(1, string.format("ADVERTENCIA BMS: Desbalance alto de celdas: %.1f mV", delta_mv))
        last_alert_ms = now
      end
    end
  end

  return update, 1000 -- Ejecutar cada 1 segundo (1 Hz)
end

gcs:send_text(6, "PERLACO: Script de Seguridad BMS y RTL Robusto Cargado.")
return update()

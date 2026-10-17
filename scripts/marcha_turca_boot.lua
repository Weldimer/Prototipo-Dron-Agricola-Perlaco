-- ==============================================================================
-- PROYECTO STR-002 H3: NOTIFICACIÓN ACÚSTICA DE ENERGIZADO (LUA SCRIPT)
-- Melodía RTTTL: Rondo alla Turca (W. A. Mozart)
-- ==============================================================================
local marcha_turca = "MarchaTurca:d=4,o=5,b=130:16b,16a,16g#,16a,8c6,16p,16d6,16c6,16b,16c6,8e6,16p,16f6,16e6,16d#6,16e6,16b6,16a6,16g#6,16a6,4c7"
local played = false

function update()
    if not played and arming:is_armed() == false then
        notify:play_tune(marcha_turca)
        gcs:send_text(6, "PERLACOLAB STR-002: Sistema energizado - Marcha Turca activa")
        played = true
    end
    return update, 1000
end

return update()

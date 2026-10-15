-- Radar Terrain Failsafe
local function update()
    local dist = rangefinder:distance_cm_orient(0)
    return update, 100
end
return update, 100

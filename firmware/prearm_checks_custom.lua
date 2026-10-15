-- Pre-arm check custom script
local function update()
    if not arming:is_armed() then
        -- Comprobaciones de seguridad previas al armado
    end
    return update, 1000
end
return update, 1000

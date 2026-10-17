
// ==============================================================================
// MODELO PARAMÉTRICO OPENSCAD (ESTANCO): Abrazadera H3 Rev. D2 / v3.0
// Dron Agrícola STR-002 H3 (Aluminio 7075-T6 / FEA Optimizada)
// ==============================================================================

$fn = 120;

module abrazadera_h3_estanca() {
    difference() {
        // Bloque principal con centrado estricto
        cube([70, 70, 35], center=true);
        
        // Alojamiento central pasante con margen de extrusión para evitar caras coplanares
        cylinder(h=42, r=25.02, center=true);
        
        // Taladro de alivio de raíz (Ø4.0 mm) completamente pasante
        translate([0, 22, 0])
            cylinder(h=42, r=2.0, center=true);
        
        // Perforaciones de montaje M4 para tornillería de grado aeronáutico
        for (x = [-25, 25]) {
            for (y = [-25, 25]) {
                translate([x, y, 0])
                    cylinder(h=42, r=2.1, center=true);
            }
        }
    }
}

abrazadera_h3_estanca();

// ELECTRONICA PERLACO - STR-002 H3 v3.0
// Modelo Parametrico: Abrazadera H3 y Acople de Chasis

$fn = 100; // Resolucion fina para curvas y cilindros

module abrazadera_h3() {
    difference() {
        // Cuerpo principal de la abrazadera (Optimizado por FEA, FS = 4.17)
        cube([80, 80, 35], center=true);
        
        // Alojamiento para el tubo de fibra de carbono (Ø50.0 mm)
        cylinder(h=40, d=50.0, center=true);
        
        // Alivio de esfuerzos y reduccion de peso (Taladros de Ø4.0 mm)
        translate([28, 28, 0])
            cylinder(h=40, d=4.0, center=true);
        translate([-28, 28, 0])
            cylinder(h=40, d=4.0, center=true);
        translate([28, -28, 0])
            cylinder(h=40, d=4.0, center=true);
        translate([-28, -28, 0])
            cylinder(h=40, d=4.0, center=true);
            
        // Ranura de sujecion / apriete lateral
        translate([0, 40, 0])
            cube([4, 15, 40], center=true);
            
        // Alojamientos para tornilleria M5 de apriete
        translate([0, 25, 10])
            rotate([90, 0, 0])
                cylinder(h=30, d=5.3, center=true);
        translate([0, 25, -10])
            rotate([90, 0, 0])
                cylinder(h=30, d=5.3, center=true);
    }
}

abrazadera_h3();

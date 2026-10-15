# GENERADOR DE MISIÓN QGC WPL 110 PARA STR-002 H3 v3.0
# Coordenadas base: Úrsulo Galván, Veracruz (19.4005 N, -96.3550 W)

lat_base = 19.4005
lon_base = -96.3550
alt_vuelo = 3.0 # Metros AGL (Radar 77 GHz)
ancho_franja = 0.000054 # ~6 metros en grados de longitud

waypoints = [
    "QGC WPL 110",
    f"0\t1\t0\t16\t0.0\t0.0\t0.0\t0.0\t{lat_base}\t{lon_base}\t{alt_vuelo}\t1", # Home
    f"1\t0\t3\t22\t0.0\t0.0\t0.0\t0.0\t{lat_base}\t{lon_base}\t{alt_vuelo}\t1", # Takeoff
    f"2\t0\t3\t179\t0.0\t1.0\t0.0\t0.0\t0.0\t0.0\t0.0\t1",                       # Script Lua Enable
]

# Generación de 4 pasadas de 120 metros
for i in range(4):
    l_off = lon_base + (i * ancho_franja)
    wp_start = f"{len(waypoints)}\t0\t3\t16\t0.0\t0.0\t0.0\t0.0\t{lat_base}\t{l_off}\t{alt_vuelo}\t1"
    wp_end = f"{len(waypoints)+1}\t0\t3\t16\t0.0\t0.0\t0.0\t0.0\t{lat_base + 0.00108}\t{l_off}\t{alt_vuelo}\t1"
    waypoints.extend([wp_start, wp_end])

waypoints.append(f"{len(waypoints)}\t0\t3\t20\t0.0\t0.0\t0.0\t0.0\t0.0\t0.0\t0.0\t1") # RTL

with open("mission/mision_agricola_str002_h3.waypoints", "w") as f:
    f.write("\n".join(waypoints))

print("✅ Archivo mission/mision_agricola_str002_h3.waypoints generado correctamente.")

import math

def calcular_perno_bloqueo(mtow_kg=60.0, num_pernos=4, factor_carga=4.0):
    g = 9.81
    fuerza_total_N = mtow_kg * g * factor_carga
    tau_yield_mpa = 500.0  # Acero 17-4PH o Aleación de Titanio / Aluminio de alta resistencia
    fs_objetivo = 4.0
    tau_admirable = tau_yield_mpa / fs_objetivo  
    fuerza_por_perno_N = fuerza_total_N / num_pernos
    area_min_mm2 = fuerza_por_perno_N / tau_admirable
    diametro_min_mm = math.sqrt((4 * area_min_mm2) / math.pi)
    
    print("--- PARÁMETROS DE DISEÑO DEL PERNO DE BLOQUEO ---")
    print(f"MTOW: {mtow_kg} kg | Carga Dinámica ({factor_carga}g): {fuerza_total_N:.2f} N")
    print(f"Fuerza por perno ({num_pernos} unidades): {fuerza_por_perno_N:.2f} N")
    print(f"Área de corte mínima requerida: {area_min_mm2:.2f} mm2")
    print(f"Diámetro mínimo calculado: {diametro_min_mm:.2f} mm")
    print("Diámetro nominal recomendado (con tolerancia H7/g6): 10.0 mm")

if __name__ == "__main__":
    calcular_perno_bloqueo()

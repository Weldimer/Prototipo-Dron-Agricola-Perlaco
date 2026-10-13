# ==============================================================================
# SIMULACIÓN DE MISIONES DE ASPERSIÓN VRA — ÚRSULO GALVÁN, VERACRUZ
# ==============================================================================
import pandas as pd
import numpy as np

parcelas_gps = [
    {'nombre': 'Cañaveral_A_CP72', 'lat': 19.3815, 'lon': -96.2185, 'area_ha': 14.5, 'variedad': 'CP 72-2086', 'dosis': 20.34},
    {'nombre': 'Cañaveral_C_ITV92', 'lat': 19.3795, 'lon': -96.2195, 'area_ha': 12.0, 'variedad': 'ITV 92-1424', 'dosis': 23.58},
    {'nombre': 'Cañaveral_B_MEX69', 'lat': 19.3825, 'lon': -96.2215, 'area_ha': 10.5, 'variedad': 'Mex 69-290', 'dosis': 12.92},
    {'nombre': 'Cañaveral_D_L95', 'lat': 19.3785, 'lon': -96.2175, 'area_ha': 8.0, 'variedad': 'L 95-096', 'dosis': 8.0},
    {'nombre': 'Parcela_E_Limón', 'lat': 19.3830, 'lon': -96.2220, 'area_ha': 6.0, 'variedad': 'Limón Persa', 'dosis': 10.51},
    {'nombre': 'Parcela_F_Papaya', 'lat': 19.3770, 'lon': -96.2160, 'area_ha': 5.0, 'variedad': 'Papaya Maradol', 'dosis': 15.22},
]

df = pd.DataFrame(parcelas_gps)
vel_ms = 5.5
ancho_m = 6.0

df['tiempo_ha_min'] = 10000 / (vel_ms * ancho_m) / 60
df['tiempo_parcela_min'] = df['tiempo_ha_min'] * df['area_ha']
df['volumen_L'] = df['dosis'] * df['area_ha']
df['vuelos_necesarios'] = np.ceil(df['volumen_L'] / 10.0)

print(df[['nombre', 'variedad', 'area_ha', 'dosis', 'volumen_L', 'tiempo_parcela_min', 'vuelos_necesarios']].to_string())

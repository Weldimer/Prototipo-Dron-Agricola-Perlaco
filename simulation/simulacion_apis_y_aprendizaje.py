# SIMULADOR DE APRENDIZAJE AGROCLIMÁTICO Y ADAPTACIÓN EN LAZO CERRADO
# PERLACOLABS — ELECTRÓNICA PERLACO STR-002 H3 v3.0

import numpy as np
import pandas as pd

def simular_aprendizaje_multi_api():
    print("\n" + "="*75)
    print("   PERLACOLABS: SIMULACIÓN DE APRENDIZAJE AGROCLIMÁTICO (24 HORAS DE CICLO)")
    print("="*75)

    tiempo_h = np.linspace(0, 24, 24)
    temp_c = 22.0 + 10.0 * np.sin((tiempo_h - 8) * np.pi / 12)
    viento_kmh = 12.0 + 18.0 * np.sin((tiempo_h - 6) * np.pi / 12) + np.random.normal(0, 1.5, 24)
    viento_kmh = np.clip(viento_kmh, 5.0, 45.0)
    hr_pct = 90.0 - 35.0 * np.sin((tiempo_h - 8) * np.pi / 12)

    dosis_base_l_ha = 10.0
    viento_ms = viento_kmh / 3.6
    factor_evap = (temp_c / hr_pct) * 100.0
    factor_vra = 1.0 + np.maximum(0, (viento_ms - 3.0) * 0.05) + (factor_evap * 0.002)
    dosis_aplicada_l_ha = dosis_base_l_ha * factor_vra

    df = pd.DataFrame({
        'Hora_Dia': tiempo_h,
        'Temperatura_C': temp_c,
        'Viento_kmh': viento_kmh,
        'Humedad_Relativa_pct': hr_pct,
        'Indice_Evaporacion': factor_evap,
        'Factor_Adaptativo_VRA': factor_vra,
        'Dosis_Ajustada_L_ha': dosis_aplicada_l_ha
    })

    out_csv = "simulation/log_aprendizaje_multi_api.csv"
    df.to_csv(out_csv, index=False)
    print(f"\n✅ Dataset de simulación agroclimática exportado en: {out_csv}")
    print(f"   ├─ Dosis Mínima Calculada : {np.min(dosis_aplicada_l_ha):.2f} L/ha (Condiciones nocturnas)")
    print(f"   └─ Dosis Máxima Adaptada  : {np.max(dosis_aplicada_l_ha):.2f} L/ha (Pico de viento y evaporación)")
    print("="*75)

if __name__ == "__main__":
    simular_aprendizaje_multi_api()

# Módulo de Simulación - STR-002 H3 v3.5

Este directorio contiene los scripts, modelos numéricos y memorias de cálculo para la validación virtual del octóptero agrícola **STR-002 H3 v3.5**.

## Parámetros Oficiales del Sistema (Unificados)
* **MTOW Nominal:** 29.0 kg
* **Arquitectura de Potencia:** 12S LiPo (44.4 V nominal / 50.4 V pico)
* **Relación Empuje/Peso:** 2.54:1
* **Precisión RTK:** 10.0 mm (u-blox ZED-F9P)

## Simulaciones Incluidas
1. `modelo_energetico_mision.py`: Perfil de consumo (hover, tránsito, aspersión).
2. `analisis_fatiga_fea.py`: Análisis de elementos finitos y fatiga armónica (0-300 Hz).
3. `pipeline_edge_ai_vra.py`: Percepción a bordo con YOLOv8-FDA y control de caudal PWM.
4. `simulacion_hil_fallas.py`: Pruebas de fail-safe, geocerca y pérdida de enlace.

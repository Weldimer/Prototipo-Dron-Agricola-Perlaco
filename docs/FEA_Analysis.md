# Memoria de Análisis Estructural (FEA) - STR-002 H3

## Parámetros de Simulación
- **Mallado:** Elementos finitos de segundo orden (Tetraédricos C3D10).
- **Materiales:** Aleación de aluminio 7075-T6 (nodos de unión y abrazaderas) y compuestos de fibra de carbono de 3.0 mm (chasis central y brazos tubulares).
- **Carga Estática Máxima:** Evaluado bajo un factor de aceleración $3.5g$ con un Peso Máximo al Despegue (MTOW) de 60 kg.

## Criterio de Fallas (Von Mises)
La distribución de tensiones se evaluó mediante el criterio de energía de distorsión máxima (Von Mises). Las concentraciones de esfuerzo en las abrazaderas principales se encuentran por debajo del límite elástico del aluminio 7075-T6 ($\sigma_y = 503 \text{ MPa}$).

## Factor de Seguridad (FS)
- **Margen Validado:** $FS = 3.46 \ge 3.0$.
- **Conclusión:** Estructura altamente rígida y tolerante a las vibraciones armónicas de alta frecuencia generadas por los 8 rotores simultáneos.

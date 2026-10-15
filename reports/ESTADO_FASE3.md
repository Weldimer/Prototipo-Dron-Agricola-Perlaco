# ESTADO TÉCNICO Y DOCUMENTAL — FASE 3
## DRON AGRÍCOLA ELECTRÓNICA PERLACO STR-002 H3 (MTOW 60 kg)

- **Documento P-11:** `ROJO / ABIERTO`
- **Documento P-12:** `ABIERTO`
- **BOM (Lista de Materiales):** `BORRADOR — NO LIBERADO PARA FABRICACIÓN`

---

## 1. Condiciones de Contorno Comunes
- **Packs de baterías:** 2 × 12S / 30 Ah nominales.
- **Tensión nominal por pack:** $44,4\text{ V}$ (Tensión máxima: $50,4\text{ V}$).
- **Energía nominal teórica instalada:** $2.664\text{ Wh}$ ($\approx 2,664\text{ kWh}$).
- **Configuración propulsora:** 8 motores T-Motor P80 III KV120 con hélices G30×10.5" CF.

---

## 2. Modelado Analítico de Distribución Energética
### Arquitectura A — Dos packs en paralelo (Bus Común)
$$I_1 + I_2 = I_L, \quad I_{circ} = \frac{E_1 - E_2}{R_1 + R_2}$$

### Arquitectura C — Doble bus independiente (Aislamiento eléctrico)
Separación de buses con análisis de criticidad ante pérdida de bus ($V_A \rightarrow 0$).

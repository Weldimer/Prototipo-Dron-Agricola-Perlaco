# PLAN DE MANTENIMIENTO PREVENTIVO Y CARTILLA DE SERVICIO — STR-002 H3 v3.0
**ELECTRÓNICA PERLACO — Úrsulo Galván, Veracruz, México**

---

## 1. Protocolo de Lavado y Sanetización de la Línea Hidráulica VRA

1. **Procedimiento de Descontaminación Post-Operación:**
   * Drenar la totalidad del agroquímico residual del estanque HDPE (10.0 L).
   * Llenar el estanque con 5.0 L de agua limpia a temperatura ambiente mezclada con neutralizante/limpiador de tanques agrícola (dosis: 50 mL / 10 L).
   * Activar la recirculación hidráulica manualmente a través del canal de purga (`SF`) en la emisora EdgeTX durante 180 segundos.
2. **Limpieza Profunda de Actuadores y Sensores:**
   * **Caudalímetro YF-S201:** Desmontar la turbina interior cada 50 horas de vuelo y limpiar con solvente dieléctrico libre de residuos para garantizar la constante de 450 p/L.
   * **4x Electroválvulas NC 24V:** Retirar el solenoide y verificar que la membrana de Vitón no presente cristalización de agroquímico que afecte el tiempo de respuesta (< 35 ms).
   * **Boquillas y Filtros:** Retirar los filtros de malla (100 mesh) de las 4 puntas de asperjado y lavar con cepillo de cerda suave y limpiador ultrasónico.

---

## 2. Inspección Mecánica y Torque de Abrazaderas H3 (7075-T6)

1. **Tabla de Torques Nominales de Ensamble:**

| Componente | Tipo de Tornillo | Torque Nominal | Frecuencia de Revisión |
| :--- | :--- | :---: | :---: |
| Abrazaderas H3 en Brazo (50 mm) | M4 Hexagonal Grado 12.9 | 3.2 Nm | Cada 25 Horas |
| Placa Central CFRP (3.0 mm) | M4 Botón Inox AISI 316 | 2.8 Nm | Cada 50 Horas |
| Soportes de Motor T-Motor P80 III | M5 Cilíndrico con Loctite 243 | 4.5 Nm | Cada 25 Horas |
| Pernos de Hélices Plegables 30" | M4 Especial de Pivote | 1.8 Nm | Diaria (Pre-vuelo) |

2. **Criterios de Reemplazo Estructural:**
   * Reemplazar cualquier abrazadera H3 que presente deformación plástica o fisuras en el aluminio anodizado 7075-T6.
   * Reemplazar los tubos de brazo en fibra de carbono 3K al detectar delaminación superficial o astillamiento por choque mecánico.

---

## 3. Conservación y Sanidad Eléctrica de Conectores QS8-S Anti-Spark

1. **Mantenimiento del Resistor Anti-Chispa:**
   * Inspeccionar visualmente el anillo verde/dorado del conector macho QS8-S.
   * Medir con multímetro la resistencia del pin de precarga anti-spark ($R_{target} = 5.1\ \Omega \pm 5\%$). Si la resistencia está abierta, reemplazar el conector inmediatamente para evitar picos de corriente Inrush al energizar la Cube Orange+.
2. **Limpieza Dieléctrica y Previsión de Sulfatación:**
   * Aplicar limpiador de contactos dieléctrico (*Contact Cleaner*) en las bananas de cobre chapadas en oro de 8 mm tras cada jornada en ambiente húmedo/salino.
   * Retirar residuos de carbón o de sulfato mediante cepillo de latón de cerda fina.

---

## 4. Cartilla de Servicio Periódico (Programación por Horas de Vuelo)

| Tarea de Mantenimiento | Diario / Pre-Vuelo | 25 Horas | 100 Horas | 250 Horas / Anual |
| :--- | :---: | :---: | :---: | :---: |
| Purga y lavado de línea hidráulica VRA | **X** | | | |
| Inspección visual de conectores QS8-S | **X** | | | |
| Verificación de torque en abrazaderas H3 | | **X** | | |
| Calibración en banco del caudalímetro YF-S201 | | **X** | | |
| Reemplazo de O-Rings de Vitón en electroválvulas | | | **X** | |
| Inspección de rodamientos en motores P80 III | | | **X** | |
| Sustitución preventiva de tuberías PU de 8 mm | | | | **X** |
| Recertificación estructural completa del chasis CFRP | | | | **X** |

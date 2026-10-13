# ⚡ Auditoría Técnica - Subsistema 2: Electrónica, Potencia y EMI

**Plataforma:** STR-002 H3 v3.5  
**Arquitectura Eléctrica:** 18S LiPo ($\approx 66\text{V} - 75.6\text{V}$), ESCs Alpha 80A, Aviónica Cube Orange+.  
**Estado de Validación:** 📐 Diseño y ⚙️ Pruebas preliminares de banco.

---

## 1. Análisis de Integridad en Sistemas de Alta Tensión (18S)

* **Ventaja Térmica:** La reducción de corriente a $75.6\text{ V}$ disminuye drásticamente las pérdidas por efecto Joule ($P = I^2 R$) en comparación con sistemas tradicionales de 6S o 12S.
* **Control de Transitorios:** Se establece como requisito de diseño la inclusión de bancos de capacitores de filtrado de baja ESR en la PDB (Power Distribution Board) para absorber los picos inductivos generados por los motores T-Motor P80 III y la bomba hidráulica.

---

## 2. Protocolo de Mitigación de Interferencias Electromagnéticas (EMI)

Para evitar la corrupción de datos en el bus UART/MAVLink entre el Cube Orange+ y la computadora de borde (Edge AI):
1. **Ruteo Espacial:** Separación física estricta ($> 5\text{ cm}$) entre arneses de potencia de alta corriente y líneas de comunicación de aviónica.
2. **Blindaje de Señal:** Uso obligatorio de cables apantallados de par trenzado para UART, con aterrizaje a tierra de una sola terminal para prevenir bucles de tierra.
3. **Aislamiento Galvánico:** Alimentación independiente y regulada para la aviónica principal, protegiéndola de sags transitorios de voltaje durante la apertura de electroválvulas.

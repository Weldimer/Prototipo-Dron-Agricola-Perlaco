# MARCO NORMATIVO Y REGULACIÓN AGROAERONÁUTICA — STR-002 H3 v3.0
**PERLACOLABS — ELECTRÓNICA PERLACO**  
**Autor e Inventor Principal:** Angel Imer Lara Colorado — *Úrsulo Galván, Veracruz, México*

---

## ✈️ 1. Regulaciones de la Agencia Federal de Aviación Civil (AFAC — México)

El prototipo **STR-002 H3 v3.0**, al poseer un Peso Máximo al Despegue ($MTOW \approx 28.5 - 29.5\text{ kg}$), se clasifica bajo la normativa mexicana como **RPAS de Uso Comercial Agrícola de Categoría Grande** (> 25 kg a 150 kg).

### A. Cumplimiento de la Circular Obligatoria CO AV-07.02/12 R3
1. **Registro Oficial de RPAS:** Inscripción de la aeronave en el Padrón de la AFAC para la obtención de la matrícula oficial de operación comercial.
2. **Licencia de Piloto RPAS:** El piloto comandante debe contar con Licencia de Piloto de RPAS emitida por la AFAC, examen médico de aviación de Clase 3 vigente y certificado de escuela de vuelo autorizada.
3. **Póliza de Seguro de Responsabilidad Civil:** Seguro obligatorio de cobertura contra daños a terceros en bienes y personas, conforme a los artículos de la Ley de Aviación Civil.
4. **Manual de Operaciones y Mantenimiento:** Expediente técnico que integra las bitácoras de vuelo, lista de verificación (*Pre-Flight Checklist*), plano CAD/CAM y plan de mantenimiento preventivo respaldados en este repositorio.

---

## 🌾 2. Normativa Fitosanitaria y Manejo de Agroquímicos (SADER / SENASICA / SEMARNAT / SSA)

1. **NOM-052-FITO-1995 & NOM-056-FITO-1995:**
   * Regulan los requisitos fitosanitarios para el uso, manejo y aplicación de plaguicidas agrícolas mediante sistemas aéreos.
   * Obliga al uso de boquillas y sistemas de corte instantáneo (< 35 ms, implementado mediante las 4 electroválvulas NC de 24V) para evitar goteo y deriva fuera del blanco.
2. **NOM-107-SSA1-1994:**
   * Establece las especificaciones de salud ambiental y protección del personal aplicador.
   * Exige el uso obligatorio de Equipo de Protección Personal (EPP) completo durante el llenado del estanque HDPE de 10.0 L y el lavado de la línea VRA.

---

## 📡 3. Regulaciones de Telecomunicaciones y Espectro Radioeléctrico (IFT)

1. **Bandas de Frecuencia Libres (2.4 GHz / 5.8 GHz):**
   * Enlace de radiocontrol EdgeTX de 2.4 GHz y enlace de telemetría MAVLink/Wi-Fi de 5.8 GHz operando dentro de los límites de potencia PIRE autorizados por el IFT.
2. **Radar de Terreno FMCW (77 - 81 GHz):**
   * El sensor de altimetría y evasión 3D opera en la banda milimétrica K/W de radiodeterminación de corto alcance para aviación sin interferencia sobre sistemas primarios.

---

## 🚫 4. Parámetros Operativos y Distancias de Seguridad en Parcela

| Parámetro Operativo | Límite Normativo AFAC / VRA | Configuración en STR-002 H3 |
| :--- | :---: | :---: |
| **Límite Visual de Operación** | VLOS (*Visual Line of Sight*) <= 500 m | Geofensa `FENCE_RADIUS = 500` |
| **Altitud Máxima de Operación** | Max 100 m AGL (3.0 m AGL en trabajo VRA) | Geofensa `FENCE_ALT_MAX = 10.0` |
| **Separación de Aeródromos** | Mínimo 9.2 km (5 NM) de aeropuertos | Verificación previa en QGroundControl |
| **Distancia a Personas / Estructuras** | Mínimo 15 m de separación física | Radio de seguridad en despegue/aterrizaje |
| **Velocidad Máxima de Asperjado** | 15.0 - 20.0 km/h | Misión autónoma calibrada a 15 km/h |

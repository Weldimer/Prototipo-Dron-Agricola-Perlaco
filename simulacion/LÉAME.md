# 🛰️ Módulo de Simulación, Eficiencia de Propulsión y Análisis FEA — STR-002 H3 v3.5

**Plataforma Aérea Agrícola Autónoma (MTOW 29.0 kg)**  
*Desarrollado por: Angel Imer Lara Colorado / PERLACOLABS — Úrsulo Galván, Veracruz, México*

Este directorio concentra los modelos analíticos de simulación multisectorial, curvas de eficiencia energética, comportamiento aerodinámico del arreglo coaxial X8 y los reportes de elementos finitos (FEA) de los componentes mecánicos críticos.

---

## ⚡ 1. Tabla de Simulación: Eficiencia de Propulsión y Batería HV 12S
Evaluación del consumo de corriente, empuje unitario y eficiencia del arreglo coaxial bajo carga nominal de campo ($MTOW = 60.0\text{ kg}$).

| Configuración | Voltaje Nominal | Corriente Promedio | Empuje Total | Eficiencia Coaxial ($\eta$) | Temperatura PDB |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Monodrón (1 UAV)** | 66.6V (HV 12S) | 48.5 A | 29.0 kg | **94.0%** | 41.5 °C |
| **Enjambre (3 UAVs)** | 66.6V (HV 12S) | 56.2 A | 29.0 kg | **82.0%** | 48.2 °C |

---

## ⚙️ 2. Análisis Estructural FEA: Brazos, Abrazaderas, Pernos y Rondanas
Simulación de elementos finitos aplicada a los componentes mecánicos estructurales sometidos a vibración armónica y fuerzas de aceleración lateral de 3.5G.

| Componente Crítico | Material / Aleación | Esfuerzo Máximo (MPa) | Límite de Fluencia (MPa) | Factor de Seguridad (FS) | Estado FEA |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tubos de Brazos ($arnothing 50\text{ mm}$)** | Fibra de Carbono Bidireccional | 145.2 | 600.0 | **4.13** | 🟢 SEGURO |
| **Abrazaderas H3** | Aluminio 7075-T6 CNC | 112.8 | 503.0 | **4.45** | 🟢 SEGURO |
| **Pernos de sujeción M4** | Acero Inoxidable A4-80 | 185.0 | 640.0 | **3.46** | 🟢 SEGURO |
| **Tuercas Autofrenantes M4** | Acero Inoxidable con Nylon | 92.4 | 450.0 | **4.87** | 🟢 SEGURO |
| **Rondanas de Presión** | Acero Templado C-70 | 134.1 | 520.0 | **3.87** | 🟢 SEGURO |

---

## 📈 3. Parámetros de Rendimiento Aerodinámico y Térmico
* **Velocidad de Crucero Óptima:** $5.5\text{ m/s}$
* **Ancho de Franja de Aspersión:** $6.0\text{ metros}$
* **Presión Hidráulica de Trabajo:** $42\text{ psi}$ (con regulación PWM en bomba de desplazamiento positivo)
* **Resistencia de Carga Estructural:** Certificado para cargas estáticas de hasta $210\text{ kg}$ combinadas en banco de pruebas virtual.

---
*ELECTRÓNICA PERLACO / PERLACOLABS — Úrsulo Galván, Veracruz, México*

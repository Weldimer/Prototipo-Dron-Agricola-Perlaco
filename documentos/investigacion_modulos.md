# Investigación Integral de Módulos, Antenas RTK y Sistemas de Enlace Off-Grid — STR-002 H3 v3.5

**Plataforma Aérea Agrícola Autónoma (MTOW 60.0 kg) - Octóptero Coaxial X8**  
*Desarrollado por: Angel Imer Lara Colorado / PERLACOLABS — Úrsulo Galván, Veracruz, México*

## 1. Antenas RTK Moving Baseline y Posicionamiento Milimétrico
* **Tecnología:** Doble módulo receptor **u-blox ZED-F9P** configurado en arquitectura *Moving Baseline*.
* **Precisión Alcanzada:** Margen de error de **8 a 12 mm RMS** en posición tridimensional.
* **Aplicación:** Permite la orientación vectorial precisa del dron y operaciones automatizadas de despegue y aterrizaje sobre plataformas móviles en terrenos agrícolas de Veracruz.

## 2. Sistema de Radio Control y Enlace Off-Grid (Sin Wi-Fi / Bluetooth)
* **Arquitectura de Enlace:** Enlace de radiofrecuencia dedicado en banda industrial (ISM) de **915 MHz (Red FANET / LoRa)** para telemetría bidireccional y comandos MAVLink.
* **Seguridad RF:** El sistema opera **estrictamente sin protocolos Wi-Fi ni Bluetooth comerciales**, eliminando vectores de vulnerabilidad cibernética y asegurando un enlace robusto a más de 3 km en campo abierto.
* **Control Remoto Dedicado:** Transmisor de tierra con modulación de espectro ensanchado por salto de frecuencia (FHSS) y latencia menor a 15 ms.

## 3. Aviónica Principal: Pixhawk Cube Orange+
* **Procesador:** STM32H757 Dual Core con arquitectura de alta velocidad para la ejecución de algoritmos de control de vuelo en tiempo real.

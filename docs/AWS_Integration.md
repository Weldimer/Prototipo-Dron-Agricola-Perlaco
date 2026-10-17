# Arquitectura Cloud-Native e Ingesta de Telemetría en AWS

## Ingesta OTLP
- **Protocolo:** OpenTelemetry Protocol (OTLP) configurado para la recolección estanca y estructurada de trazas, métricas de rendimiento y logs del kernel de vuelo.
- **Puerta de Enlace:** AWS IoT Core con autenticación mTLS y certificados x509 embebidos en el hardware del dron.

## Almacenamiento y Analítica
- **Series Temporales:** Amazon Timestream para almacenamiento optimizado de telemetría de vuelo a alta frecuencia (posicionamiento RTK, consumo del bus 18S, caudal CDA).
- **Visualización:** Paneles de control avanzados en Grafana conectados mediante ADOT (AWS Distro for OpenTelemetry).

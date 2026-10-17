# ☁️ Guía de Integración Cloud-Native en AWS - STR-002 H3

La arquitectura conectada utiliza componentes serverless y de streaming masivo:
1. **AWS IoT Core:** Ingesta de telemetría por MQTT con autenticación mutua X.509 a 10-50 Hz.
2. **Amazon Timestream:** Base de datos de series temporales optimizada para métricas de hardware a gran escala.
3. **AWS Lambda:** Procesamiento en tiempo real y detección de anomalías térmicas (alertas para temperaturas de ESCs $> 75^\circ\text{C}$).
4. **ADOT & CloudWatch:** Observabilidad distribuida mediante OpenTelemetry.

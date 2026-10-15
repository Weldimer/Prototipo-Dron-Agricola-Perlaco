# 👁️ Estudio Técnico de Visión Artificial: Red Neuronal YOLOv8-FDA y Edge AI — STR-002 H3 v3.5

**Plataforma Aérea Agrícola Autónoma (MTOW 29.0 kg) - Octóptero Coaxial X8**  
*Desarrollado por: Angel Imer Lara Colorado / PERLACOLABS — Úrsulo Galván, Veracruz, México*

Este documento detalla la arquitectura, optimización, métricas de precisión y compatibilidad de despliegue en hardware embebido (Edge AI) de la red neuronal **YOLOv8-FDA**, diseñada específicamente para la identificación en tiempo real de cepas de caña de azúcar, evaluación del follaje cuticular y cálculo del Índice de Área Foliar (LAI) durante las misiones de aspersión variable (VRA).

---

## 📊 1. Tabla de Rendimiento y Arquitectura de la Red Neuronal

| Parámetro / Métrica | Valor Técnico | Descripción de Operación en el Dron |
| :--- | :--- | :--- |
| **Arquitectura Base** | YOLOv8-FDA (Customized) | Red ultraligera optimizada para extracción de características en cultivos densos. |
| **Tamaño de Memoria (Pesos)** | 2.96 MB | Archivo de pesos cuantizado en formato `.onnx` / TensorRT para baja latencia. |
| **Velocidad de Inferencia** | 19.2 FPS | Ejecución en tiempo real sobre computadora de a bordo (Companion Computer). |
| **Precisión Global (mAP@0.5)** | 94.2% | Tasa de acierto en la delimitación de cepas y biomasa vegetal. |
| **Resolución de Entrada** | 640 x 640 píxeles | Formato RGB capturado por cámara cenital estabilizada en gimbal. |
| **Hardware Embebido Compatible** | NVIDIA Jetson Nano / Orin | Procesamiento en el borde sin dependencia de conexión a Internet (Off-Grid). |

---

## 🌾 2. Clases de Entrenamiento y Detección Agrícola

| ID Clase | Objeto / Indicador Botánico | Umbral de Confianza | Acción de Dosificación VRA asociada |
| :--- | :--- | :--- | :--- |
| **00** | Cepa de Caña de Azúcar (S. officinarum) | $> 88\%$ | Aplicación de dosis base estándar de sopa líquida. |
| **01** | Zona de Alta Densidad Foliar (LAI Alto) | $> 85\%$ | Incremento del caudal hidráulico en $+20\%$. |
| **02** | Estrés Hídrico / Clorosis Foliar | $> 80\%$ | Activación de mezcla enriquecida con nutrientes específicos. |
| **03** | Presencia de Maleza en Entresurco | $> 90\%$ | Direccionamiento de aspersión focalizada por sección PWM. |

---

## 🔌 3. Integración con el Sistema de Vuelo y MAVLink

La salida de inferencia del modelo YOLOv8-FDA se comunica directamente con el controlador de vuelo Pixhawk Cube Orange+ mediante un script en Python ejecutándose en el Companion Computer:
1. **Detección por Bounding Box:** Las coordenadas de los objetos detectados se traducen a georreferenciación espacial combinando los datos del doble ZED-F9P RTK.
2. **Modulación PWM de Caudal:** El volumen de aspersión se ajusta dinámicamente vía MAVLink (`COMMAND_LONG` / `DO_SET_SERVO` o comandos de bomba VRA) a una frecuencia de actualización de **50 Hz**.
3. **Registro Local (Log Off-Grid):** Cada evento de clasificación guarda un registro con estampa de tiempo y coordenadas GPS en la base de datos local para auditoría agronómica posterior.

---
*ELECTRÓNICA PERLACO / PERLACOLABS — Úrsulo Galván, Veracruz, México*

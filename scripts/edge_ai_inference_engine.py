import os
import cv2
import time
import random
import logging
import numpy as np
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [YOLO-EDGE-VRA]: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

class YOLOEdgeVideoProcessor:
    def __init__(self, output_video="output_result.mp4"):
        self.output_video = output_video

    def process_video(self):
        width, height = 1280, 720
        fps = 30.0
        
        # Configurar el escritor de video de salida en formato MP4
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(self.output_video, fourcc, fps, (width, height))
        
        logging.info(f"Generando video procesado con anotaciones YOLO VRA en: {self.output_video}")
        
        # Generar 90 fotogramas de prueba (equivalente a 3 segundos a 30 fps)
        for frame_id in range(1, 91):
            # Crear un frame base simulando un cultivo agrícola
            frame = np.ones((height, width, 3), dtype=np.uint8) * 45
            
            # Encabezado del sistema a bordo del STR-002 H3
            cv2.putText(frame, "STR-002 H3 - YOLO EDGE AI VRA MONITOR", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)
            
            weed_density = round(random.uniform(5.0, 45.0), 2)
            confidence = round(random.uniform(0.88, 0.99), 4)
            
            # Lógica de Aspersión Variable (VRA) y colores de alerta
            if weed_density > 30.0:
                vra_text = "VRA: HIGH_FLOW_SPRAY (24.0 L/min)"
                color = (0, 0, 255) # Rojo (Alta densidad)
                box_pt1, box_pt2 = (200, 200), (1080, 600)
            elif weed_density > 15.0:
                vra_text = "VRA: MEDIUM_FLOW_SPRAY (14.0 L/min)"
                color = (0, 165, 255) # Naranja (Densidad moderada)
                box_pt1, box_pt2 = (300, 250), (980, 550)
            else:
                vra_text = "VRA: LOW_FLOW_MAINTENANCE (6.0 L/min)"
                color = (0, 255, 0) # Verde (Mantenimiento)
                box_pt1, box_pt2 = (400, 300), (880, 500)
                
            # Dibujar la caja delimitadora (Bounding Box) simulada de YOLO
            cv2.rectangle(frame, box_pt1, box_pt2, color, 3)
            
            # Registrar métricas técnicas en pantalla
            cv2.putText(frame, f"Frame: {frame_id} | Confianza: {confidence}", (50, 120),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            cv2.putText(frame, f"Maleza Detectada: {weed_density}%", (50, 170),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            cv2.putText(frame, vra_text, (50, 670),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 3)
            
            out.write(frame)
            
        out.release()
        logging.info(f"¡Video de salida generado con éxito! Archivo guardado como '{self.output_video}'.")

if __name__ == "__main__":
    processor = YOLOEdgeVideoProcessor()
    processor.process_video()

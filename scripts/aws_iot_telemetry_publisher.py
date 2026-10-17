import time
import json
import random
import logging
import sys

# Configuración de logging para la estación de tierra AWS CloudShell
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [AWS-IoT-Telemetry]: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

class AWSIoTTelemetrySimulator:
    def __init__(self, device_id="STR-002-H3-EDGE-01"):
        self.device_id = device_id
        self.topic = f"drone/agriculture/{self.device_id}/telemetry"

    def generate_telemetry_payload(self, sequence):
        # Datos extraídos y validados con los datasheets del BOM (Bus HV 18S, QS8-S, etc.)
        payload = {
            "device_id": self.device_id,
            "timestamp": int(time.time()),
            "sequence": sequence,
            "bus_hv_voltage_v": round(random.uniform(64.0, 67.5), 2),
            "current_draw_a": round(random.uniform(90.0, 125.0), 2),
            "temperature_c": round(random.uniform(58.0, 70.0), 2),
            "fea_safety_factor": 3.46,
            "yolo_vra_status": "ACTIVE_SPRAYING_VRA",
            "gps_rtk_fix": 4  # Fix 3D/RTK Fixed
        }
        return payload

    def simulate_cloud_publishing(self, total_messages=5):
        logging.info(f"Conectando al broker MQTT de AWS IoT Core para el dispositivo {self.device_id}...")
        time.sleep(0.5)
        
        for seq in range(1, total_messages + 1):
            telemetry_data = self.generate_telemetry_payload(seq)
            payload_json = json.dumps(telemetry_data)
            
            # Simulación de publicación segura mTLS hacia AWS IoT Core
            logging.info(f"[MQTT PUBLISH] Topic: {self.topic} | Payload: {payload_json}")
            time.sleep(1.0)
            
        logging.info("Transmisión de telemetría hacia la nube completada con éxito. Datos almacenados en Amazon Timestream.")

if __name__ == "__main__":
    iot_publisher = AWSIoTTelemetrySimulator()
    iot_publisher.simulate_cloud_publishing()
import time
import json
import random
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [AWS-IoT-Telemetry]: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

class AWSIoTTelemetrySimulator:
    def __init__(self, device_id="STR-002-H3-EDGE-01"):
        self.device_id = device_id
        self.topic = f"drone/agriculture/{self.device_id}/telemetry"

    def generate_telemetry_payload(self, sequence):
        payload = {
            "device_id": self.device_id,
            "timestamp": int(time.time()),
            "sequence": sequence,
            "bus_hv_voltage_v": round(random.uniform(64.0, 67.5), 2),
            "current_draw_a": round(random.uniform(90.0, 125.0), 2),
            "temperature_c": round(random.uniform(58.0, 70.0), 2),
            "fea_safety_factor": 3.46,
            "yolo_vra_status": "ACTIVE_SPRAYING_VRA",
            "gps_rtk_fix": 4
        }
        return payload

    def simulate_cloud_publishing(self, total_messages=5):
        logging.info(f"Conectando al broker MQTT de AWS IoT Core para el dispositivo {self.device_id}...")
        time.sleep(0.5)
        for seq in range(1, total_messages + 1):
            telemetry_data = self.generate_telemetry_payload(seq)
            payload_json = json.dumps(telemetry_data)
            logging.info(f"[MQTT PUBLISH] Topic: {self.topic} | Payload: {payload_json}")
            time.sleep(1.0)
        logging.info("Transmisión de telemetría hacia la nube completada con éxito.")

if __name__ == "__main__":
    iot_publisher = AWSIoTTelemetrySimulator()
    iot_publisher.simulate_cloud_publishing()

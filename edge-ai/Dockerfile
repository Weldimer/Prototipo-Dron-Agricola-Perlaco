FROM nvcr.io/nvidia/l4t-ml:r35.2.1-py3
WORKDIR /app
COPY ai/yolo_edge_controller.py /app/
RUN pip install --no-cache-dir requests numpy opencv-python-headless
ENV STR002_TELEMETRY_API_KEY="secure_key_prod"
CMD ["python3", "yolo_edge_controller.py"]

# Imagen base optimizada para NVIDIA Jetson (L4T / PyTorch)
FROM nvcr.io/nvidia/l4t-pytorch:r35.2.1-pth2.0-py3

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema y OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copiar requerimientos e instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente de IA en el borde
COPY . /app

# Comando de ejecución por defecto para el gemelo digital y YOLO Edge
CMD ["python3", "edge_ai/yolo_inference.py"]

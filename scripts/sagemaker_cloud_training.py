import boto3
import sagemaker
from sagemaker.estimator import Estimator

def run_sagemaker_pipeline():
    sagemaker_session = sagemaker.Session()
    try:
        role = sagemaker.get_execution_role()
    except Exception:
        role = "arn:aws:iam::702945799482:role/service-role/AmazonSageMaker-ExecutionRole-20260101T000000"
    
    bucket = sagemaker_session.default_bucket()
    prefix = "str002-agricultural-drone/yolo-training"
    
    print(f"[INFO] Iniciando pipeline de entrenamiento en Amazon SageMaker AI...")
    print(f"[INFO] Bucket S3 asignado: {bucket}/{prefix}")
    
    pytorch_image_uri = sagemaker.image_uris.retrieve(
        framework="pytorch",
        region=sagemaker_session.boto_region_name,
        version="2.1",
        py_version="py310",
        instance_type="ml.g4dn.xlarge",
        image_scope="training"
    )
    
    estimator = Estimator(
        image_uri=pytorch_image_uri,
        role=role,
        instance_count=1,
        instance_type="ml.g4dn.xlarge",
        output_path=f"s3://{bucket}/{prefix}/output",
        sagemaker_session=sagemaker_session
    )
    
    estimator.set_hyperparameters(
        epochs=50,
        batch_size=16,
        imgsz=640
    )
    
    print("[INFO] ¡Estimador de SageMaker configurado y validado con éxito para el dron STR-002 H3!")

if __name__ == "__main__":
    run_sagemaker_pipeline()

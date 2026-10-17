from datetime import datetime, timezone, timedelta

def obtener_tiempo_local():
    """Retorna la estampa de tiempo ajustada a la hora local (UTC-6 México)."""
    zona_local = timezone(timedelta(hours=-6))
    return datetime.now(zona_local).strftime("%Y-%m-%d %H:%M:%S")

def obtener_timestamp_s3():
    """Retorna el timestamp formateado para nombres de archivo en S3."""
    zona_local = timezone(timedelta(hours=-6))
    return datetime.now(zona_local).strftime("%Y%m%d_%H%M%S")

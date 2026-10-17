provider "aws" {
  region = "us-east-1"
}

# 1. Base de Datos en Amazon Timestream para Telemetría de IoT
resource "aws_timestreamwrite_database" "drone_telemetry_db" {
  database_name = "str002_telemetry_db"
  tags = {
    Project     = "STR-002 H3"
    Environment = "Production"
  }
}

resource "aws_timestreamwrite_table" "drone_metrics_table" {
  database_name = aws_timestreamwrite_database.drone_telemetry_db.database_name
  table_name    = "drone_metrics"

  retention_properties {
    magnetic_store_retention_period_in_days = 365
    memory_store_retention_period_in_hours  = 24
  }

  tags = {
    Project = "STR-002 H3"
  }
}

# 2. AWS IoT Core Thing para el Dron
resource "aws_iot_thing" "str002_drone" {
  name = "STR-002-H3-AeroDrone"
  attributes = {
    Model  = "H3-v3.0"
    MTOWKg = "60"
  }
}

# 3. Rol IAM para AWS Lambda (Procesamiento de Alertas / Temperatura ESC)
resource "aws_iam_role" "lambda_iot_role" {
  name = "str002_lambda_iot_execution_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_basic" {
  role       = aws_iam_role.lambda_iot_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# 4. Función AWS Lambda para Validación de Anomalías Térmicas (>75°C)
resource "aws_lambda_function" "telemetry_processor" {
  filename      = "lambda_payload.zip"
  function_name = "str002_telemetry_anomaly_detector"
  role          = aws_iam_role.lambda_iot_role.arn
  handler       = "index.handler"
  runtime       = "python3.11"

  environment {
    variables = {
      TIMESTREAM_DB    = aws_timestreamwrite_database.drone_telemetry_db.database_name
      TIMESTREAM_TABLE = aws_timestreamwrite_table.drone_metrics_table.table_name
    }
  }
}

# 5. Permiso y regla en AWS IoT Core para derivar mensajes MQTT hacia Lambda
resource "aws_lambda_permission" "allow_iot" {
  statement_id  = "AllowExecutionFromIot"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.telemetry_processor.function_name
  principal     = "iot.amazonaws.com"
}

resource "aws_iot_topic_rule" "iot_to_lambda_rule" {
  name        = "str002_telemetry_routing"
  enabled     = true
  sql         = "SELECT * FROM 'drone/str002/telemetry'"
  sql_version = "2016-03-23"

  lambda {
    function_arn = aws_lambda_function.telemetry_processor.arn
  }
}

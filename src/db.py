
import os
import mysql.connector
from pathlib import Path

def get_connection():
    project_root = Path(__file__).resolve().parent.parent
    ca_setting = os.getenv("DB_SSL_CA", "certs/ca.pem")
    ca_path = Path(ca_setting)
    if not ca_path.is_absolute():
        ca_path = project_root / ca_path

    if not ca_path.is_file():
        raise FileNotFoundError(f"CA certificate not found at: {ca_path}")

    host = os.getenv("DB_HOST")
    port = int(os.getenv("DB_PORT", "24888"))
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME", "dmai_nlp")

    if not all([host, user, password, database]):
        raise ValueError("Missing required database environment variables")

    return mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        ssl_ca=str(ca_path),
        ssl_verify_cert=True,
        connection_timeout=15
    )

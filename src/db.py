
import os
import mysql.connector
from pathlib import Path

def get_connection():
    ca_path = os.getenv(
        "DB_SSL_CA",
        str(Path(__file__).resolve().parent.parent / "certs" / "ca.pem")
    )

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
        ssl_ca=ca_path,
        ssl_verify_cert=True,
        connection_timeout=15
    )

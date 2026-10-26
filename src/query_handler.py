
from src.nlp_processor import process_question
from src.db import get_connection

ALLOWED_START = "SELECT "

def handle_question(question):
    sql_query = process_question(question)

    if sql_query is None:
        return None, None, "I couldn't understand that question. Try one of the supported examples."

    normalized_query = sql_query.strip().upper()

    if not normalized_query.startswith(ALLOWED_START):
        return None, None, "This query type is not supported."

    if ";" in sql_query or "--" in sql_query or "/*" in sql_query:
        return None, None, "The generated query failed a safety check."

    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(sql_query)

        columns = [column[0] for column in cursor.description] if cursor.description else []
        rows = cursor.fetchall() if cursor.description else []

        return sql_query, columns, rows

    except Exception as e:
        print(f"Database error: {type(e).__name__}: {e}", flush=True)
        return sql_query, None, "The database could not complete this query. Please check the application logs."

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()

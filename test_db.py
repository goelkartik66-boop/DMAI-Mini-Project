from src.db import get_connection

connection = get_connection()
cursor = connection.cursor()

cursor.execute("SELECT * FROM Students")
rows = cursor.fetchall()

for row in rows:
    print(row)

print(f"\nTotal records: {len(rows)}")

cursor.close()
connection.close()
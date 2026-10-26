
from src.query_handler import handle_question

questions = [
    "Show all students",
    "Show students who scored above 80",
    "Show students from AI",
    "How many students are there?",
    "What is the average marks?"
]

for question in questions:
    print("\nQuestion:", question)

    sql_query, columns, result = handle_question(question)

    print("SQL Query:", sql_query)

    if columns is None:
        print(result)
    else:
        print("Columns:", columns)
        for row in result:
            print(row)

    print("-" * 50)


from src.nlp_processor import process_question

questions = [
    "Show all students",
    "Show students who scored above 80",
    "Find students below 70",
    "How many students are there?",
    "What is the average marks?",
    "Show students from AI",
    "Show students in Delhi",
    "Show students in semester 3"
]

for question in questions:
    print("Question:", question)
    print("SQL:", process_question(question))
    print("-" * 50)
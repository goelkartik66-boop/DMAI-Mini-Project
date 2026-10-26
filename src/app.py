
from flask import Flask, render_template, request
from query_handler import handle_question
import os

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "templates")
)


@app.route("/", methods=["GET", "POST"])
def home():
    question = ""
    sql_query = None
    columns = None
    rows = None
    error = None

    if request.method == "POST":
        question = request.form.get("question", "").strip()

        if question:
            sql_query, columns, result = handle_question(question)

            if columns is None:
                error = result
            else:
                rows = result
        else:
            error = "Please enter a question."

    return render_template(
        "index.html",
        question=question,
        sql_query=sql_query,
        columns=columns,
        rows=rows,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)


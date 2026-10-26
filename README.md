
# DMAI Mini Project: NLP for Database Interaction

## Project Overview
This project allows users to retrieve student information from a MySQL database using natural-language questions through a Flask web application.

## Technologies
- Python
- Flask
- MySQL
- mysql-connector-python
- HTML, CSS and JavaScript

## Project Structure
- `database/` — Database-related files
- `src/` — Flask application, database connection and NLP processing
- `templates/` — HTML templates
- `static/` — Static assets
- `screenshots/` — Application screenshots
- `report/` — Project report
- `requirements.txt` — Python dependencies

## Setup
1. Install Python and MySQL.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the MySQL database connection using the settings expected by the project.
5. Ensure the `dmai_nlp` database and required tables are created.

## Run the Application
From the project root, run:

```bash
set PYTHONPATH=.
python src/app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Features
- Natural-language student database queries
- SQL query display
- Tabular results
- Light and dark themes
- Error handling for unsupported questions

## Team
- Kartik Goel — A25ARIU0019
- Keshav Garg — A25ARIU0021

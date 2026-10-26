
import re

CITIES = {
    "delhi": "Delhi",
    "noida": "Noida",
    "ghaziabad": "Ghaziabad",
    "jaipur": "Jaipur",
    "lucknow": "Lucknow",
    "mumbai": "Mumbai",
    "pune": "Pune",
    "ahmedabad": "Ahmedabad",
    "hyderabad": "Hyderabad",
    "chandigarh": "Chandigarh",
    "amritsar": "Amritsar",
    "bengaluru": "Bengaluru",
    "bangalore": "Bengaluru",
    "kochi": "Kochi",
    "indore": "Indore",
    "kolkata": "Kolkata",
    "bhopal": "Bhopal",
    "patna": "Patna",
    "chennai": "Chennai",
    "bhubaneswar": "Bhubaneswar",
    "nagpur": "Nagpur",
    "dehradun": "Dehradun",
    "thiruvananthapuram": "Thiruvananthapuram",
    "varanasi": "Varanasi",
    "surat": "Surat",
    "ranchi": "Ranchi"
}

def process_question(question):
    question = question.lower().strip()
    question = re.sub(r"[?!.,]+$", "", question)
    question = re.sub(r"\s+", " ", question)

    if not question:
        return None

    if re.search(r"\b(drop|delete|truncate|update|insert|alter|create|replace|remove)\b", question):
        return None

    if re.search(r"\b(weather|temperature|forecast)\b", question):
        return None

    if re.search(r"\b(attendance|present|absent)\b", question):
        attendance_match = re.search(
            r"\b(below|under|less than|lower than|above|over|greater than|more than|higher than|at least|at most|equal to|exactly)\s+(\d+(?:\.\d+)?)\s*%?",
            question
        )

        if not attendance_match:
            return None

        phrase = attendance_match.group(1)
        value = float(attendance_match.group(2))

        if phrase in ("below", "under", "less than", "lower than"):
            operator = "<"
        elif phrase in ("above", "over", "greater than", "more than", "higher than"):
            operator = ">"
        elif phrase == "at least":
            operator = ">="
        elif phrase == "at most":
            operator = "<="
        else:
            operator = "="

        return f"SELECT * FROM Students WHERE Attendance {operator} {value:g}"

    city_match = re.search(
        r"\b(" + "|".join(re.escape(city) for city in sorted(CITIES, key=len, reverse=True)) + r")\b",
        question
    )

    department_match = re.search(r"\b(ai|cse|ece)\b", question)
    semester_match = re.search(r"\bsemester\s+(\d+)\b", question)

    conditions = []

    if city_match:
        conditions.append(f"City = '{CITIES[city_match.group(1)]}'")

    if department_match:
        conditions.append(f"Department = '{department_match.group(1).upper()}'")

    if semester_match:
        conditions.append(f"Semester = {int(semester_match.group(1))}")

    marks_range = re.search(
        r"\b(?:marks|scores?|scored)?\s*(?:between|from)\s+(\d+(?:\.\d+)?)\s+(?:and|to)\s+(\d+(?:\.\d+)?)\b",
        question
    )

    if marks_range:
        low = min(float(marks_range.group(1)), float(marks_range.group(2)))
        high = max(float(marks_range.group(1)), float(marks_range.group(2)))
        conditions.append(f"Marks BETWEEN {low:g} AND {high:g}")
    else:
        marks_match = re.search(
            r"\b(above|over|greater than|more than|exceed(?:s|ing)?|higher than|below|under|less than|lower than|at least|at most|equal to|exactly)\s+(\d+(?:\.\d+)?)\b",
            question
        )

        if marks_match:
            phrase = marks_match.group(1)
            value = float(marks_match.group(2))

            if phrase in ("above", "over", "greater than", "more than", "exceed", "exceeds", "exceeding", "higher than"):
                operator = ">"
            elif phrase in ("below", "under", "less than", "lower than"):
                operator = "<"
            elif phrase == "at least":
                operator = ">="
            elif phrase == "at most":
                operator = "<="
            else:
                operator = "="

            conditions.append(f"Marks {operator} {value:g}")

    if re.search(r"\b(class|overall)\s+average\b|\baverage\s+marks\s+of\s+(?:the\s+)?class\b", question):
        if re.search(r"\b(exceed|exceeds|exceeding|above|higher than|greater than|more than)\b", question):
            return "SELECT * FROM Students WHERE Marks > (SELECT AVG(Marks) FROM Students)"

    if re.search(r"\b(which|what)\s+department\b", question) and re.search(r"\b(highest|maximum|best|top)\b", question) and re.search(r"\baverage\b", question):
        return "SELECT Department, AVG(Marks) AS average_marks FROM Students GROUP BY Department ORDER BY average_marks DESC LIMIT 1"

    if re.search(r"\b(how many|count|number of)\b.*\b(students|records)\b", question):
        sql = "SELECT COUNT(*) AS total_students FROM Students"
        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        return sql

    if re.search(r"\b(failed|fail|failing)\b", question):
        sql = "SELECT * FROM Students WHERE Marks < 40"
        if conditions:
            sql += " AND " + " AND ".join(conditions)
        return sql

    if re.search(r"\b(exceptionally well|outstanding|excellent performance)\b", question):
        sql = "SELECT * FROM Students WHERE Marks >= 90"
        if conditions:
            sql += " AND " + " AND ".join(conditions)
        return sql + " ORDER BY Marks DESC"

    if re.search(r"\b(average|avg|mean)\b", question):
        sql = "SELECT AVG(Marks) AS average_marks FROM Students"
        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        return sql

    if re.search(r"\b(highest|maximum|max)\b.*\b(marks|scores?)\b", question):
        sql = "SELECT MAX(Marks) AS highest_marks FROM Students"
        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        return sql

    if re.search(r"\b(lowest|minimum|min)\b.*\b(marks|scores?)\b", question):
        sql = "SELECT MIN(Marks) AS lowest_marks FROM Students"
        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        return sql

    top_match = re.search(r"\b(?:top|first)\s+(\d+)\b", question)

    if top_match or re.search(r"\b(best-performing|highest-scoring)\b", question):
        limit = int(top_match.group(1)) if top_match else 1
        limit = min(max(limit, 1), 100)
        sql = "SELECT * FROM Students"
        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        return sql + f" ORDER BY Marks DESC LIMIT {limit}"

    if re.search(r"\b(sort|order|arrange)\b", question):
        if re.search(r"\b(name|alphabetically)\b", question):
            order_by = "Name ASC"
        elif re.search(r"\b(ascending|lowest first|smallest first)\b", question):
            order_by = "Marks ASC"
        elif re.search(r"\b(descending|highest first|largest first)\b", question):
            order_by = "Marks DESC"
        else:
            return None

        sql = "SELECT * FROM Students"
        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        return sql + " ORDER BY " + order_by

    if re.search(r"\b(student|students|class|records|people|who|which)\b", question):
        if not re.search(r"\b(show|list|find|display|get|give|tell|all|student|students|who|which)\b", question) and not conditions:
            return None

        if re.search(r"\bfrom\b", question) and not city_match and not department_match:
            return None

        sql = "SELECT * FROM Students"
        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        return sql

    if conditions:
        return "SELECT * FROM Students WHERE " + " AND ".join(conditions)

    return None

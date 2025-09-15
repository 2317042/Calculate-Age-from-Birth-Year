from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

# HTML directly inside Python
html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Age Calculator</title>
</head>
<body>
    <h1>Calculate Age</h1>
    <form method="POST">
        <input type="text" name="birth_year" placeholder="Enter Birth Year">
        <button type="submit">Calculate</button>
    </form>
    {% if age is not none %}
        <p>Your Age: {{ age }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    age = None
    if request.method == "POST":
        birth_year = request.form.get("birth_year")
        if birth_year and birth_year.isdigit():
            current_year = datetime.now().year
            age = current_year - int(birth_year)
    return render_template_string(html_code, age=age)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


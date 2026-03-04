from flask import Flask, render_template, request

app = Flask(__name__)

# store last 5 calculations
history = []

# Home Route
@app.route("/")
def home():
    return render_template("home.html")


# Calculation Route
@app.route("/calculate", methods=["POST"])
def calculate():

    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    operation = request.form["operation"]

    result = ""

    if operation == "add":
        result = num1 + num2

    elif operation == "subtract":
        result = num1 - num2

    elif operation == "multiply":
        result = num1 * num2

    elif operation == "divide":
        if num2 == 0:
            result = "Cannot divide by zero"
        else:
            result = num1 / num2

    # store history
    calculation = f"{num1} {operation} {num2} = {result}"
    history.append(calculation)

    if len(history) > 5:
        history.pop(0)

    return render_template(
        "result.html",
        num1=num1,
        num2=num2,
        operation=operation,
        result=result
    )


# Greeting Route
@app.route("/greet/<username>")
def greet(username):
    return render_template("greet.html", username=username)


# History Route
@app.route("/history")
def show_history():
    return render_template("history.html", history=history)


# Error handling for GET /calculate
@app.route("/calculate", methods=["GET"])
def calculate_error():
    return "<h2>Method Not Allowed</h2>"


if __name__ == "__main__":
    app.run(debug=True)
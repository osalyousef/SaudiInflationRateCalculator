from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/calculate", methods=["POST"])
def calculate():
    now_num = float(request.form["input1"])  # Corrected variable name
    date = request.form["input2"]

    # Fetch annual inflation data from a reliable source
    # (Replace with API call or database lookup based on your implementation)
    inflation_rate = 2.364  # Example value (adjust for actual data)

    # Calculate future value using the formula (consider error handling)
    try:
        future_value = now_num * inflation_rate
    except ZeroDivisionError:
        future_value = "Error: Inflation rate cannot be zero."
    except ValueError:
        future_value = "Error: Invalid input. Please enter a valid number."
    
    return render_template('index.html', result=future_value)

if __name__ == "__main__":
    app.run(debug=True)

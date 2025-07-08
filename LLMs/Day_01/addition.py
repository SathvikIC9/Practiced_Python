from flask import Flask, request
app = Flask(__name__)
@app.route('/length')
def square():
    num1 = request.args.get('x')
    num2 = request.args.get('y')

    if num1 is None or num2 is None:
        return f"Please provide a number using ?num =...",400
    try:
        number1 = int(num1)
        number2 = int(num2)
        return f"{number1}+{number2}={number1+number2}"
    except ValueError:
        return "Invalid Input",400
if __name__ == "__main__":
    app.run(debug=True)
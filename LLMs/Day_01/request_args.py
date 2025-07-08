from flask import Flask, request
app = Flask(__name__)
@app.route('/square')
def square():
    num = request.args.get('num')
    if num is None:
        return f"Please provide a number using ?num =...",400
    try:
        number = int(num)
        return f"The square of the number {number} is {number**2}"
    except ValueError:
        return "Invalid Input",400
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request
app = Flask(__name__)
@app.route('/length')
def square():
    num = request.args.get('num')
    if num is None:
        return f"Please provide a number using ?num =...",400
    try:
        number = (num)
        return f"The Length of the string {number} is {len(number)}"
    except ValueError:
        return "Invalid Input",400
if __name__ == "__main__":
    app.run(debug=True)
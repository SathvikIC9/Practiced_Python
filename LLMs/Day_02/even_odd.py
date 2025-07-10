from flask import Flask,request
app = Flask(__name__)
@app.route('/even')
def check():
    num = request.args.get('num')
    if num is None:
        return "Bro pls enter the value i beg u T-T..."
    try:
        number = int(num)
        if number % 2 == 0:
            return f"The number {number} is even."
        else:
            return "Not an even number"
    except ValueError:
        return "Enter proper value pls "
if __name__ == '__main__':
    app.run(debug=True)

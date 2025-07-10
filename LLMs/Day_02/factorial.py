from flask import Flask,request
app = Flask(__name__)
@app.route('/factorial')
def check():
    num = request.args.get('num')
    if num is None:
        return "Bro pls enter the value i beg u T-T..."
    try:
        number = int(num)
        fact = 1
        n = number
        while n>1:
            fact = fact*n
            n = n-1
        return f"Factorial of the number {number} is {fact}"

    except ValueError:
        return "Enter proper value pls "
if __name__ == '__main__':
    app.run(debug=True)

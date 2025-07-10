from flask import Flask,request
app = Flask(__name__)
@app.route('/prime')
def check():
    num = request.args.get('num')
    if num is None:
        return "Bro pls enter the value i beg u T-T..."
    try:
        number = int(num)
        n = number
        if n <= 1:
            return "Not a prime"
        else:
            i = 2
            is_prime = True
            while i <= n//2:
                if n % i == 0 :
                    is_prime = False
                    break
                i += 1
        if is_prime:
            return f" {n} is a prime number."
        else:
            return "Not a prime."


    except ValueError:
        return "Enter proper value pls "
if __name__ == '__main__':
    app.run(debug=True)
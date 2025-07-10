from flask import Flask, request

app = Flask(__name__)

@app.route('/product', methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
    else:
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')

    if not num1 or not num2:
        return '''
            <form method="post">
                Enter number 1: <input type="text" name="num1"><br>
                Enter number 2: <input type="text" name="num2"><br>
                <input type="submit" value="Find Product">
            </form>
            <p style="color:red;">Bro please enter both numbers 🙏</p>
        '''

    try:
        number1 = int(num1)
        number2 = int(num2)
        result = number1 * number2
        return f'''
            <form method="post">
                Enter number 1: <input type="text" name="num1"><br>
                Enter number 2: <input type="text" name="num2"><br>
                <input type="submit" value="Find Product">
            </form>
            <p>Product of {number1} and {number2} is <strong>{result}</strong></p>
        '''
    except ValueError:
        return '''
            <form method="post">
                Enter number 1: <input type="text" name="num1"><br>
                Enter number 2: <input type="text" name="num2"><br>
                <input type="submit" value="Find Product">
            </form>
            <p style="color:red;">Please enter valid integers 😭</p>
        '''

if __name__ == '__main__':
    app.run(debug=True)

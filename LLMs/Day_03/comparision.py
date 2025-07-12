from flask import Flask, request

app = Flask(__name__)

@app.route('/range', methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        n1 = request.form.get('input1')
        n2 = request.form.get('input2')

        try:
            value1 = int(n1)
            value2 = int(n2)

            if value1 > value2:
                result = f"{value1} is greater than {value2}."
            elif value1 < value2:
                result = f"{value1} is lesser than {value2}."
            else:
                result = "Both are equal."

        except ValueError:
            result = "❌ Enter valid numbers, not strings!"

        return f'''
            <form method="post">
                Enter first number: <input type="text" name="input1"><br>
                Enter second number: <input type="text" name="input2"><br>
                <input type="submit" value="Compare">
            </form>
            <p>{result}</p>
        '''

    return '''
        <form method="post">
            Enter first number: <input type="text" name="input1"><br>
            Enter second number: <input type="text" name="input2"><br>
            <input type="submit" value="Compare">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

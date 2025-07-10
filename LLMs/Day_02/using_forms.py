from flask import Flask, request

app = Flask(__name__)

@app.route('/prime', methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        num = request.form.get('num')
    else:
        num = request.args.get('num')

    if num is None or num.strip() == '':
        return '''
            <form method="post">
                Enter a number: <input type="text" name="num">
                <input type="submit" value="Check Prime">
            </form>
            <p style="color:red;">Bro pls enter the value I beg u T-T...</p>
        '''

    try:
        n = (num)
        word = n[::-1]
        
        result = f"{word} is the reverse of the word {n}."

        return f'''
            <form method="post">
                Enter a number: <input type="text" name="num">
                <input type="submit" value="Check Prime">
            </form>
            <p>{result}</p>
        '''

    except ValueError:
        return '''
            <form method="post">
                Enter a number: <input type="text" name="num">
                <input type="submit" value="Check Prime">
            </form>
            <p style="color:red;">Enter a proper numeric value pls 🙏</p>
        '''

if __name__ == '__main__':
    app.run(debug=True)


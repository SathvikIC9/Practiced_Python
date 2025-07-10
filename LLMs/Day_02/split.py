from flask import Flask, request

app = Flask(__name__)

@app.route('/reverse', methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        str = request.form.get('str')
    else:
        str = request.args.get('str')

    if str is None or str.strip() == '':
        return '''
            <form method="post">
                Enter a number: <input type="text" name="str">
                <input type="submit" value="Check Prime">
            </form>
            <p style="color:red;">Bro pls enter the value I beg u T-T...</p>
        '''

    try:
        # Let's split the input into 3 parts based on index
        # part1 = str[:2]
        part2 = str[2:5]
        # part3 = str[5:]

        return f'''
            <form method="post">
                Enter a string: <input type="text" name="str">
                <input type="submit" value="Split It!">
            </form>
            <p>Original: {str}</p>
            <p>Split:  [{part2}] </p>
        '''

    except Exception:
        return '''
            <form method="post">
                Enter a string: <input type="text" name="str">
                <input type="submit" value="Split It!">
            </form>
            <p style="color:red;">Something went wrong. Try again!</p>
        '''

if __name__ == '__main__':
    app.run(debug=True)
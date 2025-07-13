from flask import Flask,request
app = Flask(__name__)
@app.route('/range', methods=['GET','POST'])
def check():
    if request.method == 'POST':
        n = request.form.get('input')
        try:
            value = int(n)

            if value > 0 and value <= 9:
                return f"The value {value} lies in the range 0 - 9. "
            elif value > 9 and value <= 20:
                return f"The value {value} lies in the range 10 - 20."
            else:
                return "Sorry couldn't generate"
        except ValueError:
            return "Enter a number not a string"
    return '''
        <form method="post">
            Enter something: <input type="text" name="input">
            <input type="submit" value="Check Type">
        </form>
    '''
if __name__ =="__main__":
    app.run(debug=True)
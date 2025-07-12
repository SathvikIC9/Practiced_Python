from flask import Flask,request
app = Flask(__name__)
@app.route('/marks', methods=['GET','POST'])
def check():
    if request.method == 'POST':
        n = request.form.get('input')
        try:
            value = int(n)

            if value >  90 and value <= 100:
                return f"The student with {value} marks has secured A grade "
            elif value > 80 and value <= 89:
                return f"The student with {value} marks has secured B grade "
            elif value > 70 and value <= 79:
                return f"The student with {value} marks has secured C grade "
            else:
                return "Sorry You secured F grade."
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
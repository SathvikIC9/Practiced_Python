from flask import Flask , request
app = Flask(__name__)
@app.route('/countdown' ,methods =['POST','GET'])
def counter():
    if request.method == 'POST':
        try:
            value = int(request.form.get('input'))
            integer = []
            while value >= 0 :
                integer.append(value)
                value -= 1
            return f"{integer}"
        except ValueError:
            return " Please enter a value"
        
    return '''
    <form method="post">
            Enter something: <input type="text" name="input">
            <input type="submit" value="Check Type">
        </form>
    '''
if __name__== '__main__':
    app.run(debug=True)
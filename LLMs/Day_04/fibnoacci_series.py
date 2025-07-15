from flask import Flask , request
app = Flask(__name__)
@app.route('/countdown' ,methods =['POST','GET'])
def counter():
    if request.method == 'POST':
        try:
            value = int(request.form.get('input'))
            a, b = 0, 1
            count = 0
            fib = []
            while count < value:
                fib.append(str(a)) 
                a,b = b , a+b 
                count += 1
            result = ' '.join(fib)
            return f"{result}"

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
from flask import Flask , request
app = Flask(__name__)
@app.route('/counting' ,methods =['POST','GET'])
def counter():
    if request.method == 'POST':
        try:
            value = request.form.get('input')
            value = list(map(int,value.strip().split()))
            avg_value = (sum(value)) // len(value)
            minimum = min(value)
            maximum = max(value)
            return f"{avg_value} is the avg . {minimum} is minimum. {maximum} is the maximum."

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
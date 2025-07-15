from flask import Flask,request
app = Flask(__name__)
@app.route('/limit', methods =['POST','GET'])
def limit():
    if request.method == 'POST':
        try:
            value = int(request.form.get('input'))
            b = []
            while value >= 0 :
                b.append(value) 
                value -= 1
            a = sum(b)
            return f"{a}"
        except ValueError:
            return "Enter correct value pls."
    return '''
     <form method="post" target="_blank">
            Enter something: <input type="text" name="input">
            <input type="submit" value="Check Type" >
        </form>
    '''
if __name__== "__main__":
    app.run(debug=True)
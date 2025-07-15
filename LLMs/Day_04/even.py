from flask import Flask , request
app = Flask(__name__)
@app.route('/countdown' ,methods =['POST','GET'])
def counter():
    if request.method == 'POST':
        try:
            value = int(request.form.get('input'))
            my_list = []
            i = 0 
            while i <= value:
                if i % 2 == 0:
                    my_list.append(i)
                i += 1

            return f"{my_list}"

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
from flask import Flask , request
app = Flask(__name__)
@app.route('/counting' ,methods =['POST','GET'])
def counter():
    if request.method == 'POST':
        try:
            value = request.form.get('input')
            # value = value.split()
            my_dict = {}
            for char in value:
                if char == ' ':
                    continue  # Skip spaces
                if char in my_dict:
                    my_dict[char] += 1
                else:
                    my_dict[char] = 1
            return f"{my_dict}"

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
from flask import Flask,request
app = Flask(__name__)
@app.route('/check', methods=['GET','POST'])
def check():
    if request.method == 'POST':
        value =request.form.get('input')

        if value.isdigit():
            return f"<p> {value} is an Integer.</p>"
        elif value.isalpha():
            return f"<p> {value} is a String.</p>"
        else:
            return 'Mixed characters'
    
    return '''
        <form method="post">
            Enter something: <input type="text" name="input">
            <input type="submit" value="Check Type">
        </form>
    '''
if __name__ == "__main__":
    app.run(debug=True)
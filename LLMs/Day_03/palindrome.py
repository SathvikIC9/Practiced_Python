from flask import Flask,request
app = Flask(__name__)
@app.route('/check', methods=['GET','POST'])
def check():
    if request.method == 'POST':
        value =request.form.get('input')
        value_lower = value.lower()

        reversed_value = value_lower[::-1]

        if value_lower == reversed_value:
            return f"The word {value} is a palindrome."
        else:
            return "its not a palindrome"
    
    return '''
        <form method="post">
            Enter something: <input type="text" name="input">
            <input type="submit" value="Check Type">
        </form>
    '''
if __name__ == "__main__":
    app.run(debug=True)
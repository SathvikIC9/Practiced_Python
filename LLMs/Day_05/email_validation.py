from flask import Flask, request

app = Flask(__name__)

@app.route('/validation', methods=['GET', 'POST'])
def formating():
    if request.method == "POST":
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            age = int(request.form.get('age'))
            char = "@"
            if char in email and age >= 18:
                    return f"Hi {name}. You may proceed."
            else:
                 return " Sorry you arent eligible."
        except (ValueError,TypeError):
             return "Please enter correct value"

    return '''
        <form method="post" target="_blank">
            Enter your name: <input type="text" name="name"><br>
            Enter your mail: <input type="text" name="email"><br>
            Enter your age: <input type="text" name="age"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

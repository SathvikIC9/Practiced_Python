from flask import Flask, request

app = Flask(__name__)

@app.route('/format', methods=['GET', 'POST'])
def formating():
    if request.method == "POST":
        try:
            name = request.form.get('name')
            age = int(request.form.get('age'))
            return f"Hi, my name is {name} and my age is {age}."
        except (ValueError, TypeError):
            return "Enter correct value."

    return '''
        <form method="post" target="_blank">
            Enter your name: <input type="text" name="name"><br>
            Enter your age: <input type="text" name="age"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

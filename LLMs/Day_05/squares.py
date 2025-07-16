from flask import Flask, request

app = Flask(__name__)

@app.route('/format', methods=['GET', 'POST'])
def formating():
    if request.method == "POST":
        try:
            num = int(request.form.get('num'))
            b = []
            while num == 0 :
                squares =  num*num
                b.append(squares)  
                num -= 1

            return f"{b}"              

        except (ValueError, TypeError):
            return "Enter correct value."

    return '''
        <form method="post" target="_blank">
            Enter your name: <input type="text" name="name"><br>

            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def formating():
    if request.method == "POST":
        try:
            num_str = request.form.get('num')
            num = int(num_str.strip())  

            b = []
            while num >= 0:
                if num % 2 == 0: 
                    b.append(num)
                num -= 1
            b.sort()

            return f"Even numbers from input : {b}"

        except (ValueError, TypeError):
            return "Enter a valid number."

    return '''
        <form method="post" target="_blank">
            Enter a number: <input type="text" name="num"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

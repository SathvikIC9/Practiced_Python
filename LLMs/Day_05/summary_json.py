from flask import Flask, jsonify,request

app = Flask(__name__)

@app.route('/summary', methods=['GET', 'POST'])
def formating():
    if request.method == "POST":
        try:

            age = request.form.get('age')
            my_set = list(map(int,age.strip().split()))
            maximum = max(my_set)
            minimum = min(my_set)
            add = sum(my_set)

            return jsonify({
                "maximum": maximum,
                "minimum": minimum,
                "total":add,
                "original list":my_set

            })
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

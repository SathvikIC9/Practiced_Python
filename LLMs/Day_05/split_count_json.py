from flask import Flask, jsonify,request

app = Flask(__name__)

@app.route('/summary', methods=['GET', 'POST'])
def formating():
    if request.method == "POST":
        try:
            name = request.form.get('name')  
            if not name:
                return "Please enter your name."

            word_list = name.split()
            word_count = len(word_list)
            return jsonify({"word count": word_count,
                            "words": word_list})
        except Exception as e:
            return f"Error: {str(e)}"

    return '''
        <form method="post" target="_blank">
            Enter your name: <input type="text" name="name"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask,request
app = Flask(__name__)
@app.route('/length', methods=['GET','POST'])
def check():
    if request.method == 'POST':
        value =request.form.get('input')
        value_split = value.split()
        # n = len(value_split)
        result = any(word.endswith('le') for word in value_split)
        if result:
            return f"'le' is there in the word {value}"
        else:
            return "No there is no 'le' in this word."
    
    return '''
        <form method="post">
            Enter something: <input type="text" name="input">
            <input type="submit" value="Check Type">
        </form>
    '''
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask,request
app = Flask(__name__)
@app.route('/length', methods=['GET','POST'])
def check():
    if request.method == 'POST':
        value =request.form.get('input')
        value_split = value.split()
        result = max(value_split, key = len)
        lenght = len(result)
        return f"The word with max length is {result} with the length {lenght}"
    
    return '''
        <form method="post">
            Enter something: <input type="text" name="input">
            <input type="submit" value="Check Type">
        </form>
    '''
if __name__ == "__main__":
    app.run(debug=True)
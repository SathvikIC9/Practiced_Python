from flask import Flask,request
app = Flask(__name__)
@app.route('/',methods =['POST','GET'])
def finder():
    if request.method == 'POST':
        try:
            value = request.form.get('value')
            # split = value.split()
            sentence = request.form.get('sentence')
            if value in sentence:
                return "Found ✅"
            else:
                return "Not found ❌"
            
            
        except Exception as e:
            return f" Error ...ENTER PROPER VALUE...{str(e)}"
    return '''
    <form method="post">
            Enter something: <input type="text" name="value">
            Enter something: <input type="sentence" name="sentence">
            <input type="submit" value="Check Type">
        </form>
    '''
if __name__ == "__main__":
    app.run(debug=True)

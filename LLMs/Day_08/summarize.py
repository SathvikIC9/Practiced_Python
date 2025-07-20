from flask import Flask,request
app = Flask(__name__)
@app.route('/',methods =['POST','GET'])
def finder():
    if request.method == 'POST':
        # result = ''
        try:
            value = request.form.get('value')
            value = value.split()
            count = len(value)
            first_word = value[0]
            last_word = value[-2]
            if value[-1] == '.':
                return f"{count} is the number of words \n {first_word} is the first word in the sentence \n {last_word} is the last word \n HANJII!!!! its there."
            else:
                return f"{count} is the number of words \n {first_word} is the first word in the sentence \n {last_word} is the last word \n NAHI HAI !!!!"
            
            
        except Exception as e:
            return f" Error ...ENTER PROPER VALUE...{str(e)}"
    return '''
    <form method="post">
            Enter something: <input type="text" name="value">
            <input type="submit" value="Check Type">
        </form>
    '''
if __name__ == "__main__":
    app.run(debug=True)

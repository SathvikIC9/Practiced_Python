'''
? - seemss like a question
how /what - u seem curious
why - thats deep
'''
from flask import Flask,request
app = Flask(__name__)
@app.route('/',methods =['POST','GET'])
def finder():
    if request.method == 'POST':
        try:
            value = request.form.get('value')
            value = value.lower()
            if '?' in value :
                return "Seems like a Question"
            elif "how" in value:
                return "U look curious"
            elif "what" in value:
                return "U look curious"
            elif "why" in value:
                return "Thats deep!"
            else:
                return "Intresting...."
            
            
            
        except Exception as e:
            return f" Error ...ENTER PROPER VALUE...{str(e)}"
    return '''
    <form method="post" target ="__blank">
            Enter something: <input type="text" name="value">
            <input type="submit" value="Check Type">
        </form>
    '''
if __name__ == "__main__":
    app.run(debug=True)

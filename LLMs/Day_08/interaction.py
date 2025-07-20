from flask import Flask,request
app = Flask(__name__)
@app.route('/',methods =['POST','GET'])
def finder():
    if request.method == 'POST':
        try:
            value = request.form.get('value')
            value = value.lower()
            if value == 'hello':
                return "Hi!"
            elif value == 'bye':
                return "God Bye"
            elif value == 'thanks':
                return "You;re Welcome!"
            else:
                return "Sry i dint understand."
            
            
            
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

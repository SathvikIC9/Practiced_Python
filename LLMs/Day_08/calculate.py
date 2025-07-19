from flask import Flask,request
app = Flask(__name__)
@app.route('/',methods =['POST','GET'])
def finder():
    if request.method == 'POST':
        try:
            value = request.form.get('value')  
            tokens = value.split()           

            num1 = int(tokens[0])
            operator = tokens[1]
            num2 = int(tokens[2])

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 // num2         
            else:
                result = "Unsupported operator"

            return f"Result: {result}"
            
            
            
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

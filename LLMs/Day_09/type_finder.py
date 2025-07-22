from flask import Flask,request
app = Flask(__name__)
@app.route('/typeCheck',methods = ['POST','GET'])
def extractor():
    result=''
    if request.method =='POST':
        try:
            value = request.form.get('value')
            integer = value.isdigit()
            alphabet = value.isalpha()
            decimal = float(value)
            if value == '':
                result = "Input cannot be empty."
            elif value.isdigit():
                result = f"{value} is an Integer."
            elif value.replace('.', '', 1).isdigit() and value.count('.') == 1:
                result = f"{value} is a Decimal."
            elif value.isalpha():
                result = f"{value} is Alphabetic."
            else:
                result = "I don't know bruv..."
        except Exception as e:
            return F"THIK SE LIKH BHAI {e}"
    return f'''
<form method="post" target="_blank">
    Enter the value : <input type="name" name="value">
    <input type="submit" value="Check"><br>
    <div>{result}</div>
</form>
'''
if __name__ == "__main__":
    app.run(debug=True)
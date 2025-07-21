from flask import Flask,request
app = Flask(__name__)
@app.route('/extractemail',methods = ['POST','GET'])
def extractor():
    result=''
    if request.method =='POST':
        try:
            value = request.form.get('value')
            values = value.strip().split()
            if "@" and ".com" in value:
                result = f"{values[-1]}"
            else:
                result= "Enter proper value."
        except Exception as e:
            return F"THIK SE LIKH BHAI {e}"
    return f'''
<form method="post" target="_blank">
    Enter your detials : <input type="name" name="value">
    <input type="submit" value="Check"><br>
    <div>{result} is yr email</div>
</form>
'''
if __name__ == "__main__":
    app.run(debug=True)
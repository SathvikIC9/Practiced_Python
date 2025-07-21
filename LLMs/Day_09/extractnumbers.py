from flask import Flask,request
app = Flask(__name__)
@app.route('/userinputbot',methods = ['POST','GET'])
def extractor():
    result=''
    if request.method =='POST':
        try:
            value = request.form.get('value')
            values = value.strip().split()
            my_set = []
            has_number = any(token.isdigit() for token in values)
            for token in has_number:
                my_set.append(token)
            result = my_set
            
        except Exception as e:
            return F"THIK SE LIKH BHAI {e}"
    return f'''
<form method="post" target="_blank">
    Enter your detials : <input type="name" name="value">
    <input type="submit" value="Check"><br>
    <div>{result}</div>
</form>
'''
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route('/tokeninfo',methods = ['POST','GET'])
def extractor():
    if request.method =='POST':
        try:
            value = request.form.get('value')
            values = value.strip().split()
            return jsonify({
                "tokens":values,
                "length":len(values),
                "Maximum":max(values, key=len)
                })
        except Exception as e:
            return F"THIK SE LIKH BHAI {e}"
    return f'''
<form method="post" target="_blank">
    Enter your detials : <input type="name" name="value">
    <input type="submit" value="Check"><br>
    
</form>
'''
if __name__ == "__main__":
    app.run(debug=True)
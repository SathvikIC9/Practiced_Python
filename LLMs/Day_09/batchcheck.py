from flask import Flask,request
app = Flask(__name__)
@app.route('/checker',methods = ['POST','GET'])
def extractor():
    result=''
    if request.method =='POST':
        try:
            value = request.form.get('value')             
            punctuation = ["!","?","."]
            dict_check ={}
            for values in value:
                if values in punctuation:
                    if values in dict_check:
                        dict_check[values] += 1
                    else:
                        dict_check[values] = 1
            
            
            result = f'{dict_check}'
                
            
        except Exception as e:
            return F"THIK SE LIKH BHAI {e}"
    return f'''
<form method="post" target="_blank">
    Enter your detials : <textarea type="textarea" name="value"></textarea><br>
    <input type="submit" value="Check"><br>
    <div>{result}</div>
</form>
'''
if __name__ == "__main__":
    app.run(debug=True)
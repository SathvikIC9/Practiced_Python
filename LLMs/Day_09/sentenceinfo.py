from flask import Flask,request
app = Flask(__name__)
@app.route('/counter',methods = ['POST','GET'])
def extractor():
    result=''
    if request.method =='POST':
        try:
            value = request.form.get('value')
            values = value.strip().split()
            val = value.strip('')
            count = len(values)
            length = []
            for word in values:
                length.append(len(word))
            total = sum(length)
            average = sum(length)//count
            result = f"the total number of words are: {total}. Average word count is {float(average)}. The sentence is: {value}  "

            
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
from flask import Flask, request
app = Flask(__name__)

@app.route('/clear', methods=['GET', 'POST'])
def remember():
    result = ""
    if request.method == 'POST':
        try:
            value = request.form.get('value')  # matches input name
            with open('question.txt','w') as f:
                f.write('')
            
            result = "Okay noted.. 👍"
        except Exception:
            result = "Oops"
        
    return f'''
    <form method="post">
        <input type="submit">
        <div>{result}</div>            
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

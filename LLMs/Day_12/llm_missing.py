from flask import Flask, request
app = Flask(__name__)

@app.route('/missing', methods=['GET', 'POST'])
def remember():
    result = ""
    if request.method == 'POST':
        try:
            value = request.form.get('value')  
            if value == "memory":
                with open('missing.txt') as f:
                    content = f.readlines()

            result =content
            
            result = "Okay noted.. 👍"
        except Exception:
            result = "Oops the file wasnt found."
        
    return f'''
    <form method="post">
        Enter your name: <input name="value" type="text">
        <input type="submit">
        <div>{result}</div>            
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

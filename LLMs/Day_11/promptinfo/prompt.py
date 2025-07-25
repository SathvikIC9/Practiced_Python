from flask import Flask, request
app = Flask(__name__)

@app.route('/question', methods=['GET', 'POST'])
def remember():
    result = ""
    if request.method == 'POST':
        try:
            value = request.form.get('value')  
            # asked = value.split()
            # word = asked[-1]
            with open('promptinfo/poem.txt') as f:
                content = f.read()

            if value == "write a poem on flask.":
                result = content
            else:
                result = "Sorry I aint that good at literature. 😭"
                

        except Exception:
            result = "Oops"
        
    return f'''
    <form method="post">
        Enter your name: <input name="value" type="text">
        <input type="submit">
        <pre>Here is the poem you asked</pre>
        <div>{result}</div>            
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

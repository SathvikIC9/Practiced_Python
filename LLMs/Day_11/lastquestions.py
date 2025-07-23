from flask import Flask, request
app = Flask(__name__)

@app.route('/lastquestion', methods=['GET', 'POST'])
def remember():
    result = ""
    if request.method == 'POST':
        try:
            with open('question.txt') as f:
                content = f.readlines()

            result =content
            
            
        except Exception:
            result = "Oops"
        
    return f'''
    <form method="post">
        <div>{result}</div>            
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

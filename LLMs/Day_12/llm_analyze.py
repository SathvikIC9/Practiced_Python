from flask import Flask, request
import pyjokes

app = Flask(__name__)

@app.route('/llm_analyze', methods=['GET', 'POST'])
def analyze():
    result = ""
    if request.method == 'POST':
        try:
            value = request.form.get('value')
            value = value.lower()
            if value == 'analyze':
                with open('question.txt') as f:
                    content = f.readlines()
                    question_count = sum(1 for line in content if "?" in line)
                    word_count = sum(len(line.split()) for line in content)
                    result = f"There are {word_count} words in the file.\nThere are {question_count} questions."

        except Exception:
            result = "Oops"
        
    return f'''
    <form method="post">
        Enter your name: <input name="value" type="text">
        <input type="submit">
        <pre>{result}</pre>            
    </form>
    '''
@app.route('/',methods=['GET','POST'])
def remember():
    answer = ""
    if request.method == 'POST':
        try:
            value = request.form.get('value')  
            with open('question.txt','a') as f:
                f.write(value + '\n')
            if value == "memory":
                with open('question.txt') as f:
                    content = f.readlines()

            answer ="<br>".join(content)
            
            answer = "Okay noted.. 👍"
        except Exception:
            answer = "Oops"
        
    return f'''
<form method="post">
        Enter your name: <input name="value" type="text">
        <input type="submit">
        <div>{answer}</div>  
        <div><a href="http://127.0.0.1:5000/llm_analyze">Analyze here</a></div>          
    </form>
    '''
if __name__ == "__main__":
    app.run(debug=True)

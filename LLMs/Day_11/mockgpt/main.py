from flask import Flask, request
import pyjokes

import time

app = Flask(__name__)

@app.route('/askgpt_simple', methods=['GET', 'POST'])
def remember():
    result = ""
    wait = ''
    flask_questions_01 = ["Tell me a joke","Joke"]
    flask_questions_02 = ["Write a poem about flask","Poem on flask"]

    if request.method == 'POST':
        try:
            value = request.form.get('value')
            if value.endswith("?"):
                time.sleep(2)
                wait = "Let me think... 🤔" 
            if any(asked.lower() in value.lower() for asked in flask_questions_01):
                result = pyjokes.get_joke()
            elif any(asked.lower() in value.lower() for asked in flask_questions_02):
                with open("poems.txt") as f:
                    content = f.read()
                    result = content 
            
            else:
                result = "I'm still learning to answer that! 😅"

        except Exception:
            result = "Oops"
        
    return f'''
    <form method="post">
        <h1> Hello there ! How may I help you ?😊 </h1>
        Enter your query: <input name="value" type="text">
        <input type="submit">
        <div>{wait}</div>            
        <div>{result}</div>            
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

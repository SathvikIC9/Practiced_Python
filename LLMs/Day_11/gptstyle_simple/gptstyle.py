from flask import Flask, request

import time

app = Flask(__name__)

@app.route('/askgpt_simple', methods=['GET', 'POST'])
def remember():
    result = ""
    wait = ''
    flask_questions = [
    "Why is Flask popular?",
    "What makes Flask so widely used?",
    "Why do developers prefer Flask?",
    "What are the advantages of using Flask?",
    "Why is Flask a popular web framework?",
    "What's special about Flask compared to others?",
    "Why do people choose Flask for web apps?"
]

    if request.method == 'POST':
        try:
            value = request.form.get('value')
            if value.endswith("?"):
                time.sleep(2)
                wait = "Let me think... 🤔" 
            if any(asked.lower() in value.lower() for asked in flask_questions):
                result = "Flask is popular because it's lightweight, flexible, and easy to get started with!😊"
            else:
                result = "I'm still learning to answer that! 😅"

        except Exception:
            result = "Oops"
        
    return f'''
    <form method="post">
        Enter your name: <input name="value" type="text">
        <input type="submit">
        <div>{wait}</div>            
        <div>{result}</div>            
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

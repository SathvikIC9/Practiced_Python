from flask import Flask, request
import random
import pyjokes

app = Flask(__name__)

@app.route('/askgpt', methods=['GET', 'POST'])
def remember():
    result = ""
    if request.method == 'POST':
        try:
            value = request.form.get('value')
            value = value.lower()
            poem = ['write a poem','poem','give me a poem']
            joke = ['write a joke','joke','tell me a poem']

            if any(phrase in value for phrase in poem):  
                with open('askgpt/poems.txt','r') as f:
                    result = f.read()
            elif any(phrase in value for phrase in joke):
                result = pyjokes.get_joke()
            else:
                result = "Oops dint find that 😅"
        except Exception:
            result = "Oops"
        
    return f'''
    <form method="post">
        Enter your name: <input name="value" type="text">
        <input type="submit">
        <pre>{result}</pre>            
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

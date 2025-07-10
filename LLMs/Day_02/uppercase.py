from flask import Flask, request
app = Flask(__name__)

@app.route('/uppercase')
def home():
    word = request.args.get('word')
    if word is None:
        return f"Please provide a word using ?word=...",400
    try:
        words = (word)
        return f"The new word is {words.upper()}"
    except ValueError:
        return "Enter valid input.",400     

if __name__ == '__main__':
    app.run(debug=True)

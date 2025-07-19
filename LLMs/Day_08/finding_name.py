from flask import Flask,request
app = Flask(__name__)
@app.route("/analyze")
def finder():
    try:
        value = "What is your name?"
        word = 'name'
        if word in value:
            return "I am a flask app."
        else:
            return "I am nothing."
    except Exception as e:
        return f"Error as {str(e)}"
if __name__ == '__main__':
    app.run(debug=True)
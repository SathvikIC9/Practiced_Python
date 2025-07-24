from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/answer', methods=['POST','GET'])
def answer():
    value = request.form.get('value')

    flask_questions = [
        "why is flask popular",
        "what makes flask so widely used",
        "why do developers prefer flask",
        "what are the advantages of using flask",
        "why is flask a popular web framework",
        "what’s special about flask compared to others",
        "why do people choose flask for web apps"
    ]

    if any(q in value for q in flask_questions):
        reply = "Flask is popular because it's lightweight, flexible, and easy to get started with!"
    else:
        reply = "Hmm, I’m still learning to answer that! 😅"

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)

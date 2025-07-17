from flask import Flask,request
app = Flask(__name__)
@app.route('/')
def search():
    with open('data.txt','w') as f :
        f.write("Welcome to my website.\n")

    a = "Welcome to my website"

    with open('data.txt') as f1:
        words = f1.read()
    if a in words:
        return " Sucsess"
    else:
        return "qaf the wak"
if __name__ == "__main__":
    app.run(debug=True)
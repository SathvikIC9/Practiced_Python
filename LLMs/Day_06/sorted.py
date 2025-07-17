from flask import Flask,request
app = Flask(__name__)
@app.route('/')
def search():
    with open('data.txt') as f1:
        words = f1.readlines()
        lower = [word.strip() for word in words]
        length = sorted(lower)
    return '<br>'.join(length)
    
if __name__ == "__main__":
    app.run(debug=True)
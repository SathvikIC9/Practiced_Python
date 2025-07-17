from flask import Flask,request
app = Flask(__name__)
@app.route('/')
def search():
    with open('data.txt') as f :
        words = f.read()
    
    if 'python' in words:
        return "Yes the word is in the file."
    else:
        return "The Word is not in the file."
if __name__ == "__main__":
    app.run(debug=True)
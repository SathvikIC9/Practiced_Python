from flask import Flask,request
app = Flask(__name__)
@app.route('/')
def search():
    with open('data.txt') as f1:
        words = f1.readlines()
        length = len(words)
    return f"{length} are the number of lines in the file."
    
if __name__ == "__main__":
    app.run(debug=True)
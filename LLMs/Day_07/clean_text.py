from flask import Flask 
import string

app = Flask(__name__)
@app.route('/clean')
def spliting():
        try:
            value = "I love Python!"
            a = [value.strip().translate(str.maketrans('', '',string.punctuation)) for a in value]
            return f"{a}"
        except Exception as e :
            return f'Error as {e}'

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request
app = Flask(__name__)
@app.route('/join')
def spliting():
        try:
            value = ['apple','banana','grapes']
            a = " ".join(value)
            return f"{a}"
        except Exception as e :
            return f'Error as {e}'

if __name__ == '__main__':
    app.run(debug=True)
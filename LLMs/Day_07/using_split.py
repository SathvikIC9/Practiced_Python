from flask import Flask, request
app = Flask(__name__)
@app.route('/split')
def spliting():
        try:
            value = "I love Python"
            a = value.split()
            return f"{a}"
        except Exception as e :
            return f'Error as {e}'

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request
app = Flask(__name__)
@app.route('/longest')
def spliting():
        try:
            value = "I love programming in Python"
            value = value.split()
            a = max(value,key=len)
            return f"{a}"
        except Exception as e :
            return f'Error as {e}'

if __name__ == '__main__':
    app.run(debug=True)
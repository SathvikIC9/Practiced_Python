from flask import Flask
app = Flask(__name__)
@app.route("/")
def data_read():
    try:
        with open('data.txt') as f:
            content = f.read()

        return f"{content}"
    except Exception as e:
        return f"Enter correct value as {e}"
    
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
app = Flask(__name__)
@app.route("/")
def data_read():
    try:
        with open('data.txt') as f:
            content = f.read()
            words = content.split()
            count = len(words)
            b = [len(word) for word in words]
        with open('data.txt') as f:
            lines = f.readlines()

            return f"""The number of words in the matter are {count} the number of lines are {lines} and the total word count is {b}."""

        
        return f"{content}"
    except Exception as e:
        return f"Enter correct value as {e}"
    
if __name__ == '__main__':
    app.run(debug=True)
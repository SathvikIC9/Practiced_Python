from flask import Flask, jsonify

app = Flask(__name__) 

@app.route('/')
def formating():
        try:
            numbers = [3,6,9]
            return jsonify(numbers = numbers)

        except (ValueError, TypeError):
            return "Enter a valid number."



if __name__ == '_main_':
    app.run(debug=True)
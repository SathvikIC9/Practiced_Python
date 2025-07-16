from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def formating():
    if request.method == "POST":
        try:
            input_str = request.form.get('num')  # Get input string
            words = input_str.strip().split()  # Split into words
            reversed_chars = [word[::-1] for word in words]  # Reverse each word

            return f"Reversed characters: {reversed_chars}"

        except (ValueError, TypeError):
            return "Enter a valid number."  

    # GET method: show form
    return '''
        <form method="post" target="_blank">
            Enter a number: <input type="text" name="num"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '_main_':
    app.run(debug=True)
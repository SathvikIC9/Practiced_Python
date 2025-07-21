from flask import Flask, request


app = Flask(__name__)

@app.route('/filecheck', methods=['GET', 'POST'])
def extractor():
    result = ''
    if request.method == 'POST':
        try:
            value = request.form.get('value')
            split = value.split()
            if split[0] == 'add':
                result = split[1]+split[2]
            elif split[0] == 'sub':
                result = split[1] - split[2]
            elif split[0] == 'mul':
                result = split[1] * split[2]
            elif split[0] == 'div':
                result = split[1] // split[2]
        except Exception as e:
            result = f"THIK SE LIKH BHAI: {e}"

    return f'''
    <form method="post">
        <input type="submit" value="Check if file is empty"><br><br>
        <div><b>{result}</b></div>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

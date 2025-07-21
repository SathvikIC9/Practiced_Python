from flask import Flask, request


app = Flask(__name__)

@app.route('/filecheck', methods=['GET', 'POST'])
def extractor():
    result = ''
    if request.method == 'POST':
        try:
            file_path = "file.txt"
            with open(file_path, 'r') as f:
                    read = f.read().strip()
                    if read == '':
                        result = "Yes, the file is empty."
                    else:
                        result = "No, the file is not empty."
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

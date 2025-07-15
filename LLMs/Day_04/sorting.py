from flask import Flask, request

app = Flask(__name__)

@app.route('/sorting', methods=['POST', 'GET'])
def counter():
    if request.method == 'POST':
        try:
            value = request.form.get('input')
            word_list = value.strip().split()
            sorted_words = sorted(word_list, key=str.lower)

            return f"Sorted words: {' '.join(sorted_words)}"

        except Exception as e:
            return f"Error: {str(e)}"

    return '''
    <form method="post" target="_blank">
        Enter words: <input type="text" name="input">
        <input type="submit" value="Sort Words">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

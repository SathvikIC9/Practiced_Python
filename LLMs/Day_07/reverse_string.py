from flask import Flask 
app = Flask(__name__)
@app.route('/reverse')
def spliting():
        try:
            value = "one one two three two"
            value = value.split()
            my_list = set(value)
            return f"{my_list}"

        except Exception as e :
            return f'Error as {e}'

if __name__ == '__main__':
    app.run(debug=True)
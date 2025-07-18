from flask import Flask, request
app = Flask(__name__)
@app.route('/fruits')
def spliting():
        try:
            value = "apple banana apple"
            value = value.split()
            my_dict = {}
            for word in value:
                if word in my_dict:
                    my_dict[word] += 1
                else:
                     my_dict[word] = 1
            return f"{my_dict}"
        except Exception as e :
            return f'Error as {e}'

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def formating():
    if request.method == "POST":
        try:
            input_str = request.form.get('num')
            vowels = "aeiouAEIOU"
            split = input_str.split()
            my_list = []
            if vowels in input_str:
                my_list.append(input_str)
            value = (len(my_list)/len(split))*100
            return f"The percentage of vowel is {value}%"
        except (ValueError, TypeError):
            return "Enter a valid number."
    return '''
        <form method="post" target="_blank">
            Enter a number: <input type="text" name="num"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
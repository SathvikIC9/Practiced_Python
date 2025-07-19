from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route('/',methods =['POST','GET'])
def finder():
    if request.method == 'POST':
        try:
            value = request.form.get('value')
            # value = value.lower
            words = value.split()
            my_dict = {}
            for word in words:  
                if word in my_dict:
                    my_dict[word] +=1
                else:
                    my_dict[word] = 1
            return jsonify(my_dict)
            
            
            
        except Exception as e:
            return f" Error ...ENTER PROPER VALUE...{str(e)}"
    return '''
    <form method="post" target ="__blank">
            Enter something: <input type="text" name="value">
            <input type="submit" value="Check Type">
        </form>
    '''
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
app  = Flask(__name__)
@app.route('/help')
def home():
    return "This app is to help people to make themselves better."

if __name__ =='__main__':
    app.run(debug = True)
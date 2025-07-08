from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Welcome to the Home Page</h1>
        <body style="background-color: aqua;"></body>
        <p><a target="__blank" href="/about">Go to About Page</a></p>
        <p><a target="__blank" href="/help">Go to Help Page</a></p>
    '''

@app.route('/about')
def about():
    return '''
        <h1>About Page</h1>
        <p>This app uses Flask and LLMs.</p>
        <p><a href="/">Back to Home</a></p>
    '''

@app.route('/help')
def help_page():
    return '''
        <h1>Help Page</h1>
        <p>This is the help section.</p>
        <label>Message:</label>
        <p> <input type="text" name = "Enter your Quiery"> </p>
        <p><button type="button" name="Submit" width = "1000px" ></button></p>
        <p><a href="/">Back to Home</a></p>
    '''

if __name__ == '__main__':
    app.run(debug=True)

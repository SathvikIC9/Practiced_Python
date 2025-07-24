from flask import Flask, request
app = Flask(__name__)

@app.route('/wlcome', methods=['GET', 'POST'])
def remember():
    result = ""
    try:
        with open("remember.txt", "r") as f1:
            name = f1.read()
                
        result = f"Welcome Back {name} 😁!"

    except Exception:
        result = "Oops"
        
    return f'''
    <form method="post">
        <div>{result}</div>            
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

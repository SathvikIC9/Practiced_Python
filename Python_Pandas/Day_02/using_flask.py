from flask import Flask,request
import pandas as pd
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])

def dataframe():
    data = {
    "Name":['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
    "Age":[23,26,23,24,28],
    "Gender":["Male","Female","Male","Female","Male"],
    "Job Role": ["Junior Developer", "Senior Developer", "Project Manager", "UI/UX Designer", "DevOps Engineer"]
}
    df = pd.DataFrame(data)
    result = ""
    if request.method=="POST":
        try:
            value = request.form.get("value")
            if "datadrame" in value:
                result = df
            else:
                result = "Sorry not found."
        except Exception as e:
            result = "Oops!"
    return f'''
<form method="post">
        Enter your name: <input name="value" type="text">
        <input type="submit">
        <pre>{result}</pre>            
    </form>

'''
if __name__ == "__main__":
    app.run(debug=True)
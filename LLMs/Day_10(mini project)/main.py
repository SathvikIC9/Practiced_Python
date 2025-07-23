from flask import Flask,request,jsonify

app = Flask(__name__)
@app.route("/",methods= ["POST",'GET'])
def bot():
    reply = '' # using this to spearate the replies from the bot and the result if the calculations.
    result = ''
    if request.method == "POST":
        try:
            asked = [
    "What is your name?",
    "May I know your name?",
    "Can you tell me your name?",
    "What's your name?",
    "Who are you?",
    "Please tell me your name.",
    "How should I address you?"
]
            curious = ['why','Why','How','how']
            value = request.form.get('value')
            values = value.lower()
            split = values.split()
            my_set = [int(token) for token in split if token.isdigit()]
            if "add" in values:
                result = my_set[0]+my_set[1]
            elif "sub" in values:
                result = my_set[0]-my_set[1]
            elif "mul" in values:
                result = my_set[0]*my_set[1]
            elif "div" in values:
                result = my_set[0]//my_set[1]
            elif "percent" in values :
                result = ((my_set[0]//my_set[1])*100)
            else:
                result = "Sorry i m still learning 😅"
            if not result:
                result = "No calculation performed."
            if value in asked:
                reply = "Hi there! I am SmartBot 😎"
            elif curious in value:
                reply = "Seems like You are curious.😏"
            word_list = split
            my_dict = {}
            for word in word_list:
                my_dict[word] = my_dict.get(word, 0) + 1
  
            total = f"The totale words in your sentence are: {len(values)}"
            count = f" The total Unique words in your sentence are :{len(my_dict)}"
            longest = f" The Longest word in your message is : {max(my_dict,key=len)}"
            result += f"<br>{total}<br>{count}<br>{longest}"

        except Exception as e :
            return f"Sry we are working over it!..."
    return f'''
        <form method="post">
        <h3>Hi There 😊!</h3>
        Enter your message: <input name="value" type="text">
        <input type="submit" value="Send">
        <div><b>Bot:</b> {reply}</div>
        <div><b>Result:</b> {result}</div>
    </form>
'''
if __name__ == "__main__":
    app.run(debug=True)
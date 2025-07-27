from flask import Flask, request

app = Flask(__name__)

@app.route('/chat', methods=['GET', 'POST'])
def chatbot():
    result = ''
    if request.method == 'POST':
        try:
            user_input = request.form.get('message').lower()
            
            
            if "poem" in user_input:
                result = "Here's a short poem: Flask is fast, Flask is light, It makes your backend a delight!"
            elif "joke" in user_input:
                result = "Why did the developer go broke? Because he used up all his cache!"
            elif "what is" in user_input:
                topic = user_input.replace("what is", "").strip("?")
                result = f"I'm still learning about {topic.strip()}."
            elif user_input.strip() == "":
                result = "Take your time 😊."
            elif "clear" in user_input:
                with open('chatbot.txt', 'w') as f2:
                    f2.write("")
                result = "Chat history cleared! 🧹"

            else:
                result = "Hmm, I’m not sure what you mean yet."
            with open('chatbot.txt', 'a') as f:
                f.write(f"User: {user_input}\nBot: {result}\n")
        except Exception as e:
            result = "Oops! Something went wrong."
            with open('chatbot.txt', 'a') as f1:
                f1.write(f"Error: {str(e)}\n")

    return f'''
        <h3>Chat with SmartBot 🤖</h3>
        <form method="post">
            <input name="message" type="text" placeholder="Ask something..." style="width: 300px;">
            <input type="submit" value="Send">
        </form>
        <div style="margin-top: 20px;">
            <b>Bot:</b> {result}
        </div>
    '''
if __name__ =="__main__":
    app.run(debug=True)
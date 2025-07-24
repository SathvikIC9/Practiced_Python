from flask import Flask, request

app = Flask(__name__)


@app.route('/emotion_detect', methods=['POST','GET'])
def answer():
    result = ""
    happy_emotions = [
    "happy", "excited", "glad", "great", "good", "awesome", "amazing",
    "thankful", "loved", "chill", "cool", "pumped", "relaxed", "fine",
    "joyful", "peaceful", "content", "hopeful", "satisfied", "grateful","yayy","less goooo"
    ]
    spoken_sad_words = [
    "sad", "upset", "down", "bad", "angry", "hurt", "lonely", "tired",
    "frustrated", "annoyed", "depressed", "mad", "worried", "anxious",
    "miserable", "broken", "guilty", "sorry", "drained", "low","ugh"
    ]



    if request.method == 'POST':
        try:
            value = request.form.get('value')
            if any(word.lower() in value.lower() for word in happy_emotions):
                result = "Positive emotion 😊"
            elif any(words.lower() in value.lower() for words in spoken_sad_words):
                result = "Little sad emotion. 😅"
            else:
                result = "Sorry i wasnt that efficient.😥"
        except Exception:
            result = "Sorry couldnt help you."
    return f'''
    <form method="post">
        Enter your name: <input name="value" type="text">
        <input type="submit">          
        <div>{result}</div>            
    </form>
    '''


        


if __name__ == '__main__':
    app.run(debug=True)

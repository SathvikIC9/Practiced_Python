from flask import Flask, request, render_template_string, jsonify
import requests

app = Flask(__name__)

# Basic HTML form
HTML_FORM = '''
<!doctype html>
<title>Ollama Chat</title>
<h2>Ask something to Ollama</h2>
<form method=post>
  <input name=message type=text placeholder="Your message" required>
  <input type=submit value=Send>
</form>
{% if reply %}
<h3>Ollama's Reply:</h3>
<p>{{ reply }}</p>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def chat():
    reply = ""
    if request.method == 'POST':
        user_message = request.form['message']
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                "model": "llama3",  # Or use any model you have (e.g., "mistral", "gemma")
                "prompt": user_message,
                "stream": False
            }
        )
        if response.status_code == 200:
            data = response.json()
            reply = data.get("response", "[No reply received]")
        else:
            reply = f"[Error from Ollama: {response.status_code}]"
    return render_template_string(HTML_FORM, reply=reply)

if __name__ == '__main__':
    app.run(debug=True)

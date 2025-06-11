from flask import Flask, request, jsonify, render_template
import random
from t2cchatbot.utils import tokenize, stem_words
from t2cchatbot.chatbot import model, tag_responses  # Make sure these are imported correctly

app = Flask(__name__)

# Home route to render your front-end website
@app.route("/")
def index():
    return render_template("index.html")

# Chatbot API route
@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message", "")
        if not user_message:
            return jsonify({"response": "Please enter a message."}), 400

        tokens = tokenize(user_message)
        stems = " ".join(stem_words(tokens))
        tag = model.predict([stems])[0]

        response = random.choice(tag_responses.get(tag, ["I'm not sure how to help with that."]))
        return jsonify({"response": response})
    
    except Exception as e:
        return jsonify({"response": "An error occurred.", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

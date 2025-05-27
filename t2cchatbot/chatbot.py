import json
import joblib
import random
import os
import nltk
from nltk.stem import PorterStemmer

nltk.download('punkt')

# === Preprocessing ===
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence.lower())

def stem_words(words):
    return [stemmer.stem(w) for w in words]

# === Get the absolute path of the current file ===
BASE_DIR = os.path.dirname(__file__)

# === Load trained model ===
model_path = os.path.join(BASE_DIR, "data", "chat_model.pkl")
model = joblib.load(model_path)

# === Load intents and responses ===
intents_path = os.path.join(BASE_DIR, "data", "intents.json")
with open(intents_path) as file:
    data = json.load(file)

tag_responses = {
    intent["tag"]: intent["responses"] for intent in data["intents"]
}

# === Predict response based on user input ===
def get_bot_response(user_input):
    tokens = tokenize(user_input)
    stems = " ".join(stem_words(tokens))
    tag = model.predict([stems])[0]
    return random.choice(tag_responses.get(tag, ["Sorry, I didn't understand that."]))

# === (Optional) Command line chat for quick test ===
if __name__ == "__main__":
    print("Trash2Cash Bot: Hello! Type 'quit' to exit.")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            print("Trash2Cash Bot: Goodbye!")
            break
        response = get_bot_response(inp)
        print(f"Trash2Cash Bot: {response}")

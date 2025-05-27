import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


from flask import Flask, render_template, request, jsonify
from flask import Flask, render_template, request
from t2cchatbot.chatbot import get_bot_response
from flask import jsonify  # <- needed for returning JSON from /chat

app = Flask(__name__)

# Global RATES and LOCATIONS definitions
RATES = {
    "Plastic (PET bottles)": (80, 100),
    "Nylon (Pure water sachets)": (70, 200),
    "Aluminum (Cans)": (200, 500)
}

LOCATIONS = {
    "Lagos": ["Ikeja", "Surulere", "Yaba", "Lekki"],
    "Abuja": ["Garki", "Wuse", "Maitama", "Kubwa"]
}

def get_rate_range(material):
    """Return the rate range for a given material."""
    return RATES.get(material, (0, 0))

def calculate_reward(material, weight):
    """Calculate reward based on material and weight."""
    # Material names should match with the global RATES keys
    material_lower = material.lower()

    for key, (min_rate, max_rate) in RATES.items():
        if material_lower in key.lower():
            reward = (min_rate + max_rate) / 2 * float(weight)
            return reward
    return 0

def get_locations(state):
    """Return the list of locations for a given state."""
    return LOCATIONS.get(state, [])

@app.route("/", methods=["GET", "POST"])
def web_interface():
    reward = None
    material = None
    weight = None
    location = None

    if request.method == "POST":
        material = request.form.get("material")
        weight = request.form.get("weight")
        location = request.form.get("location")

        # Calculate the reward based on material and weight
        if material and weight and location:
            reward = calculate_reward(material, weight)
        else:
            reward = None

    return render_template("index.html", reward=reward, material=material, weight=weight, location=location, locations=LOCATIONS, rates=RATES)

@app.route("/process", methods=["GET", "POST"])
def process():
    reward = None
    material = None
    weight = None
    location = None

    if request.method == "POST":
        material = request.form.get("material")
        weight = request.form.get("weight")
        location = request.form.get("location")

        # Calculate the reward based on material and weight
        if material and weight and location:
            reward = calculate_reward(material, weight)
        else:
            reward = None

    return render_template("process.html", reward=reward, material=material, weight=weight, location=location)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    response = get_bot_response(message)  # your model's response logic
    return jsonify({"response": response})


def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Flask, render_template, request, jsonify
from t2cchatbot.chatbot import get_bot_response

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
    material_lower = material.lower()
    for key, (min_rate, max_rate) in RATES.items():
        if material_lower in key.lower():
            reward = (min_rate + max_rate) / 2 * float(weight)
            return reward
    return 0

def get_locations(state):
    """Return the list of locations for a given state."""
    return LOCATIONS.get(state, [])

# ✅ Renamed this function from web_interface to home
@app.route("/", methods=["GET", "POST"])
def home():
    reward = None
    material = None
    weight = None
    location = None

    if request.method == "POST":
        material = request.form.get("material")
        weight = request.form.get("weight")
        location = request.form.get("location")
        if material and weight and location:
            reward = calculate_reward(material, weight)

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
        if material and weight and location:
            reward = calculate_reward(material, weight)

    return render_template("process.html", reward=reward, material=material, weight=weight, location=location)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    response = get_bot_response(message)
    return jsonify({"response": response})

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        
        # For now, just log or print (or email/store later)
        print("Contact form submitted:", name, email, message)
        
        # Flash message to confirm (requires session key setup if used)
        flash("Message sent successfully!")
        return redirect("/contact")

    return render_template("contact.html")


def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()

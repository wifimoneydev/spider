# 🤖 T2CChatbot: The Smart Recycling Assistant for Trash2Cash

T2CChatbot is a conversational AI assistant built as a core interface for **Trash2Cash (T2C)** — a recycling platform that allows users to exchange trash (plastics, nylons, aluminum cans) for cash. This chatbot helps guide users through the recycling journey, from understanding accepted materials to calculating potential earnings and finding the nearest drop-off center.

---

## 🧩 Project Purpose

Millions of people in cities like Lagos and Abuja generate recyclable waste but lack knowledge or incentives to properly sort and dispose of it. Trash2Cash solves this by paying users for sorted waste. But even with cash incentives, many still find the process confusing or tedious.

**T2CChatbot solves this user experience gap** by making it easy to:
- Understand what Trash2Cash does
- Ask questions about recyclable materials
- Estimate how much users will earn from collected trash
- Get directions to the nearest T2C outlet
- Learn how to sign up or track previous exchanges

The chatbot acts like a smart, friendly guide—available 24/7 to educate and assist users.

---

## 🛠 Features and Capabilities

| Feature | Description |
|--------|-------------|
| 🔍 Trash Inquiry | Users can ask about what kind of materials are accepted, how to sort trash, and which trash types are most valuable. |
| 💰 Reward Estimator | Given a material type and weight, the bot calculates an estimated cash reward using real-time rates. |
| 📍 Location Finder | The bot helps users find their nearest Trash2Cash drop-off center based on local government area (LGA) or city. |
| 🤝 Onboarding Guide | Explains how to get started with Trash2Cash—whether on the web, app, or physical outlet. |
| 🧠 Smart Memory | Optionally remembers users' last conversation, location, or typical questions for more personalized responses. |
| 📦 Collection Scheduling (Coming soon) | Will allow users to schedule pickups or drop-off appointments. |

---

## 🧠 How the Chatbot Works

### 1. Intent Detection
T2CChatbot uses a combination of:
- Predefined intents (e.g., "reward calculation", "nearest outlet", "materials accepted")
- NLP libraries like **spaCy** or **transformers** to extract user intent from text
- Fine-tuned prompts for **GPT-3.5 or GPT-4** via OpenAI API for generating smart replies

### 2. Dynamic Data Retrieval
For real-time tasks like:
- Calculating trash reward
- Fetching drop-off locations
The bot connects to mock APIs or backend logic from the Trash2Cash database.

### 3. Response Generation
Replies are generated using:
- Static responses for simple FAQs
- Dynamic logic for calculated answers
- GPT API for natural language generation when context or personalization is needed

---

## 🧱 Architecture

User (Web / Mobile / WhatsApp)
│
▼
+------------------+
| T2CChatbot UI | ← Optional chat frontend (React, HTML/JS)
+------------------+
│
▼
+------------------+
| Chatbot Engine | ← NLP + Logic (Python)
+------------------+
│
▼
+------------------+
| T2C Backend API | ← Rates, Locations, User Data
+------------------+



## ⚙️ Installation & Running Locally

### Requirements:
- Python 3.9+
- `pip install -r requirements.txt`

### Steps:

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/T2CChatbot.git
cd T2CChatbot
Install dependencies

pip install -r requirements.txt
Set your API Key (Optional for GPT)


export OPENAI_API_KEY=your_key_here
Run chatbot script


python chatbot.py
Or if using Flask:


python app.py
📦 Project Files Explained
File	Purpose
chatbot.py	Core chatbot logic: input handling, intent detection, response generation
intents.json	List of known user intents and training examples
responses.py	Dictionary or logic that maps intents to responses
train_model.py	Optional script for training intent classifier (NLTK or ML-based)
app.py	Flask app for web-based chatbot
templates/	HTML files for rendering chatbot in browser
data/corpus.json	FAQ-style knowledge base
.env	(Optional) Store your API keys securely
requirements.txt	All Python packages used

🧪 Sample Conversations
User: How much will I get for 2.5kg of nylon?
Bot: At ₦150/kg, you’ll earn about ₦375 for 2.5kg of nylon.

User: What kind of plastic is accepted?
Bot: We accept PET plastic bottles (e.g., water bottles), PP containers, and HDPE jugs. Avoid PVC or dirty plastics.

User: Where can I drop off my trash in Ikeja?
Bot: The nearest drop-off is at “T2C Outlet – Ikeja LGA, Awolowo Way”, open 9AM–6PM daily.

🧭 Project Goals
Educate the public on recyclable waste and its value.

Automate user interaction to reduce burden on human agents.

Improve recycling rates in Nigeria starting with Lagos and Abuja.

Make Trash2Cash accessible to even low-literacy users via natural conversation.

🚀 Future Plans
 Multilingual support (Pidgin, Yoruba, Hausa)

 Voice integration

 WhatsApp bot version

 Scheduled trash pickup request

 Integration with user accounts (to track past exchanges)

👤 About the Creator
Daniel aka @wifimoneydev
Founder of Trash2Cash – Nigeria’s automated public recycling and reward platform.
Focused on building systems that reward sustainability, powered by AI and automation.

📝 License
This project is licensed under the MIT License. Feel free to fork and build your own version to promote sustainability anywhere in the world.


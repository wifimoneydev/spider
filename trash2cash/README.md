# Trash2Cash (T2C) ♻️💰

**Trash2Cash (T2C)** is a digital recycling platform aimed at encouraging individuals in developing countries to earn money by properly disposing of recyclable materials. This MVP (Minimum Viable Product) was built as part of my CS50P final project and focuses on Lagos and Abuja, Nigeria.


## 🚀 Project Overview

Trash2Cash allows users to:
- Select the type of recyclable material (Plastic, Nylon, Aluminum)
- Input the weight (in kilograms)
- Choose their Local Government Area (LGA) within Lagos or Abuja
- Instantly calculate their estimated cash reward
- See the nearest drop-off location based on their LGA

The long-term vision is to evolve this into an AI-powered, fully automated trash exchange system with container outlets across Nigeria and beyond.


## 📁 Directory Structure

Trash2Cash/
│
├── index.html # Main homepage
├── about.html # About the Trash2Cash project
├── contact.html # Contact form
├── style.css # Custom styles
├── script.js # JavaScript logic for dynamic calculations
├── assets/ # Images, icons, logos
│ └── logo.png
├── README.md # You're here!
└── ...

yaml
Copy
Edit


## 🌍 Target Audience

The MVP is designed for users in Nigeria, specifically Lagos and Abuja, who wish to:
- Earn cash from recyclable trash
- Contribute to sustainable living
- Find nearest drop-off stations for recycling



## 🛠️ Technologies Used

- **HTML5**: For structuring content
- **CSS3**: For styling and layout (responsive design)
- **JavaScript**: For calculations, dynamic DOM updates
- **VS Code**: Primary code editor
- **CS50P Python environment** (for logic prototyping)
- **Git** & **GitHub**: Version control


## 🎯 Core Features

### 1. Material Selection
```html
<select id="material">
  <option value="plastic">Plastic (₦80–₦100/kg)</option>
  <option value="nylon">Nylon (₦70–₦200/kg)</option>
  <option value="aluminum">Aluminum (₦200–₦500/kg)</option>
</select>
User can choose from 3 recyclable materials.

Each material has a dynamic pricing range based on market rates.

2. Weight Input
html
Copy
Edit
<input type="number" id="weight" placeholder="Enter weight in kg">
Accepts weight in kilograms``

JavaScript ensures only valid numeric input is accepted.

3. Location/LGA Selection
html
Copy
Edit
<select id="location">
  <option value="ikeja">Ikeja</option>
  <option value="lekki">Lekki</option>
  <option value="wuse">Wuse</option>
  ...
</select>
The user selects their Local Government Area.

The location is used to determine the nearest drop-off point (static for MVP, dynamic in future).

4. Reward Calculation (in script.js)
javascript
Copy
Edit
function calculateReward(material, weight) {
  const rates = {
    plastic: [80, 100],
    nylon: [70, 200],
    aluminum: [200, 500]
  };

  const [minRate, maxRate] = rates[material];
  const avgRate = (minRate + maxRate) / 2;
  return avgRate * weight;
}
Dynamically calculates estimated cash reward

Displayed on the screen using DOM manipulation

5. Responsive Design (in style.css)
css
Copy
Edit
@media screen and (max-width: 768px) {
  .navbar {
    flex-direction: column;
  }
  .container {
    padding: 10px;
  }
}
Fully responsive navigation bar and content

Mobile-first design ensures usability on low-end devices

6. Fixed Navigation Bar
css
Copy
Edit
.navbar {
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1000;
}
Keeps the navbar visible while scrolling

Enhances user experience and branding

📖 Pages Explained
📌 index.html
Main landing page

Contains the reward calculator form

Displays drop-off info and contact prompt

📌 about.html
Explains the mission and future vision of Trash2Cash

Details the impact of plastic waste and how recycling can help

Shares info about automation and future AI plans

📌 contact.html
Basic contact form (name, email, message)

Validates inputs using JavaScript (planned for later)

Sends queries to a mock or dummy backend for now

🧠 How I Built It
Step 1: Prototyping in Python (CS50P)
Wrote the logic for reward calculation using dictionaries and functions

Used input() and float() to simulate user interaction

Verified formula correctness before porting to JavaScript

Step 2: HTML Structure
Used semantic HTML elements like <header>, <section>, <footer>

Created reusable components (e.g., navbar, buttons)

Step 3: Styling with CSS
Chose a dark theme to stand out visually

Defined classes like .container, .section, .btn for reuse

Made navbar fixed and adjusted padding to avoid overlap

Step 4: Interactivity with JavaScript
Added event listeners to the form submit button

Validated weight and material inputs

Used functions to compute and display result dynamically

Step 5: Testing
Manually tested with different weights and materials

Ensured accuracy of reward calculations

Confirmed layout on desktop and mobile

🚧 Known Issues
No backend integration yet (reward not stored or tracked)

Drop-off locations are static text, not generated from database

No authentication or user wallet feature

AI-powered trash sorter is still in planning phase

📈 Future Plans
Integrate a backend (Flask or Django) to store user submissions

Connect to a geolocation API to dynamically suggest nearest drop-off

Add wallet system and reward history

Build the AI-powered trash classification system with cameras and Raspberry Pi

Partner with recycling plants to handle collected waste

Expand to other states and countries

🤝 Acknowledgments
CS50P by Harvard for teaching foundational programming

OpenAI for guidance and project ideation

My community in Nigeria for inspiring this mission to clean and empower

Friends and family who reviewed my code and UI

📬 Contact

📧 Email: trash2cash.ng@gmail.com

📍 Based in: Lagos, Nigeria

🔐 License
This project is open-source and free to use for educational or social good purposes. Contact me for commercial use or collaborations.

Let's turn trash into treasure. Together. 💚


# PROJECT TITLE:  Trash2Cash (T2C)

#### VIDEO DEMO URL:  https://youtu.be/5TD3n5k77fg>

#### DESCRIPTION:

**Trash2Cash (T2C)** is a web-based recycling incentive platform developed to encourage responsible waste disposal in Nigeria through monetary rewards. Built as the final project for Harvard's CS50P course, this application allows users to exchange recyclable trash for cash in a streamlined, tech-enabled process.

At its core, T2C helps users input the type of recyclable materials they’ve collected (e.g., plastic bottles, aluminum cans, or nylon sachets), enter the weight of their collection, and receive an instant estimated cash reward. Additionally, users can find the nearest drop-off center based on their local government area (LGA) within major cities such as **Lagos** and **Abuja**.

---

### 🌍 The Problem

Nigeria, like many developing nations, faces a serious environmental crisis due to improper waste disposal. Streets are littered with plastic bottles, nylon sachets, and aluminum cans. These materials clog drainage systems, pollute natural ecosystems, and contribute to flooding and disease outbreaks during the rainy season.

Despite the growing awareness about recycling, there remains a gap between intention and action — mostly due to a lack of structured infrastructure, poor awareness, and a missing economic incentive. People, especially in low-income areas, do not see the tangible benefits of recycling. Trash2Cash aims to change that narrative.

---

### 💡 The Solution

Trash2Cash is designed to:
- Educate users on the value of recycling.
- Motivate waste collection by offering **instant cash estimates** based on real-time market prices.
- Show users **where to take their recyclables** for actual cash rewards.
- Scale a **community-driven recycling culture** through technology.

The interface is clean, mobile-friendly, and designed with modern aesthetics using a black, white, gray, and green color palette — symbolizing clarity, neutrality, and eco-consciousness. The homepage introduces the user to the concept of recycling and emphasizes its importance in building a healthier, more sustainable Nigeria.

---

### 🔧 How It Works

1. **User inputs trash material type** (Plastic, Nylon, Aluminum).
2. **User enters weight** of collected material.
3. **User selects location** based on LGA.
4. The app instantly calculates and displays an **estimated cash reward**.
5. Nearest **drop-off centers** are recommended based on the location.

The app is powered by Python and Flask, with HTML/CSS for the frontend. The material rates are hardcoded into the application using a dictionary and may vary between a minimum and maximum range (e.g., aluminum cans: ₦200–₦500/kg). The reward is calculated using the average of these values multiplied by the weight entered by the user.

---

### 📈 Vision for the Future

Trash2Cash is more than a school project — it’s a **vision for the future of Nigeria**.

#### Short-Term Goals:
- Launch pilot programs in Lagos and Abuja.
- Partner with local government waste departments and private recycling companies to create verified drop-off points.
- Build mobile app versions for Android and iOS to improve accessibility.
- Add more materials and dynamic pricing that reflects real-time market conditions.

#### Long-Term Impact:
- **Empower local communities** to take ownership of their environment.
- **Create jobs** through collection, sorting, and processing of recyclable waste.
- Reduce the volume of non-biodegradable waste on streets, in gutters, and landfills.
- Inspire a **new generation of eco-conscious Nigerians**, especially youths and students, to see waste as an economic opportunity.
- Promote the **circular economy**, where trash is not the end, but the beginning of new products, materials, and value chains.
- Integrate a **digital wallet** so users can store rewards or convert them into mobile airtime, food vouchers, or bank transfers.

---

### 🇳🇬 Why Nigeria?

Nigeria has a population of over 220 million people, with thousands of metric tons of waste generated daily. Yet, less than 10% of it is properly recycled. While some urban initiatives exist, they are fragmented, underfunded, or limited to elite neighborhoods.

Trash2Cash targets the **everyday Nigerian**, especially in low and middle-income areas, offering a **real financial incentive** to participate in recycling. By making recycling feel rewarding — both socially and economically — T2C can shift mindsets across the country.

---

### 🛠 Technical Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML5, CSS3
- **Templating:** Jinja2
- **UI Theme:** Dark-themed with green eco-friendly accents
- **Folder Structure:**
  - `/templates`: Contains all HTML files (`index.html`, `about.html`, `contact.html`)
  - `/static`: Contains `styles.css`
  - `project.py`: Main Flask application
  - `README.md`: Project documentation

---

### 🚀 Future Features (Post-CS50)

- User authentication (register/login).
- Map integration (e.g., Google Maps API) to find and display drop-off centers visually.
- Admin dashboard for partners to track waste collection data and trends.
- A reward leaderboard to gamify recycling efforts in different neighborhoods.
- SMS notifications and reminders for drop-off schedules.
- Support for vernacular/local languages (e.g., Yoruba, Igbo, Hausa).

---

Trash2Cash combines **education**, **technology**, and **community impact** into one platform. It proves that even something as "dirty" as trash can become the cornerstone of a cleaner, richer, and more responsible society — starting with Nigeria, and expanding to other developing countries with similar waste challenges.

---

Made with love, code, and a vision for a better planet. 🌱

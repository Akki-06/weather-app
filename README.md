# 🌦️ Weather App

A clean and modern **Django-based Weather Application** that allows users to search real-time weather information for any city using the **OpenWeather API**.  
The project focuses on clarity, simplicity, and a polished user experience.

---

## 🚀 Features

- 🌍 Search weather by city name  
- 🌡️ Displays temperature in Celsius  
- 🌤️ Weather condition with custom icons  
- 💧 Humidity & 🌬️ wind speed details  
- ❌ Graceful handling of invalid city names  
- 🧭 Clean UI states (initial, success, error)  
- 🎨 Modern responsive design  
- ❤️ Footer branding for authenticity  

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS  
- **API:** OpenWeather API  
- **HTTP Client:** requests  
- **Database:** SQLite (default Django DB)  

---

## 📂 Project Structure

weather-app/
├── weather/
│   ├── static/
│   │   ├── css/
│   │   └── icons/
│   ├── templates/
│   │   └── index.html
│   ├── views.py
│   └── urls.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/weather-app.git
cd weather-app


### 2️⃣ Create & Activate Virtual Environment

python -m venv venv
source venv/bin/activate # macOS / Linux
venv\Scripts\activate # Windows


### 3️⃣ Install Dependencies

pip install -r requirements.txt

---

## 🔑 Add OpenWeather API Key

Add your API key in `settings.py`:

WEATHER_API_KEY = "your_api_key_here"

Get your API key from:  
https://openweathermap.org/api

---

## 🗄️ Run Database Migrations


---

## 📸 UI States

- **Initial State:** Prompt to search for a city  
- **Success State:** Weather data displayed with icons  
- **Error State:** “City not found” message with custom image  

---

## 🧠 Python Standard Libraries Used

These are included automatically with Python and require no installation:

- datetime  
- os  
- json  

---

## 📌 Future Improvements

- 🌙 Day / Night icon switching  
- ⏳ Loading animation  
- 📱 Improved mobile responsiveness  
- 🌐 AJAX-based search (no page reload)  

---

## 👤 Author

**Akhil (Akki)**  
Made with ❤️ by Akki © 2026  

---

## 📄 License

This project is open-source and free to use for learning and personal projects.


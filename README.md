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
## 📱Screenshot

<img width="400"  alt="Screenshot 2026-01-03 184040" src="https://github.com/user-attachments/assets/2df26d47-3b62-47d5-b2fa-a2e8f384290e" />

<img width="400" alt="Screenshot 2026-01-03 184104" src="https://github.com/user-attachments/assets/7e14cd09-dd42-41f6-8fe3-bf9b75064065" />

<img width="400" alt="Screenshot 2026-01-03 184020" src="https://github.com/user-attachments/assets/604fa78b-c63f-401a-86ad-750742272004" />

---
## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/weather-app.git
cd weather-app


### 2️⃣ Create & Activate Virtual Environment

- python -m venv venv
- source venv/bin/activate # macOS / Linux
- venv\Scripts\activate # Windows


### 3️⃣ Install Dependencies

pip install -r requirements.txt

---

## 🔑 Add OpenWeather API Key

Add your API key in `settings.py`:

WEATHER_API_KEY = "your_api_key_here"

Get your API key from:  
https://openweathermap.org/api

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


# 🎬 Movie Recommender API (Backend + AI)

This repository contains the **backend API** for the Movie Recommender project, powered by **Python FastAPI** and a simple AI-based recommendation logic. The backend serves a desktop client built with **C# WPF** to provide personalized movie recommendations.

---

## 🚀 Features

- **AI-based recommendation:** Suggests movies based on the user’s input (favorite movies).
- **FastAPI backend:** Provides REST endpoints to serve recommendations.
- **JSON-based movie database:** Loads movie data dynamically from `movies.json`.
- **CORS enabled:** Allows cross-origin requests from WPF desktop client or other frontends.
- **Scalable structure:** Easy to update the movie database via JSON or external APIs (TMDB).

---

## 📂 Project Structure

Backend/
├─ main.py # FastAPI backend code
├─ movies.json # Movie database
├─ requirements.txt # Python dependencies
└─ README.md # This file


---

## 🛠 Tech Stack

- **Backend:** Python, FastAPI
- **AI/Logic:** Simple keyword matching + recommendation selection
- **Data:** JSON movie database (can be updated with TMDB API)
- **CORS:** Enabled for cross-origin requests
- **Frontend client:** C# WPF desktop app (separate repo)

---

## ⚡ API Endpoints

### **POST /recommend**
Get movie recommendations based on user input.

**Request Body:**
```json
{
  "favorite_movies": "Inception"
}

Response:

{
  "user_movie": "Inception",
  "recommendations": [
    {
      "title": "Interstellar",
      "overview": "...",
      "rating": "8.6",
      "date": "2014-11-07"
    },
    {
      "title": "The Matrix",
      "overview": "...",
      "rating": "8.7",
      "date": "1999-03-31"
    }
  ]
}

GET /

Welcome message for API testing:

{
  "message": "Welcome to the Movie Recommendation API 🎬"
}

📝 How to Run
1. Create a Python environment

python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows

2. Install dependencies

pip install -r requirements.txt

3. Run the API

uvicorn main:app --reload

The API will be available at: http://127.0.0.1:8000
🎯 Update Movie Database

The movie database is in movies.json. You can update it manually or fetch new movies using the TMDB API script provided (Python).
🌟 Notes

    The AI recommendation is based on matching the user’s input with movie titles in the JSON database.

    The API is designed to work with the WPF Desktop client for a complete user experience.

    Future improvements: integrate real AI/ML model for smarter recommendations.

📸 Screenshots (Desktop App)


💻 Author

Abdelmalek Zouaoui – AI & Full-Stack Developer

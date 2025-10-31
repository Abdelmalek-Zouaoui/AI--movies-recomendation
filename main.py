from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json

# ---------------- FastAPI app ----------------
app = FastAPI()

# Enable CORS so your WPF app can call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For testing, allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- Request model ----------------
class MovieRequest(BaseModel):
    favorite_movies: str  # Must match JSON key from WPF app

# ---------------- Load movie database ----------------
with open("data/movies.json", "r", encoding="utf-8") as f:
    movie_db = json.load(f)

# ---------------- Helper function ----------------
# Build a dictionary mapping lowercase title -> movie data
movie_dict = {m["title"].lower(): m for m in movie_db}

def get_recommendations(user_input: str, top_n=5):
    user_input_lower = user_input.lower()
    matched_movie = None

    # Step 1: Find the movie mentioned
    for title_lower, movie in movie_dict.items():
        if title_lower in user_input_lower:
            matched_movie = movie
            break

    if not matched_movie:
        return []

    # Step 2: Recommend top_n other movies
    recommendations = []
    for movie in movie_db:
        if movie["title"] != matched_movie["title"]:
            recommendations.append({
                "title": movie["title"],
                "overview": movie.get("overview", "No overview available"),
                "rating": movie.get("rating", 0),
                "release_date": movie.get("release_date", "Unknown"),
                "poster": movie.get("poster")  # Add poster URL
            })
        if len(recommendations) >= top_n:
            break

    return recommendations


# ---------------- POST endpoint ----------------
@app.post("/recommend")
def recommend_movies(request: MovieRequest):
    recs = get_recommendations(request.favorite_movies, top_n=5)
    if not recs:
        return {"message": "Sorry, I don't have recommendations for that movie yet."}

    return {
        "user_movie": request.favorite_movies,
        "recommendations": recs
    }

# ---------------- Root endpoint ----------------
@app.get("/")
def home():
    return {"message": "Welcome to the Movie Recommendation API 🎬"}

import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the movie data with embeddings
with open("data/movies_embeddings.json", "r", encoding="utf-8") as f:
    movies = json.load(f)

# Load the same embedding model used in preprocess.py
model = SentenceTransformer("all-MiniLM-L6-v2")

# Extract embeddings into a NumPy array for fast computation
movie_embeddings = np.array([m["embedding"] for m in movies])

def recommend_movies(user_input, top_n=5):
    """
    Find top N similar movies based on user input.
    """
    # Step 1: Encode the user message
    user_embedding = model.encode(user_input).reshape(1, -1)

    # Step 2: Compare with all movie embeddings using cosine similarity
    similarities = cosine_similarity(user_embedding, movie_embeddings)[0]

    # Step 3: Sort movies by similarity (highest first)
    indices = similarities.argsort()[::-1][:top_n]

    # Step 4: Build recommendation list
    recommendations = []
    for idx in indices:
        m = movies[idx]
        recommendations.append({
            "title": m["title"],
            "overview": m["overview"],
            "rating": m["rating"],
            "release_date": m["release_date"],
            "similarity": round(float(similarities[idx]), 3)
        })
    
    return recommendations

# For direct testing from terminal
if __name__ == "__main__":
    user_text = input("🎬 Write a movie you like: ")
    recs = recommend_movies(user_text)
    print("\n🔥 Recommended movies:\n")
    for i, r in enumerate(recs, 1):
        print(f"{i}. {r['title']} ({r['release_date']}) — ⭐ {r['rating']}")
        print(f"   {r['overview'][:180]}...\n")

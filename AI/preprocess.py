import json
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

# Load the dataset
with open("data/movies.json", "r", encoding="utf-8") as f:
    movies = json.load(f)

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

processed = []

print("Generating embeddings for movie overviews...")

for movie in tqdm(movies):
    text = f"{movie['title']} - {movie['overview']}"
    embedding = model.encode(text).tolist()
    processed.append({
        "id": movie["id"],
        "title": movie["title"],
        "overview": movie["overview"],
        "rating": movie.get("rating"),           # ✅ Corrected here
        "release_date": movie.get("release_date"),
        "embedding": embedding
    })

# Save to new file
with open("data/movies_embeddings.json", "w", encoding="utf-8") as f:
    json.dump(processed, f, indent=2)

print(f"✅ Processed {len(processed)} movies and saved embeddings.")

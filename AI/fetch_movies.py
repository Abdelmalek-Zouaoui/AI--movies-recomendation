import requests, json, os

API_KEY = "41b558c84a2220c88a0144bce355871f"
URL = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page="

def fetch_movies(pages=5):
    movies = []

    for page in range(1, pages + 1):
        response = requests.get(URL + str(page))
        data = response.json()
        os.makedirs("data", exist_ok=True)  # make sure 'data' folder exists

        # Check that the API response has 'results'
        if 'results' not in data:
            print(f"⚠️ No results found on page {page}")
            continue

        for m in data['results']:
            movies.append({
                "title": m.get('title', 'Unknown'),
                "overview": m.get('overview', 'No overview available'),
                "id": m.get('id'),
                "rating": m.get('vote_average', 0),
                "release_date": m.get('release_date', 'Unknown'),
                "poster": f"https://image.tmdb.org/t/p/w500{m['poster_path']}" if m.get('poster_path') else None
            })

        print(f"✅ Page {page} fetched successfully.")

    # Save all movies to JSON
    with open("data/movies.json", "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=2, ensure_ascii=False)

    print(f"\n🎬 Saved {len(movies)} movies to data/movies.json")

if __name__ == "__main__":
    fetch_movies()

def get_movies_by_category(movie_list, category):
    movies_in_category = [movie for movie in movie_list if movie["category"] == category]
    return movies_in_category

if __name__ == "__main__":
    movies = [
        {
            "name": "Usual Suspects", 
            "imdb": 7.0,
            "category": "Thriller"
        },
        {
            "name": "Hitman",
            "imdb": 6.3,
            "category": "Action"
        },
        {
            "name": "Dark Knight",
            "imdb": 9.0,
            "category": "Adventure"
        },
    ]

    action_movies = get_movies_by_category(movies, "Action")
    print("Movies in the 'Action' category:")
    for movie in action_movies:
        print(f"Name: {movie['name']}, IMDB: {movie['imdb']}")

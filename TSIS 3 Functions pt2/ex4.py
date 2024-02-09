def compute_average_imdb_score(movie_list):
    total_score = sum(movie["imdb"] for movie in movie_list)
    num_movies = len(movie_list)
    if num_movies == 0:
        return 0  
    average_score = total_score / num_movies
    return average_score

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

    average_score = compute_average_imdb_score(movies)
    print(f"Average IMDB score of the movies: {average_score}")

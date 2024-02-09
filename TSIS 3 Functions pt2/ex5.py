def compute_average_imdb_score_by_category(movie_list, category):
    movies_in_category = [movie for movie in movie_list if movie["category"] == category]
    
  
    total_score = sum(movie["imdb"] for movie in movies_in_category)
    num_movies = len(movies_in_category)
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

    
    category = "Action"
    average_score = compute_average_imdb_score_by_category(movies, category)
    print(f"Average IMDB score of movies in the '{category}' category: {average_score}")

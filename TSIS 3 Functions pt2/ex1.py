def is_above_5_5(movie):
    return movie["imdb"] > 5.5

if __name__ == "__main__":
    movie = {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    }
    print(is_above_5_5(movie))  # Output: True

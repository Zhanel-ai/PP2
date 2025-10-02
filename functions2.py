#1
def is_high_imdb(movie: dict) -> bool:
    return movie.get('IMDB', 0) > 5.5
#print(is_high_imdb(movies[0]))  




#2
def filter_high_imdb(movies: list[dict]) -> list[dict]:
    return [m for m in movies if m.get('IMDB', 0) > 5.5]
#print(filter_high_imdb(movies))



#3
def by_category(movies: list[dict], category: str) -> list[dict]:
    cat = category.lower()
    return [m for m in movies if m.get('category', '').lower() == cat]
#print(by_category(movies, "Romance"))



#4
def average_imdb(movies: list[dict]) -> float:
    if not movies:
        return 0.0
    return sum(m.get('IMDB', 0) for m in movies) / len(movies)
#print(average_imdb(movies))



#5
def average_imdb_by_category(movies: list[dict], category: str) -> float:
    subset = by_category(movies, category)
    return average_imdb(subset)
#print(average_imdb_by_category(movies, "Comedy"))


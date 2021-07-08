"""

Stwórz klasę BazaFilmow w ramach, której korzystasz z danych zawartych w pliku movies.txt. Każdy pojedynczy film powinien być reprezentowany przez klasę Film.

    odpowiednio przetwórz dane z pliku, żeby otrzymać listę instancji klasy Film
    klasa BazaFilmow powinna zawierać metodę do sortowania filmów po nazwie
    klasa BazaFilmow powinna zawierać metodę do sortowania filmów po roku
    klasa BazaFilmow powinna zawierać metodę do obliczenia różnicy w latach między najstarszym, a najnowszym filmem
"""
import json 

class BazaFilmow:
    def __init__(self, list_of_movies):
        self.list_of_movies = list_of_movies

class Film: 
    def __init__(self, title, year, cast, genres):
        self.title = title
        self.year = year
        self.cast = cast
        self.genres = genres

def import_from_json():
    with open("/home/garr/Projects/codme_zadania/movies.json", encoding='utf-8') as f: 
        movies =json.load(f)
        return movies 

def create_classes(movies):
    movie_lst = []
    for movie in movies:
        movie_lst.append(Film(movie['title'], movie['year'], movie['cast'], movie['genres']))
    return movie_lst

def main():
    for movie in create_classes(import_from_json()):
        print(f"Movie: {movie.title}, Year: {movie.year}")

if __name__=='__main__':
    main()
        
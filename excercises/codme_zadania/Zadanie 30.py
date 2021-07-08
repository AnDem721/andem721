import json

def get_data():
    with open("movies.json", encoding="utf-8") as f:
        movie_data = json.load(f)
        horror_movies = []
        for movie in movie_data:
            if "Horror" in movie['genres']:
                horror_movies.append(movie)
        return horror_movies

def write_to_file(horrors):
    with open('horror_movies.json', 'w', encoding='utf-8') as f:
        json.dump(horrors, f)
#jeszcze wiecej zahashowanego tekstu
def main():
    horrors = get_data()
    write_to_file(horrors)

main()
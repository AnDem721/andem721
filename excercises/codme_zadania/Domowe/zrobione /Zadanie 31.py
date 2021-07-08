import json
import os

def get_data():
    with open("songs.json", encoding="utf-8") as f:
        processed_file = json.load(f)
        return processed_file

def create_dirs(songs):
    os.makedirs("Piosenki", exist_ok=True)
    artists = []
    path_to_folder = 'c:/Users/Fabryka/PycharmProjects/pythonProject/Piosenki'
    for song in songs:
        if song['artist'] in artists:
            pass
        else:
            artists.append(song['artist'].replace("/", "").replace(" ", "_").replace("'", ""))
    for artist in artists:
        os.makedirs(os.path.join(path_to_folder,artist), exist_ok=True)

def song_files(songs):
    path_to_folder = 'c:/Users/Fabryka/PycharmProjects/pythonProject/Piosenki'
    for song in songs:
        work_folder = path_to_folder + "/" + song["artist"].replace("*", "x").replace("/", "").replace(" ", "_").replace("'", "")
        file_name = song["title"].replace("*", "x").replace("/", "").replace(" ", "_").replace("'", "") + ".txt"
        with open(os.path.join(work_folder, file_name), "w", encoding="utf-8") as f:
            f.write(song["lyrics"])





def main():
    songs = get_data()
    create_dirs(songs)
    song_files(songs)
main()
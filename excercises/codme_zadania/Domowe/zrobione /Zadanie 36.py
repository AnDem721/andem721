import json

class Song:
    def __init__(self, artist, title, lyrics):
        self.artist = artist
        self.title = title
        self.lyrics = lyrics

def import_from_json():
    with open("songs.json", encoding="utf-8") as f:
        songs = json.load(f)
        return songs

def apply_to_class(songs):
    songs_lst = []
    for song in songs:
        songs_lst.append((Song(song['artist'], song['title'], song['lyrics'])))
    print(songs_lst)
    return songs_lst

def main():
    for song in apply_to_class(import_from_json()):
        print(f"Artist: {song.artist}, Title: {song.title}")


if __name__ == '__main__':
    main()

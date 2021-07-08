import json

def get_artists():
    with open("songs.json", encoding="utf-8") as f:
        songs_data = json.load(f)
        artist_only = [key['artist'] for key in songs_data]
        return artist_only

def most_common_artis(artists):
    artists_dict = {}
    for artist in artists:
        if artist in artists_dict:
            artists_dict[artist] += 1
        else:
            artists_dict[artist] = 1
    print(f"najczęściej pojawiającym sie artystą jest: ", max(artists_dict, key=artists_dict.get))

artists = get_artists()
most_common_artis(artists)
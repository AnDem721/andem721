music_formats = ["mp3", "wav", "flac", "aac", "ogg", "wma"]
def get_files():  #przyjecie od uzytkownika naz plikow
    file_list=[]
    while True:
        fl_name = input("Podaj nazwę pliku (lub \"x\" by zakończyć) : ")
        if fl_name != "x":
            file_list.append(fl_name)
        else:
            break
    return file_list

def filter_files(files): #przefiltrowanie plikow
    usr_music_files = []
    for file in files:
        single = file.split(".")
        if single[1] in music_formats:
            usr_music_files.append(file)
    return usr_music_files


def main():
    files = get_files()
    music_files = filter_files(files)
    print(f"Twoje pliki dzwiękowe to: {music_files}")



main()
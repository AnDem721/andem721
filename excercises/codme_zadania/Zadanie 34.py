
while True:
    filename = input("podaj plik do otworzenia: ")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            file_content = f.readlines()
            print(file_content)
            break
    except:
        print("nie ma takiego pliku")


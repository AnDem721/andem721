title = input("Podaj tytuł swojej ulubionej piosenki ->")
znaki = len(title)
print(f"Tytuł twojej piosenki składa się z {znaki} znaków")
print("w tym tytule a występuje", title.count("a"), "razy")
title = title.strip(' ')
spacja = title.find(" ")
if spacja > 0:
    print("w tytule wystepuje spacja")
else:
    print('w tytule nie wystepije spacja')
title2 = list(title)
print('$'.join(title2))
print(title.replace(' ',''))







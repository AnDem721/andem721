dict = {
    "imie": "Andrzej",
    "nazwisko": "Kowalski",
    "adres": "Gdanska 1",
    "urodzony": "1983",
}

print(dict["imie"], dict["nazwisko"], "urodził sie w", dict["urodzony"], "i mieszka pod adresem", dict["adres"])
pseudo = input("Podaj pseudonim: ")
dict["nick"] = pseudo

print(dict)

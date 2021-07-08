uczniowe_na_roku = ["Mateusz", "Jan", "Ania", "Kasia", "Ola", "Jacek", "Rafał", "Karolina"]
uczniowe_na_wykladzie = ['Rafał', 'Jacek', 'Ola', 'Jan', 'Karolina', 'Kasia']

na_roku_set = set(uczniowe_na_roku)
na_wykladzie_set = set(uczniowe_na_wykladzie)


print(na_roku_set.difference(na_wykladzie_set))

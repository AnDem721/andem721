
punkty = {
    1 : ["a", "e", "i", "n", "o", "r", "s", "w", "z"],
    2 : ["c", "d", "k", "l", "j", "m", "p", "t", "y"],
    3 : ["b", "g", "h", "u"],
    5 : ["f"]
}

word = (input("podaj wybrane słowo: "))
punktacja = []

word = list(word.lower())
print(word)
for x in word:
    for key, letter in punkty.items():
        if x in letter:
            punktacja.append(key)
print(punktacja)
print(f" Twój wynik to {sum(punktacja)}")


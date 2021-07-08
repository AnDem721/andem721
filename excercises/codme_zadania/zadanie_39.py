"""Napisz klasę, która będzie zawierała trzy metody:


pobierz_napis - pobiera napis od użytkownika
wyswietl_napis - wyświetla wczesniej pobrany napis od uzytkownika
wyswietl_odwrocony_napis


Dla każdego stworzonego obiektu, metoda pobierz_napis może być wywołana tylko raz
"""

class Napis:
    def __init__(self):
        self.napis = ""
        self.napis_counter = 0

    def pobierz_napis(self):
        if self.napis_counter == 0:
            nap = input("Podaj dowolny napis: ")
            self.napis_counter += 1
            self.napis = nap
        else: 
            raise ValueError("Juz uzyles tej funkcji")

    def wyswietl_napis(self): 
        print(f"Twoj napis: {self.napis}")

    def odwroc_napis(self):
        print(self.napis[::-1])


if __name__ == '__main__':
    n1 = Napis() 
    n1.pobierz_napis()
    n1.wyswietl_napis()
    n1.odwroc_napis()
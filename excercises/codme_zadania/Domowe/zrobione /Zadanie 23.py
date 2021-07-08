# Napisz program który pobiera dane od użytkownika a następnie zlicza liczbę
# poszczególnych liter. Podziel go na odpowiednie funkcje których będzie można ponownie użyć
# (pobierz_dane(), policz_litery(), ...)
import re
def get_data():
    user_data = input("Wpisz lub wklej wybrany tekst: ")
    return user_data

def clean_data(user_data):
    analized_text = list(user_data.lower())
    for index, item in enumerate(analized_text):
        if item.isalpha():
            pass
        else:
            analized_text[index] = ""
    analized_text = list(filter(None, analized_text))
    print(analized_text)
    return analized_text

def sign_count(analized_text):
    sign_dict = {}
    for sign in analized_text:
        if sign in sign_dict:
            sign_dict[sign] += 1
        else:
            sign_dict[sign] = 1
    for key in sign_dict:
        print(key, ' : ', sign_dict[key])

def main():
    user_data = get_data()
    analized_text = clean_data(user_data)
    sign_count(analized_text)

main()

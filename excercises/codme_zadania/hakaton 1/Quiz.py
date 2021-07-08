import time
import random
pyt_dict = {
    1 : "Jaka jest stolica Portugali?",
    2 : "Jaki jest symbol chemiczny srebra?",
    3 : "Kim była „Sportowa osobowość roku” BBC w 2001 roku?",
    4 : "Gdyby Ziemia została przekształcona w czarną dziurę, jaka byłaby średnica jej horyzontu zdarzeń?",
    5 : "Gdybyś spadł w pozbawioną powietrza oraz tarcia dziurę przechodzącą przez środek Ziemi, ile czasu zajmie opadnięcie na drugą stronę? (Do najbliższej minuty.)",
    6 : "Jaka amerykańska grupa pop z lat 1960 stworzyła „surfin sound”?",
    7 : "Ile słoneczników było w trzeciej wersji obrazu Van Gogha „Słoneczniki”?",
    8 : "Który metal odkrył Hans Christian Oersted w 1825 roku?",
    9 : "Jaki zawód widniał na wizytówce Ala Capone",
    10 : "Ilu graczy jest w olimpijskiej drużynie do curlingu?"
}
odp_dict = {
    1 : ["Lizbona", "Porto", "Lagos", "Braga", "Lizbona"],
    2 : ["Ag", "Sr", "Au", "Hg", "Ag"],
    3 : ["David Beckham", "Michael Owen", "Paula Radcliffe", "Lewis Hamilton", "David Beckham"],
    4 : ["20mm", "20 000m", "1m", "10 000 000 0000 0000 m", "20mm"],
    5 : ["42 minuty", "13 minut", "137 minut", "342 minut", "42 minuty"],
    6 : ["Beach Boys", "The Monkees", "The Stooges", "The Grateful Dead", "Beach Boys"],
    7 : ["12", "3", "24", "1", "12"],
    8 : ["aluminium", "tytan", "wolfram", "platyna", "aluminium"],
    9 : ["Sprzedawca używanych mebli", "Fryzjer", "Dentysta", "Księgowy", "Sprzedawca używanych mebli"],
    10 : ["Cztery", "Jedenaście", "Trzy", "Sześć", "Cztery"]
}
current_dict = { "a":"", "b":"" , "c":"" , "d":"" }
score = 0
print("Zaczynamy!")
gra = random.sample(pyt_dict.keys(), k=5)
for runda in gra:
    time.sleep(1)
    print("\n" * 10)
    print(pyt_dict[runda])
    current_dict = dict(zip(current_dict, set(odp_dict[runda])))
    for x, y in current_dict.items():
        print(x, y)
    usr_odp = str(input("Twoja odpowiedz to => "))
    if usr_odp in current_dict.keys():
        if current_dict[usr_odp] == odp_dict[runda][4]:
            print("Brawo! To jest dobra odpowiedz")
            score = score + 1
            time.sleep(1)

        else:
            print("Niestety to jest zła odpowiedz")
            print(f"Prawidłowa odpowiedź to => {odp_dict[runda][4]}")
            time.sleep(1)
print("\n" * 10)
print(f"Uzyskany wynik to: {score} na 5 punktów")
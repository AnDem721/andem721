"""
Napisz program, który wylicza i informuje użytkownika o cenie jego wakacji:
wybierz 3 dostępne lokalizacje
dla każdej z tych lokalizacji ustal cenę za lot, cenę za wypożyczenie samochodu (dziennie) oraz cenę za nocleg (dziennie)
zapytaj użytkownika o liczbę nocy, lokalizację oraz liczbę dni, którą zamierza spędzić na miejscu
program powinien wypisać całkowitą sumę, którą użytkownik musi zapłacić wraz z poszczególnymi składowymi (np. lot kosztuje 500, samochód 400, nocleg 1500)
"""
import Zad25_get_user_input
# przechowywanie cennika

poland = {
    "flight": 500,
    "car_rental": 60,
    "accommodation": 200
}

iceland = {
    "flight": 700,
    "car_rental": 150,
    "accommodation": 300
}

uk = {
    "flight": 600,
    "car_rental": 500,
    "accommodation": 500
}


def calculate_cost(location, days, nights):
    # 2 * cena lotu + days * car_rental + nights * accommodation
    if location == "uk":
        chosen_country = uk
    elif location == "iceland":
        chosen_country = iceland
    elif location == "poland":
        chosen_country = poland

    flight_cost = chosen_country["flight"] * 2
    rental_cost = chosen_country["car_rental"] * days
    accommodation_cost = chosen_country["accommodation"] * nights

    total = flight_cost + accommodation_cost + rental_cost

    print(total)
    print(flight_cost, rental_cost, accommodation_cost)
    return total, flight_cost, rental_cost, accommodation_cost

def summarize_costs(costs):
    print(f"total => {costs[0]}")
    print(costs[1:])

def main():
    location, nights, days = Zad25_get_user_input.get_user_input()
    cost = calculate_cost(location, days, nights)
    summarize_costs(cost)

main()

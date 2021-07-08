def get_user_input():
    countries = ["uk", "iceland", "poland"]
    location = input("Where would you like to go? (uk, iceland, poland) -> ")
    # while location != "uk" and location != "iceland" and location != "poland":
    while location not in countries:
        location = input("Where would you like to go? (uk, iceland, poland) -> ")
    nights = int(input("How many nights? ->"))
    days = int(input("How many days? ->"))
    return location, nights, days
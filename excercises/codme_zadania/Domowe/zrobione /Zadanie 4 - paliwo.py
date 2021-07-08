gas_price = 4.44
avg_use = 9
print(f"Cena paliwa wynosi {gas_price}, średnie spalanie to {avg_use} l/km")

while True:
    usr_am = int(input("Jaka jest kwota, którą chcesz wydać na paliwo: "))
    usr_route = int(input("Jaki dystans chciałbyś przejechać: "))
    usr_need = usr_route / avg_use
    usr_cost = usr_am / gas_price
    if usr_cost < usr_need:
        print("niestety, musisz skrócić dystans lub wydać więcej")
    else:
        print("mozna jechac!")
        break

imie = input("Podaj imię bohatera:")
miasto = input("Podaj skąd wyjechał:")
miasto2 = input("podaj dokąd pojechał:")
transport = input("wymyśl środek transportu:")
opowiadanie = f"{imie} z {miasto} pojechał do {miasto2} {transport}"
print(opowiadanie)
opowiadanie2 = opowiadanie [::-1]
print(opowiadanie2)
op3 = opowiadanie.split()
op3 = op3 [::-1]
op3 = " ".join(op3)
print(op3)

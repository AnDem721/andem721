list = []
for x in range(1,11):
    list.append(float(input(f"Podaj {x} liczbę: ")))
print(list)
print(f"suma podanych liczb to {sum(list)}")
print(f"Średnia z podanych liczb to {sum(list) / len(list)}")


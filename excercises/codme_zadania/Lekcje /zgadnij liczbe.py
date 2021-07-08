import random
num = random.randint(1, 100)
print(num)
while True:
    num2 = int(input("zgadnij liczbe: "))
    if num2 > num:
            print("Podana liczba jest za duza")
    elif num2 < num:
            print("podana licznba jest za mała")
    else:
        print("cool")
        break
score = int(input("Podaj procentowy wynik testu: "))
if score in range(0,101):
    if score in range(0,29):
        print(f'{score}% daje ocenę: 1')
    elif score in range(30,51):
        print(f'{score}% daje ocenę: 2')
    elif score in range(51,75):
        print(f'{score}% daje ocenę: 3')
    elif score in range(75,91):
        print(f'{score}% daje ocenę: 4')
    else:
        print(f'{score}% daje ocenę: 5')
else:
    print("podałeś zły wynik testu")
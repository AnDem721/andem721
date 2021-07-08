list = []
while True:
    if len(list) > 3:
        list.append(input("podaj liczbe"))
    else:
        for x in list:
            print(x, end="")
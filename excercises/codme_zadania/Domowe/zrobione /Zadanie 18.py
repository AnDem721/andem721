def get_numbers():
    numList = input("Podaj dowolną ilośc liczb oddzielonych przecnkiem =>")
    numList = numList.split(',')
    return numList

def print_biggest(numList):
    numList = numList
    print(f' Największa z podanych liczb to: {max(numList)}')


print_biggest(get_numbers())

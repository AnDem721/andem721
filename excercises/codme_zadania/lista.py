""" ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE

1-n = [1,2,3,4,5,...,10]
np. n=10
wejście: [2,3,7,4,9], 10
wyjście: [1,5,6,8,10]"""


def list_check(list, n):
    missing_nums=[]
    for num in range(1,n+1):
        if num not in  list:
            missing_nums.append(num)
        
    return missing_nums

print(list_check([2,3,7,4,9], 10))
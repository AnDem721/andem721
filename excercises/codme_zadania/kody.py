""" ZADANIE 1. GENERATOR KODÓW POCZTOWYCH

przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi
"""
x = "79-900"
y = '80-155'
def generator(x, y):
    kody = []
    for num in range(int(x.split('-')[1])+1, 1000):
        kody.append(x.split('-')[0]+'-'+str(num))
    
    for num in range(int(y.split('-')[1])):
        kody.append(y.split('-')[0]+'-'+f"{num:03}")
    
    return kody
    
print(generator(x,y))

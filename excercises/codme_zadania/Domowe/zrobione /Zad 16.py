# Napisz funkcję, która przyjmie historię transakcji i na tej podstawie obliczy aktualne saldo konta.

#transakcje = [("D", 1000), ('W', 400), ('D', 200), ('D', 1500), ('W', 500)]

transakcje = []
def get_usr_input():
    transakcje = []
    while True:
        type = input("Podaj rodzaj operacji [d]eposit/[w]ithdraw/[e]xit")
        if type == "d" or type == "w":
            amnt = input("Podaj kwotę operacji: ")
            transakcje.append((type, int((amnt))))
        else:
            break
    return transakcje

transakcje = get_usr_input()

def saldo(transakcje):
    depo = []
    withd =[]
    for trans in transakcje:
        if trans[0] == "d":
            depo.append(trans[1])
        else:
            withd.append(trans[1])

    saldo = sum(depo) - sum(withd)
    print(f"Twoje saldo wynosi {saldo} pln.")

# def main():
#     get_usr_input()
#     transakcje = get_usr_input()
#     saldo(transakcje)



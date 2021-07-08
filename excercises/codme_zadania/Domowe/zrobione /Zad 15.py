# Napisz funkcję do generowania haseł o długości zadanej przez użytkownika.
#
# Hasło powinno się zmieniać wraz z każdym uruchomieniem programu.
#
# Pamiętaj, że dobre hasło powinno zawierać zarówno małe jak i duże litery,
# cyfry oraz znaki specjalne (np. #?%&).
import random

def new_passwd(strenght):
    sgn = "abcdefghijklmnoprstuwxyzABCDEFGHIJKLMNOPRSTUWXYZ1234567890!@#$%^&*()"
    avb_sgn = list(sgn)
    paswd_lst = []
    passwd = ""
    for x in range(strenght):
        paswd_lst += random.choice(avb_sgn)
    for let in paswd_lst:
        passwd += let
    print(passwd)
    return passwd

new_passwd(2)
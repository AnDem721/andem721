
import random

word_list = ["government", "history", "hundred ", "industry ", "jacket", "kitchen ", "knife" ]
ran_wrd = random.choice(word_list)
print(ran_wrd)
wrd_shf = "".join(random.sample(ran_wrd, len(ran_wrd)))
print(f"Wylosowane słowo to {wrd_shf}, zgadnij jakie to slowo")

usr_wrd = input("Co to za słowo?: ")
while True:
    if usr_wrd != ran_wrd:
        print("To nie to słowo, spróbuj jeszcze raz...")
        usr_wrd = input("Co to za słowo?: ")
    else:
        print("Brawo! Zgadłeś")
        break

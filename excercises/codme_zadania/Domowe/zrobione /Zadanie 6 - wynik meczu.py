score =""
sep = ":"
while True:
    score = str(input("Podaj wynik meczu: "))
    if score.find(sep) > 0:
        score_list = score.split(":")
        score1 = int(score_list[0])
        score2 = int(score_list[-1])
        if int(score1) == int(score2):
            print("remis")
            break
        elif score1 > score2:
            print(f"Gospodarze wygrali {score1 - score2} bramkami ")
            break
        else:
            print(f'goście wygrali {score2 - score1} bramkami')
            break
    else:
        print("Podaj wynik w formacie x:x")


def rep_lace(word,let1, let2):
    str2 = ""
    txt_list = list(word)
    idx = txt_list.index(let1)
    txt_list[idx] = let2
    for let in txt_list:
        str2 += let
    print(str2)
    return str2

rep_lace("Tekst", "k", "U")


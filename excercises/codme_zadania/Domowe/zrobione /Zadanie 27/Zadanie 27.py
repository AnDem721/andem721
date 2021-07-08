def get_text():
    with open("Zadanie 27_txt.txt", "r", encoding="utf-8" ) as source_txt:
        src_txt = source_txt.readlines()
        full_txt = []
        for line in src_txt:
            lista = line.split("\n")
            full_txt.append(lista[0].replace(".","").replace(",","").replace(":","").lower())
    return full_txt


def transform_to_dict(full_txt):
    txt_lines = {"1" : "", "2" : "", "3" : "", "4": ""}
    txt_lines = dict(zip(txt_lines, full_txt))
    return txt_lines


def print_row_info():
    txt_lines = transform_to_dict(get_text())
    for key, value in txt_lines.items():
        print(f"Wiersz {key} :", value)
        print(f"Długość wiersza to: ", len(value))
        value_letters = list(value.replace(" ", ""))
        letter_dict = {}
        for letter in value_letters:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
        print(f"najczęściej występującą literą jest: ", max(letter_dict, key=letter_dict.get))
        print()


def common_word(full_txt):
    tekst = []
    for line in full_txt:
        tekst.append(line.split(" "))
    tekst = [item for elem in tekst for item in elem]
    words_dict = {}
    for word in tekst:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    print(f"Najczęściej występujące słowo w tekście to: ", max(words_dict, key=words_dict.get))

def main():
    print_row_info()
    full_txt = get_text()
    common_word(full_txt)

main()
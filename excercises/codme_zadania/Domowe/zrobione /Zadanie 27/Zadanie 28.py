import random
def get_text():
    with open("Zadanie 27_txt.txt", "r", encoding="utf-8") as source_txt:
        src_txt = source_txt.readlines()
    full_txt = []
    for line in src_txt:
        lista = line.split("\n")
        full_txt.append(lista[0])
    return full_txt

def print_random(full_text):
    print(random.sample(full_text, 1))

# print(get_text())
full_text = get_text()
print_random(full_text)
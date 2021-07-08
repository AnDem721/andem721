#Napisz program, który wyświetli tylko zakomentowane linijki we wszystkich plikach Pythonowych w bieżącym folderze
import os

def get_all_python_files():
    files = os.listdir()
    python_files = []
    for file in files:
        if file[-3:] == ".py":
            python_files.append(file)
    return python_files

def get_all_hash(python_files):
    hash_text = []
    for file in python_files:
        with open(file, "r", encoding="utf-8") as f:
            file_text = f.read().split("\n")
            # print(file_text)
            for text in file_text:
                text.lstrip()
                if text.find("#") >= 0:
                    hash_text.append(text[text.find("#"):])
                else:
                    pass
    return hash_text

def print_hash_text(hash_text):
    for text in hash_text:
        print(text)


def main():
    python_files = get_all_python_files()
    print(python_files)
    print_hash_text(get_all_hash(python_files))

main()
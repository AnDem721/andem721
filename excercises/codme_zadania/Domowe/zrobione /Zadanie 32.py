#Napisz program, który wyświetli nazwę największego pliku w bieżącym katalogu
import os

files = os.listdir()
max_file_size = 0
max_file_name = ""
for file in files:
    if os.path.isfile(file):
        file_size = os.path.getsize(file)
        if file_size > max_file_size:
            max_file_size = file_size
            max_file_name = file
print("największy plik to", max_file_name, " o rozmiarze: ", max_file_size / (1024*1024), "MB")



import sys
try:
    file_name = sys.argv[1]
except IndexError:
    print("Nie podano nazwy pliku")
    exit()
def ponumeruj(nazwa_pliku):
    with open(nazwa_pliku) as f:
        # for line in f:
        #     print(line)
        for i, line in enumerate(f, start=1):
            print(i, line.rstrip())

try:
    ponumeruj(file_name)
except FileNotFoundError:
    print("Nie ma takiego pliku!")
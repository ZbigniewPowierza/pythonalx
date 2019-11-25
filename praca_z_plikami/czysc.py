# python czysc.py emails.txt przeczyszczone.txt
# "\n".join(emails)

with open("dane/emails.txt") as f:
    print(f.read())

import sys
try:
    file_name = sys.argv[1]
except IndexError:
    print("Nie podano nazwy pliku")
    exit()
def otworz(nazwa_pliku):
    with open(nazwa_pliku) as f:
        for line in f:
            wynik = []
            if line.count("@")==1:
                line.lower()
                if
                wynik.add(line)

                print(line)
try:
    otworz("dane/"+file_name)
except FileNotFoundError:
    print("Nie ma takiego pliku!")

def czysc
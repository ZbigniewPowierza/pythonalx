"""
napisz funkcje ktora otworzy podany jako argument plik (podana nazwa pliku lub sciezka)
i wypisze go numerujac linie

plik.txt
raz
dwa
trzy

Wynik
1 Raz
2 Dwa
3 Trzy

2. Pozwól na uruchomienie programu z commad line

$python numerator.py test
"""

# with open("test") as f:
#     print(f.read())

def otwieranie_pliku(string):
    with open ("string") as f:
    return print (f.read ())

otwieranie_pliku("test.txt")
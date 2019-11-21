# a) Napisz funkcje, ktora wymnozy  przez siebie elementy podane w liscie wejsciowej

def pomnoz(lista):
    wynik = 1
    for i in lista:
        wynik = wynik * i
    return wynik


print(f"Wynik mnożenia elemtów listy będących parametrami funkcji (pomnoz([1, 5, 4])) to", pomnoz([1, 5, 4]))
print("Wynik mnożenia elemtów listy to", pomnoz([1, 5, 4]))
lista = [10, 10, 2]
print(pomnoz(lista))

# b) Napisz funkcje, ktora wymnozy  przez siebie nieokresloną liczbę argumentów

# c) napisz funkcje ktora wybierze i zwrocu z podanego napisu liste liczb

# x = "a1b2c1d2"
# [1,2,1,2]

# x = "a100b200"
# [1, 0, 0, 2, 0, 0]

for i, j in enumerate("0123456789"):
    print(i, j, j.isdigit())


def cyfry_z_napisu(napis):
    rezultat = []
    for i in napis:
        if i.isdigit():
            rezultat.append(i)
        # else:  #- nie jes potrzebna ta i poniższa linijka
        #     continue
    return rezultat

napis = "a1b2c1d2"
print(cyfry_z_napisu(napis))

napis = "a100b200"
print(cyfry_z_napisu(napis))
# d)
# x = "a100b200"
# #[100, 200]

def liczby_z_napisu(napis):
    pozycje = []
    cyfry = []
    for i, j in enumerate(napis):
        print(i, j, "Czy liczba -", j.isdigit())
        if j.isdigit():
            print(i, j, "Tylko liczby -", j.isdigit())
            pozycje.append(i)
            cyfry.append(j)
        # else:  #- nie jes potrzebna ta i poniższa linijka
        #     continue
        for k in pozycje:
            if k+1 == pozycje(k+1):
                liczby = pozycje[k]
    return pozycje, cyfry


napis = "a100b200"
print(liczby_z_napisu(napis))
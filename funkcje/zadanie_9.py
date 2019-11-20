# a) Napisz funkcje, ktora wymnozy  przez siebie elementy podane w liscie wejsciowej

def pomnoz(lista):
    wynik = 1
    for i in lista:
        wynik = wynik * i

    return wynik

print(pomnoz([1, 5, 4]))
lista = [10, 10, 2]
print(pomnoz(lista))

# b) Napisz funkcje, ktora wymnozy  przez siebie nieokresloną liczbę argumentów

# c) napisz funkcje ktora wybierze i zwrocu z podanego napisu liste liczb

# x = "a1b2c1d2"
#[1,2,1,2]

# x = "a100b200"
#[1, 0, 0, 2, 0, 0]

for i, j in enumerate("0123456789"):
    print(i, j, j.isdigit())

# def cyfry_z_napisu(string):
#     rezultat = []
#     for i in string:
#         if i.isdigit

# d)
# x = "a100b200"
# #[100, 200]
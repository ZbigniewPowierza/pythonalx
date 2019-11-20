# przypomnienie
# int, float, complex, str,
# list -> [], tuple -> ()
# dict -> {}
# przypomnienie
# int,  ,float , com
#
# dict {}
#
#    pol_ang = {
#       # "klucz": "Wartość"
#        "klucz": "key",
#        "wartosc": "value",
#        "pies": "dog"
#    }

#    print(pol_ang)
#    print(pol_ang["pies"])
#    # print(pol_ang["dog"]) - zwróci błąd do nie ma takiego klucza w słowniku

#    if "dog" in pol_ang:
#        print(pol_ang["dog"])

#    print(dir(pol_ang))

#    print(pol_ang.get("dog"), "Brak takiego hasła")

#    pol_ang["kot"] = "cat"
#    print(pol_ang)
# nie wszystkoi moze byc kluczem - listy nie, nie mogą być obiekty mutowalne
# print({1: "a", 2: "b", 1.1: "c"})

# print(dict())
# x = dict()
# print(type(x))

pol_ang = {
    # "klucz": "wartosc"
    "klucz": "key",
    "wartosc": "value",
    "pies": "dog"
}

print(pol_ang)
print(pol_ang["pies"])
print("dog" in pol_ang)

if "dog" in pol_ang:
    print(pol_ang["dog"])

print(dir(pol_ang))

print(pol_ang.get("dog", "Brak takiego hasła"))
print(pol_ang.get("pies", "Brak takiego hasła"))

pol_ang['kot'] = "cat"

print(pol_ang)
# kluczem moga byc liczby, napisy, tuple
print({1: "a", 2: "b"})
print({1.1: "a", 2.1: "b"})
print({(1, 2): "pierwsza"})
# print({[1, 2]: "pierwsza"}) #to sie nie uda bo lista jest niehaszowalna

print(pol_ang.keys())
print(pol_ang.values())
print(pol_ang.items())

# set -> {}
# zbior - kolekcja unikalnych i nieuporzadkowanych wartosci
zbior = {1, 2, 3, 4}
print(zbior, type(zbior))
print(dir(zbior))

zbior2 = {1, "a", 2, "b", "c", "z", 3}
zbior2.add(9)
print(zbior2)
zbior2.add("a")
print(zbior2)

lista = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 4, 6, 3, 3, 3, 3, 3, 7, 7, 7, 7]
print(set(lista))

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {1, 2}
print("Suma zbiorów: ", A | B, A.union(B))
print("Różnica zbiorów: ", A - B, A.difference(B))
print("Część wspólna, przecięcie: ", A & B, A.intersection(B))
print("Różnica symetryczna: ", A ^ B, A.symmetric_difference(B))
print("Podzbiór", A.issubset(C))
print("Podzbiór", C.issubset(A))

# # Zadanie na dziś.
# # Korzystając z modułu random (np random.shuffle)
# # Zrób takie mapowanie poniższych list, by każda osoba kupiła prezent komuś innemu
# # np:
# osoby = ['marek', 'przemek', "michał", "kamila"]
# osoby2 = ['marek', 'przemek', "michał", "kamila"]
# # tutaj wasza magia:
# # i sprawdzamy - z wykorzystaniem funkcji zip
# for os1, os2 in zip(osoby, osoby2):
#     print(f"{os1} kupuje prezent {os2}")
# # i przykładowy wynik:
# # marek kupuje prezent przemek
# # michał kupuje prezent kamila
# # kamila kupuje prezent marek
# # przemek kupuje prezent michał

from random import shuffle
osoby = ['marek', 'przemek', "michał", "kamila"]
osoby2 = ['marek', 'przemek', "michał", "kamila"]

def is_in_same_position(lista1, lista2):
    for i, os in enumerate(lista1):
        # print(f"- {lista1[i]} i {lista2[os]}")
        if os == lista2[i]:
            return True
    return False

print(is_in_same_position(osoby, osoby2))

while is_in_same_position(osoby, osoby2):
    print("Coś się powtarza")
    shuffle(osoby2)


# while True:
#     shuffle (osoby2)


for os1, os2 in zip(osoby, osoby2):
    print(f"{os1} kupuje prezent {os2}")
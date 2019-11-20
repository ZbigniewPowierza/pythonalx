# from random import shuffle

osoby = ['marek', 'przemek', "michał", "kamila"]
osoby2 = ['marek', 'przemek', "michał", "kamila"]


# def is_in_same_position(lista1, lista2):
#     for i, os in enumerate(lista1):
#         # print(f"- {lista1[i]} i {lista2[os]}")
#         if os == lista2[i]:
#             return True
#     return False
#
#
# print(is_in_same_position(osoby, osoby2))

for nr, wart in enumerate(osoby):
    print(nr, wart)
    if wart == osoby2(nr):
        print("Kolejność elementów list 'osoby' i 'osoby2' są identyczne")
        break
    else:
        osoby2.sort(reverse=True)

# print()
# for nr2, wart2 in enumerate(osoby2):
#     print(nr2, wart2)
#     # if wart == osoby2(nr):
#     #     print("Kolejność elementów list 'osoby' i 'osoby2' są identyczne")
#     #     # osoby2 = osoby2.sort(reverse=True)
#     #     # continue


# while is_in_same_position(osoby, osoby2):
#     print("Coś się powtarza")
#     shuffle(osoby2)
#
# # lub w ten sposób robimy to samo
# # while True:
# #     shuffle (osoby2)
#
#
# for os1, os2 in zip(osoby, osoby2):
#     print(f"{os1} kupuje prezent {os2}")

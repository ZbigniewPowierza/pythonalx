# powtórka z obslugi plików

fd = open ("dane.txt", "rt")
# for linia in fd:
#     print (linia)
# for linia in fd:
#     print (linia, end= "")
# for index, linia in enumerate(fd, 1):
#     print ("krok", index, ":", linia, end= "")
# fd.close()

# with open("dane.txt", "rt") as fd:
#     for index, linia in enumerate (fd, 1):
#         print ("krok", index, ":", linia, end="")
# print("czy plik zamknięty", fd.closed)

with open("dane.txt", "rt") as fd:
    for index, linia in enumerate (fd, 1):
        print ("krok", index, ":", linia, end="")
print("\nCzy plik zamknięty", fd.closed) # jak widać plik jest zamknięty, pomimo braku metody close, to daje konstruktor "with open"

# https://jsonlint.com/ - sprawdzanie json-ów

# http://api.nbp.pl/api/exchangerates/tables/A?format=json/
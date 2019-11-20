"""
funkcje anonimowe

"""

x = lambda a, b : a*b
print(x(10, 6))

def fun_sort(x):
    return x[1]

lista = [('Winogrona', 10), ('Jabłko', 2,99), ('Banan', 4,99)]
print(sorted(lista))
print(sorted(lista, key=fun_sort))
print(sorted(lista, key=lambda x: x[1]))

# napisz funkcje ktora z zadanej listy wybierze elementy okreslone przez funkcje klucza
# lista = [1, 2, 3, 4, 5, 6]
# wybierz(lista, key: lambda x= x%2 == 0)
# [2, 4, 6]
# wybierz(lista, key: lambda x= x > 5)
# [6]

"""
lista_liczb = [1, 2, 3, 4, 5, 6]
def wybierz(lista_liczb, funkcja):
    wynik = []
    for el in lista:
        if funkcja(el) is True:
            wynik.append(el)
    return wynik

print(wybierz(lista_liczb, lambda x: x%3 ==0))
"""

# zrob funkcje przycinającą listę na podstawie warunku początkowego i końcowego

# >>>przytnij(
#       data=[1, 2, 3, 4, 5, 6, 7],
#       start=lambda x: x>3,
#       stop=lambda x: x ==6,
#           )
#   [4, 5, 6]
data=[1, 2, 3, 4, 5, 6, 7]
def przytnij(data, start, stop):
    wynik = []
    for i in data:
        print(i)
        if start(i) is True:
            if stop(i) is True:
                wynik.append(i)
            else:
                continue
        return wynik

print(przytnij(data, lambda x: x>3, lambda x: x ==6))
print(sorted([1, 2, 3, 4, 5, 6, 7], key=lambda x: x>3, key=lambda x: x ==6))

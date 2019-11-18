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

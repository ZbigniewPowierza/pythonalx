# napisz funkcje ktora policzy maksimum z 3 podanych liczb

# max_of_three(10, 1, 17)
#17

# w celu rozwiazania mozna napisac wiecej niz jedna funkcje

lista = [10, 2, 5]

def max_of_two(x, y):
    if x > y:
        return x
    return y
def max_of_three(a, b, c):
    if c > max_of_two(a, b):
        return c
    return max_of_two(a, b)

print(max_of_three(100, 213, 0))
print(max_of_three(-1, -2, 0))

"""
max_of_three = lista[0]
for i in lista:
    if i > max_of_three:
        max_of_three = i
    else:
        continue

print(max_of_three)

def max_of_three(lista):
    wynik = lista[0]
    for i in lista:
        if i > wynik:
            wynik = i
        else:
            continue
    return wynik

print(max_of_three(lista))

"""

def max_of_three2(x, y, z):
    wynik2 = x
    if y > x and z < y:
        wynik2 = y
    elif y < x and z > x:
        wynik2 = z
    return wynik2

print(max_of_three2(-1,-5,-10))

# def max_of_three3(x, y, z): zrobić w domu
#     return max_of_two(max_of_two())
#
#     wynik3 = x
#     if y > x and z < y:
#         wynik2 = y
#     elif y < x and z > x:
#         wynik2 = z
#     return wynik2

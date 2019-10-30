# definicja funkcji, procedury, zestawu instrukcji
def nazwa_funkcji(): # ta funkcja nie przyjmuje argumentów
    # ciało f-kcji
    #blok instrukcji
    print("Hello World!")
    # pass
# wywołanie funkcji
nazwa_funkcji()

def funkcja_z_argumentem(x, y, z):
    pass

def funkcja_z_argumentem(x):
    """

    x- argument mojej funckji Mogę uzywać go
    wewnątrz nbiej. bedzie dostepny przez x
    :param x:
    :return:
    """

def do_piatej(liczba):
    print(liczba**5)
    return liczba**5
x = do_piatej(4)
print(x)

# napisz funkcję któr przymien napis i zwroci kopie napisu zamieniona na duze litery

def na_duze_litery(napis):
    return napis.upper()

print(na_duze_litery("ala ma kota"))


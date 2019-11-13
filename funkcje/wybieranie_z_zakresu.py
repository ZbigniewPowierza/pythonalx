"""
lista = [-2, 10, 0, 5, 1, 16, 9]
wybierz z przedziału(lista, 5, 10)
[10, 5, 9]

"""

def wybierz_z_przedzialu(kolekcja_typu_lista, liczba1, liczba2):
    wynik = []
    for i in kolekcja_typu_lista:
        if liczba2 >= i >= liczba1:
            wynik.append (i)
    return wynik

def test_wybierz_z_przedzialu_pusta_lista():
    assert wybierz_z_przedzialu ([], 10, 20) == []

def test_wybierz_z_przedzialu():
    assert wybierz_z_przedzialu ([1, 10, 11, 20, 30], 10, 20) == [10, 11, 20]
    assert wybierz_z_przedzialu ([1, 10, 11, 20, 30], 0, 1) == [1]

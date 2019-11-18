"""
funkcja z dowolna liczba parametrow

"""


# funkcja mnozy wartosci podane do jej srodka
# mozliwe podanie nieznanej liczby parametrow
"""
def iloczyn(*args):
    wynik = 1
    for nr, arg in enumerate (args, 1):
        #wynik = wynik * arg
        wynik *= arg
        #print (f"Pozycja {nr} = {arg}")
    return wynik

print(iloczyn(1, 2, 5))
"""

def iloczyn(start, *args):
    wynik = start
    for nr, arg in enumerate (args, 1):
        #wynik = wynik * arg
        wynik *= arg
        #print (f"Pozycja {nr} = {arg}")
    return wynik


print(iloczyn(2, 1, 2, 5))
print(iloczyn(2))
# print(iloczyn()) # bedzie błąd, bo musi być wypełniony prezynajmniej jeden element (start)

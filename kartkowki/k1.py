#  zad 1 - typy danych

# str
# int
# float
# complex
#
# bool
# none

# zad 2 - struktury danych

# tuple
# list
# dict
# set
#
# # zad 3 - sortowanie listy- 2 sposoby
#
# lista = [1,2,3]
# lista.sort()
# sorted(lista)
#
# # zad 4
# ###
# slownik = {}
# slownik{'ala'} # dostane wyjątek, bo nie ma takiego klucza
#
# if 'ala' in slownik:
#     print(slownik['ala'])
#
# slownik.get('ala')  #domyslnie zwracana jest wartość None, jeśli klucza nie ma
# slownik.get('ala', "brak")  #brak jest domyślną wartością
# ###
# zad 5

def zlacz_teksty(a, b):
    c = a + b
    return c[::-1]

print(zlacz_teksty('ala ma kota', 'a kot ma ale'))
"""
przekazywanie listy parametrow nazwanych
"""

# def fun_parametry(**kwargs):
#     print(kwargs)
#     print(kwargs["imie"])
#
# fun_parametry(imie="Jan", nazwisko="Kowalski", email="jk@firma.pl",
#               wiek=44)

def fun_parametry(nr, **kwargs):
    print(kwargs)
    print("Imie: ", kwargs["imie"])
    print ("Imie: ", kwargs.get("imie", "-brak-")) #nawet jak nie bedzie rekordu z polem imie to nie wywali bledu

fun_parametry(102, imie="Jan", nazwisko="Kowalski", email="jk@firma.pl",
              wiek=44)


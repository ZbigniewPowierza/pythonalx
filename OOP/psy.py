#  najprstsza klasa, istnieje , nic nie robi
class Pies:
    pass

# tworze instancje klasy Pies
# jest przypisana do zmiennej azor
azor = Pies()

print(azor)
print(isinstance(azor, Pies))
print(dir(azor))
# otrzymujemy specjalne (bo podkreslenia), skad one sie wziely
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '
# __format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__']

# dziedziczą z klasy Obiekt

print(isinstance(azor, object))
print(isinstance(print, object))
try:
    print(azor.waga)
except Exception:
    print("Coś nie tak jezeli chodzi o azor.waga - moze jeszcze nie ma tego atrybutu")
azor.waga = 10
print(azor.waga)
azor.waga =+1
print(azor.waga)
reks = Pies()
print(azor == reks)
print(azor, reks)
# wynik <__main__.Pies object at 0x002AE148> <__main__.Pies object at 0x002AE340> - widac ze to inne adresy

class Pies:
    def __init__(self, imie, waga):
        self.imie = imie
        self.waga = waga

    def szczekaj(self):
        print(f"(self.imie} szczeka")
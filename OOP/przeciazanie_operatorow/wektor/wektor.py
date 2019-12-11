# Zaimplementuj klase Vector dostarczajaca funkcjonalnosc wektora
# swobodnego na dwuwymiarowej płaszczyznie. Wektory powinny
# miec mozliwosc dodawania, odejmowania, mnozenia (przez inny
# wektor i przez liczbe), porównywania (po długosci) oraz powinny
# posiadac czytelna reprezentacje napisowa.
# Przykład uzycia:
# vector_1 = Vector(x=1, y=2)
# vector_2 = Vector(x=1, y=2)
# vector_3 = vector_1 + vector_2

class Wektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Wektor(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __mul__(self, other):
        if isinstance(other, int):
            return Wektor(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    def __gt__(self, other):
        return self.lenght > other.lenght

    @property
    def lenght(self):
        return (self.x ** 2+ self.y ** 2)

    # def __eq__(self, other):
    #     return self.x == other.x a

    # def __add__(self, other):
    #     if isinstance(other, int):
    #         return MyInt(str(other + self.i))
    #     return MyInt(str(self.i + other.i))
    #
    # def __radd__(self, other):
    #     return self.__add__(other)
    #
    # def __eq__(self, other):
    #     return self.i == other.i
    #
    # def __sub__(self, other):
    #     return MyInt (str (self.i - other.i))
    #
    # def __str__(self):
    #     return f"<MyInt: {self.repr}>"
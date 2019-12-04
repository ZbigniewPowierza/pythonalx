""""
Utworz klase Product
ktora bedzie dzialac tak:
NazwaKlasy
# >>> from produkt import Product
# >>> pr = Product(1, "woda", 10.99)
# >>> pr.id
# >>> 1
# >>> pr.name
# >>> 'woda'
# >>> pr.price
# >>> 10.99
# >>> pr.show()
# >>> 'Woda (1), cena: 10.99'
"""

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def show(self):
        return f"{self.name} ({self.id}), cena: {self.price}"


def test_product():
    pr = Product(1, "woda", 10.99)
    assert pr.id == 1
    assert pr.name == "woda"
    assert pr.price == 10.99

def test_product_show():
    pr = Product(1, "woda", 10.99)
    assert pr.show() == "woda (1), cena: 10.99"
"""

utworz klase produkt
ktora bedzie dzialac tak:
# >>> from produkt import Product
# >>> pr = Product(1, "woda", 10.99)
# >>> pr.id
# >>> 1
# >>> pr.name
# >>> "woda"
# >>> pr.show()
# >>> 'Woda (1), cena: 10.99'

"""
class Product:
    def __int__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

def test_product():
    pr = Product(1, "woda, 10.99")
    assert pr.id == 1
    assert pr.name == "woda"
    assert pr.price == 10.99

def show(self):
    return f"{self.name} ({self.id}), cena: {self.price}"
    #print(f"{self.name, (self.id), self.price}")

def test_product_show():
    pr = Product(1, 'woda', 10.99)
    assert pr.show() == "woda (1), cena: 10.99"

class Product:
    def __int__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def show(self):
        return f"{self.name} ({self.id}), cena: {self.price}"
        #print(f"{self.name, (self.id), self.price}")

class Product2:
    NEXT_ID = 1 #atrybut klasowy
    def __int__(self, name, price):
        self.id = self.get_id() #pobieram atrybut klasowy i przypisuje do instancji
        self.name = name
        self.price = price
        self.incr_next_id()

    @classmethod
    def incr_next_id(cls):
        cls.NEXT_ID += 1
    @classmethod
    def incr_next_id(cls):
        cls.NEXT_ID += 1

    def show(self):
        return f"{self.name} ({self.}"

def test_product2():
    pr = Product2("woda, 10.99")
    pr2 = Product2 ("wóda, 20.22")
    assert pr.id == 1
    assert pr.name == "woda"
    assert pr.price == 10.99
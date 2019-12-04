from collections import namedtuple

Item = namedtuple("Item", ["product", "quantity"])

class Basktet:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        item = Item(product=product, quantity=quantity)
        self.items.append(item)

    def count_total_price(self):
        price = 0
        for item in self.items:
            price += item.product.price * item.quantity
        return price


    def generate_report(self):
        output = "Produkty w koszyku:\n"
        for item in self.items:
            output += f"- {item.product.name} ({item.product.id}), cena: {item.product.price} * {item.product.quantity}"
        output += f"W sumie: (self.count_total_price()}"
        return output


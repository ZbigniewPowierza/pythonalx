from produkt_rkorzen import Product
from basket import Basket


class TestBasket:
    def test_create_basket(self):
        basket = Basket ()
        assert True

    def test_add_product_to_basket(self):
        basket = Basket ()
        product = Product ("Woda", 10)
        basket.add_product (product, 5)
        assert len (basket.items) == 1
        product2 = Product ("Wóda", 25)
        basket.add_product (product2, 3)
        assert len (basket.items) == 2
        Product._NEXT_ID = 1

    def test_count_total_price(self):
        basket = Basket ()
        product = Product ("Woda", 10)
        basket.add_product (product, 5)
        assert basket.count_total_price () == 50
        product2 = Product ("Wóda", 25)
        basket.add_product (product2, 3)
        assert basket.count_total_price () == 75
        Product._NEXT_ID = 1

    def test_gennerate_report(self):
        basket = Basket ()
        product = Product ("Woda", 10)
        basket.add_product (product, 5)
        expected = """Produkty w koszyku:
- Woda (5), cena: 10 x 5
- Wóda (6), cena: 25 x 3
W sumie: 125 """
        assert basket.generate_report() == expected
        Product._NEXT_ID = 1

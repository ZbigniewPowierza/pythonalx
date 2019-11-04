import unittest


"""
napisz funkcję która sprzawdzi czy podana liczba jest liczba pierwsza

"""

def czy_pierwsza(x):
    """sprawdza czy x jest liczba pierwszą

    przykłady użycia:
    #przykład użycia doctestów
    >>> czy_pierwsza(10)
    False
     >>> czy_pierwsza(7)
    True
    """
    for i in range(2, x):
        if x % i == 0:
            return False

    return True

# print(help(czy_pierwsza())
# prymitywna forma testów - bez zadnego frameworka
#assert czy_pierwsza(3) is True
#assert czy_pierwsza(10) is False
#assert czy_pierwsza(11) is True

# unittesty

# class TestCzyPierwsza(unittest.TestCase):
#     def test_czy_pierwsza_dla_liczby_pierwszej(self):
#        self.assertEqual(czy_pierwsza(7), True)
#        self.assertEqual(czy_pierwsza(11), True)
#
#     def test_czy_pierwsza_dla_liczby_niepierwszej(self):
#         self.assertIs(czy_pierwsza(10), False)
#         self.assertIs(czy_pierwsza(20), False)
#         self.assertIs(czy_pierwsza(21), False)

class TestCzyPierwsza(unittest.TestCase):
    def test_czy_pierwsza_dla_liczby_pierwszej(self):
       assert(czy_pierwsza(7), True)
       assert(czy_pierwsza(11), True)

    def test_czy_pierwsza_dla_liczby_niepierwszej(self):
        assert(czy_pierwsza(10), False)
        assert(czy_pierwsza(20), False)
        assert(czy_pierwsza(21), False)
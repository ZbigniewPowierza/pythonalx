from wektor import Wektor

class TestWektor:

    def test_create_wektor(self, x, y):
        w = Wektor(x, y)
        assert True

    def test_add(self):
        v1 = Wektor(1, 2)
        v2 = Wektor(2, 2)
        v = v1 + v2
        assert v.x == 3
        assert v.y == 4
        assert v == v3

    def test_sub(self):
        v1 = Wektor(1, 2)
        v2 = Wektor(2, 2)
        v3 = Wektor(-1, 0)
    assert v1 - v2 == v3

    def test_multiply_by_other_wektor(self):
        v1 = Wektor(1, 2)
        v2 = Wektor(2, 2)
    assert v1 * v2 == 6

    def test_multiply_by_int(self):
        v1 = Wektor(1, 2)
        v2 = Wektor(2, 2)
    assert v1 * v2 == 6

    def test_lenght(self):
        v = Wektor(3, 4)
        assert v.lenght == 5
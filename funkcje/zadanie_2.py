"""
napisz funkcje zwracajacą zbiór znaków występujacych w danym napisie
więcej niż podana liczba razy:
# np:
# >>> wiecej_niz("ala ma kota a kot ma ale", 3)
# {'a', ' ')
"""
def wiecej_niz(text, b):
    #pass
    result = set()
    for s in set(text):
        if text.count(s) > b:
            result.add(s)
    return result

def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("", 0) == set() # nie {}

def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("aaa bbb cc d", 2) == {"a", "b", " "}

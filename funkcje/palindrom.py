# Napisz  funkcje ktora sprawdzi czy dany tekst jest palindromem

# is_palindrom("kajak") is True
# is_palindrom("kot") is False

def is_palindrom(tekst):
    tekst = tekst.lower()
    signs_to_remove = " .,;!?"  #pierwszy znak to spacja
    for s in signs_to_remove:
        tekst = tekst.replace(s, "")
    return tekst == tekst[::-1]

    # if tekst.replace(" ", "").replace (".", "").lower() == tekst[::-1].replace(" ", "").replace (".", "").lower():
    #     return True
    # else:
    #     return False

# print(is_palindrom("kajak"))
# print(is_palindrom("Kajak"))
# print(f" Czy 'kajak' to palindron:  - {is_palindrom("kajak")}")

def test_is_palindrom_for_palindrom():
    assert is_palindrom("kajak") is True
    assert is_palindrom ("kajak") is True
    assert is_palindrom ("A to idiota") is True
    assert is_palindrom ("A to idiota.") is True
    assert is_palindrom ("Ada, gmina za nim gada.") is True

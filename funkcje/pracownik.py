"""
tworzenie rekordu pracownika - dwa parametry obowiązkowe, dwa opcjonalne
ma zwrocic zmienną typu słownik

"""

def utworz_pracownika(imie, nazwisko, email='info@firma.pl', telefon=None):
    pracownik = dict()
    pracownik["imie"] = imie
    pracownik["nazwisko"] = nazwisko
    pracownik["email"] = email
    pracownik["telefon"] = telefon
    return pracownik

print(utworz_pracownika("Jan", "Kowalski"))
print(utworz_pracownika("Adam", "Nowak", "anowak@firma.pl", "501126356"))

print(utworz_pracownika("Jan", "Zielak", telefon="601453623"))

print(utworz_pracownika("Jan", "Zielak", email="jzielak@firma.pl"))
print(utworz_pracownika("Jan", "Zielak", "jzielak@firma.pl"))
print(utworz_pracownika("Jan", "Zielak", telefon="601453623", email="jzielak@firma.pl"))
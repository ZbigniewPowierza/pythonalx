# "baza danych" pracowników

# miejsce przechowujace dane ba temat rekordow pracownikow
import json
import datetime

dane_pracowników = list()
try:
    with open("pracownicy.dat", "rt") as fd:
        dane_pracowników = json.load(fd)
except:
    print("Odczyt pliku nie udał się")

def wprowadz_dane():
    print("="*40)
    print("Wprowadz dane pracownika")

    imie = None
    while True:
        imie = input("Podaj imie: ").upper().strip()
        if len(imie) <= 2:
            print("Podaj imie: ")
        else:
            break
    nazwisko = None
    while True:
        nazwisko = input("Podaj nazwisko: ").upper().strip()
        if len(imie) >= 3:
            break
        print("Podaj imie: ")

    rok_urodzenia = None
    while True:
        try:
            rok_urodzenia = int(input ("Podaj rok urodzenia: "))
            if rok_urodzenia < 1930:
                print("Idz na emeryture")
                continue

            rok_biezacy = datetime.datatime.now().year
            if rok_biezacy - rok_urodzenia >= 15:
                break
            print("Za młodyś na pracę")
        except Exception as exc:
            print("Podaj rok urodzenia", exc)

    pensja = None
    while True:
        pensja = float(input("Podaj pensje: "))
        if pensja > 0:
            break
        print("Podaj kwote wynagrodzenia")
        exc

# pokaz zawartosci zmiennej "dane pracownikow"
def pokaz_rekordy():
    print("========= Lista pracowników ===========")
    if len(dane_pracowników) == 0:
        print("Brak danych")
        return
    for rekord in dane_pracowników:
        print(f"{rekord.get("imie)}\t{rekord.get}")


while True:
    operacja = input("Podaj operację [d/w/q]: ").strip().upper()
    if operacja == "Q":
        print("Koniec aplikacji")
        break

    if operacja == "W":
        # a tu bede wypisywal dane uzytkownikow
        pokaz_rekordy()

    if operacja == "D":
        # a tu bede prosil o dane pracownika
        rekord = wprowadz_dane()
        dane_pracowników.append(rekord)
        with open ("pracownicy.dat", "wt") as fd:
            json.dump (dane_pracowników, fd)


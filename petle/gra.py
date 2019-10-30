import random

DEBUG = True

# lsujemy pocztkowe położenie gracza i skarbu

gracz_x = random.randint(1, 10)
gracz_y = random.randint(1, 10)
skarb_x = random.randint(1, 10)
skarb_y = random.randint(1, 10)

# obloczam odleglość po wylosowaniu
odleglosc_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

# w zależnosci od wartosci zmiennej DEBUG
# printuje info o położeniu skarbu i gracza

if DEBUG:
    print(f"Połozenie gracza (x={gracz_x}, y={gracz_y})")
    print(f"Połozenie skarbu (x={skarb_x}, y={skarb_y})")
    print(f"Minimalna liczba ruchów = {odleglosc_po_wylosowaniu}")

print("""
Witaj!
Twoim zadaniem jest odnalezienie Skarbu!
Możesz się poruszać wpisując komendy:
w - góra
s - dół
a - lewo
d - prawo
UWAŻAJ! MOżesz wypaść poza planszę.
Po każdym ruchu możesz dostać informację o tym czy się zbliżasz czy oddalasz.
ZACZYNAMY!
""")
l_ruchow = 0
while True:
    # pytamy gracza o ruch
    ruch = input("Wpisz komendę (a-lewo, w-góra, d-prawo, s-dół)")
    odleglosc_przed_ruchem = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    # zmieniamy pozycję gracza - zgodnie z komendą
    if ruch == "a":
        gracz_x = gracz_x - 1
    elif ruch == "s":
        gracz_y = gracz_y - 1
    elif ruch == "d":
        gracz_x += 1
    elif ruch == "w":
        gracz_y -= 1
    else:
        print("Trzymaj się reguł ...!#!#$%$!")
        continue # żeby nie by było "bez zmian"

    if DEBUG:
        print(f"Położenie gracza po ruchu (x={gracz_x}, y={gracz_y})")
        print(f"Położenie skarbu (x={skarb_x}, y={skarb_y})")

    # po ruchu robimy sprawdzenia
    if not (1 <= gracz_x <= 10 and 1 <= gracz_y <= 10):
        print("Wypadłeś poza planszę")
        break

    odleglosc_po_ruchu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

    if odleglosc_po_ruchu == 0:
        print("Wygrałeś!!!")
        break

    if DEBUG:
        print()
        print("#"*40)
        print(f"Odl przed: {odleglosc_przed_ruchem}")
        print(f"Odl po: {odleglosc_po_ruchu}")
        print(f"Położenie gracza po ruchu (x={gracz_x}, y={gracz_y})")
        print(f"Położenie skarbu (x={skarb_x}, y={skarb_y})")

    los = random.randint(1, 5)

    if los != 1:
        print("Przykro mi nie wylosowałeś podpowiedzi")
    else:
        if odleglosc_po_ruchu < odleglosc_przed_ruchem:
            print("Ciepło")
        elif odleglosc_po_ruchu > odleglosc_przed_ruchem:
            print("Zimno")
        else:
            print("Bez zmian")
        liczba_ruchow += 1  # liczba_ruchow = liczba_ruchow + 1
        if DEBUG:
            print("Liczba ruchów", liczba_ruchow)

        if liczba_ruchow > 2 * odleglosc_po_wylosowaniu:
            skarb_x = random.randint(1, 10)
            skarb_y = random.randint(1, 10)

            # Obliczam odleglosc po wylosowaniu
            odleglosc_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
            print("Jesteś Gapa! Skarb Zmienił położenie!! Hahaha!")

    # Zadanie domowe
    # Postaraj się w jakiejś formie zwizualizować położenia na planszy
    """
    To jest plansza bez gracza
    0000
    0000
    0000
    0000
    Plansza z grczem:
    0000
    00G0
    0000
    0000
    wcisam s:
    0000
    0000
    00G0
    0000
    ide w lewo i trafiam na skarb
    0000
    0000
    0S00
    0000
    plansza = [[0,0,0,0],[0,0,0,0],[0,S,0,0],[0,0,0,0]]
    """
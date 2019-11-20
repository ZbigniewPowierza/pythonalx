"""
OFERUJEMY NASTĘPUJĄCE PRODUKTY
marchew: 2,35, ziemniaki: 2,20, cebula: 1,8, ogórki: 4,0

co chcesz kupić? marchew
ile chcesz kupic [marchew]? 3

Za [marchew] płcisz 7,05 pPLN

DODAJEMY  obsluge magazynu
po zakupie ilosc towaru sie zmniejsza
jezeli ktos chce kupic wiecej niz w magazynie to mowie ze nie moze
"""
def wyprintuj(dict, jednostka):
    for k, v in dict.items():
        return print(f" - {k}: {v} ")

slownik = {
    'marchew': 2.35,
    'ziemniaki': 2.20,
    'cebula': 1.80,
    'ogórki': 4.00,
    # 'bataty': {'cena': 8.0, 'magazyn': 40}
    # 'bataty': [8, 40]
}
magazyn = {
    'marchew': 100,
    'ziemniaki': 200,
    'cebula': 50,
    'ogórki': 50,
}
print("Witaj w naszym PyZieleniaku")
print("OFERUJEMY NASTĘPUJĄCE PRODUKTY: ".title())
# for i in slownik:
#     print(f" - {i}: {slownik[i]}")
wyprintuj(slownik, "PLN")
# print(slownik.keys())
while True:
    tryb = input("Wybierz tryb: [z-zakupowy], [m-magazynowy] [k-kończymy]")
    if tryb.lower() == 'k':
        break
    elif tryb.lower() == 'z':
        while True:
            wyprintuj (slownik, "PLN")
            co_kupuje = input("Jaki towar chces kupić [wpisz k by zakończyć]").lower()
            if co_kupuje.lower() == 'k':
                break
            if co_kupuje in slownik:
                ile = input(f"Ile chcesz kupić [{co_kupuje}]")
                ile = float(ile)
                if ile <= magazyn[co_kupuje]:
                    naleznosc = ile * slownik[co_kupuje]
                    magazyn[co_kupuje] = magazyn[co_kupuje] - ile
                    # magazyn[co_kupuje] -= float (ile)
                    print(f"Za [{co_kupuje}] płacisz: {naleznosc:.2f} PLN")
                else:
                    print("Nie mam tyle kg tego towaru")
            else:
                print("Nie mam takiego produktu!")
    elif tryb.lower() == 'm':
        while True:
            print("W magazynie: ")
            # for product, ilosc in magazyn.items():
            #     print(f" - {product}: {ilosc} kg")
            wyprintuj(magazyn, "kg")
            #print(f"Lista towarów, których stan jest niższy od wyjściowego [{}")
            produkt_do_dodania = input("Co chcesz dodać?")
            ile_do_dodania = int(input("Ile chcesz dodać?"))
            if not produkt_do_dodania in slownik:
                cena_nowego_produku = float(input("Jaka będzie cena?"))
                slownik[produkt_do_dodania] = cena_nowego_produku




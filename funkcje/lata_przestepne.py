"""

Zaimplementuj funkcję zwracajaca lata przestepne na podstawie zadanego zakresu

lata_przestepne(1990, 2020)
[1992, 1996, 2000, 2004, 2008, 2016, 2020]

rok przestepny jest co cztery lata, o ile nie dzieli sie przez 100, za wyjatkiem gdy dzieli sie rowniez 400

"""
def czy_przestepny(rok):
#     if (rok%4 == 0 and rok%100 !=0) or rok%400 ==0:
# #   if (rok % 4 == 0 and rok % 100 != 0) or (rok % 4 == 0 and rok % 400 == 0): #tak też można napisać
#         return True
#     else:
#         return False
    return (rok%4 == 0 and rok%100 !=0) or rok%400 ==0

def lata_przestepne(rok_od, rok_do):
    if rok_od > rok_do: #walidacja zakresu lat
        return None

    lata = list()
    for rok in range(rok_od, rok_do+1):
        if czy_przestepny(rok):
            lata.append(rok)
    return lata

# print(lata_przestepne(2000, 2032))

def test_lata_przestepne():
    assert (lata_przestepne(2020, 2030) == [2020, 2024, 2028]) is True
#
# def test_lista_lat_przestepnych_pusta_lista():
#     assert lista_lat_przestepnych ([], 10, 20) == []
#
# def test_lista_lat_przestepnych():
#     assert lista_lat_przestepnych (2020, 2030) == [10, 11, 20]
#     assert wybierz_z_przedzialu ([1, 10, 11, 20, 30], 0, 1) == [1]
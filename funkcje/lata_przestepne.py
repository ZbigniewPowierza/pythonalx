"""

Zaimplementuj funkcję zwracajaca lata przestepne na podstawie zadanego zakresu

lata_przestepne(1990, 2020)
[1992, 1996, 2000, 2004, 2008, 2016, 2020]

rok przestepny jest co cztery lata, o ile nie dzieli sie przez 100, za wyjatkiem gdy dzieli sie rowniez 400

"""

def test_lista_lat_przestepnych_pusta_lista():
    assert lista_lat_przestepnych ([], 10, 20) == []

def test_lista_lat_przestepnych():
    assert lista_lat_przestepnych (2020, 2030) == [10, 11, 20]
    assert wybierz_z_przedzialu ([1, 10, 11, 20, 30], 0, 1) == [1]
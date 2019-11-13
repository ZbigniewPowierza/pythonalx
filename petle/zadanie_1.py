"""
Zapytaj użytkowniak o 10 liczba
i wypisz ich srednia
skorzystaj z pętli for oraz funkcji range()

"""

print(range(5))
suma = 0
for i in range(5):
    x: int = int(input("Podaj liczbę"))
    suma = suma + x
print(suma/5)


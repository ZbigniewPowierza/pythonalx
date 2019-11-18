"""
obliczanie silni
"""

# na podstawie rekurencji

# n! = n(n-1)!
import time

def silnia_rekurencja(n):
    if n<= 1:
        return 1
    else:
        return n*silnia_rekurencja(n-1)

def silnia_iteracyjnie(n):
    wynik = 1
    for i in range (1, n+1):
        wynik *= i
    return wynik

licznik = 10000
ts1 = time.time()
for i in range(0, licznik):
    silnia_rekurencja(800)
ts2 = time.time()
print("Czas dla rekurencji: ", ts2-ts1, " sekund")

ts1 = time.time()
for i in range(0, licznik):
    silnia_iteracyjnie(800)
ts2 = time.time()
print("Czas dla iteracji: ", ts2-ts1, " sekund")

print()
print(silnia_rekurencja(990))
print(i, silnia_iteracyjnie(990))
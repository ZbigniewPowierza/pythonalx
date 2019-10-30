# losowanie

import random

print(dir(random))
print(help(random.randint))
print(random.randint(1,10)) #loduje liczbę całk. z przedziału od 1 do 10

gracz_x = random.randint(1, 10)
gracz_y = random.randint(1, 10)

skarb_x = random.randint(1, 10)
skarb_y = random.randint(1, 10)

print("Połozenia gracza", gracz_x, gracz_y)
print("Połozenia skarbu", skarb_x, skarb_y)

odleglosc = abs(skarb_x - gracz_x) + abs(skarb_x - gracz_x)

while True:
    instrukcja = input("by zakończyć wciśnij 'k")

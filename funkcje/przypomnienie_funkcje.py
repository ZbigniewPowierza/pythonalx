def do_potegi(podstawa, wykladnik):
    return podstawa ** wykladnik

wynik = do_potegi(1,1)
wynik2 = do_potegi(2, 12)
print(wynik)

def unique_letters(text):
    u_letters = set(text)
    u_letters = "".join(u_letters)
    return u_letters, len(text)

dane = unique_letters("Rafał Korzeniewski")
print(dane)
print(type(dane))

print("litery: ", dane(0))
litery, długość = unique_letters("Rafał Korzeniewski")

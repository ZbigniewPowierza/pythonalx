# Zapytaj użytkowniaka o imię
# Wypisz powitanie
# Jak masz na imię ? Zbyszek
# Hello Zbyszek!

a = input("Jak masz na imię: ")
print("Hello" + " " + a + "!" )

a = input("Jak masz na imię")
print("Hello" + " " + a + "!" )
print("Hello {}!".format(a))
print(f"Hello {a}!")
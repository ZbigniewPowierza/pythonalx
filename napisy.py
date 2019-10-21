#
# Typ danych: napisy (albo string)
#
napis1 = "Ala ma kota"
napis2 = 'Ala ma kota'
napis3 = 'A to jest "cudzysłów" '
napis4 = "A to jest \"cudzysłów\" "
napus5 = "znaki specjalne: \t \n \r lalamido"

dlugosc = len(napis1)
print("Długość zmiennej napis1 to ", dlugosc, " znaków")
print(napus5)
#wiek = input("Podaj wiek:")
#print("Twój wiek to: ", wiek.strip())
s = "Ruda tańczy jak szalona"
print(s.capitalize()) #kapitaliki
print(s.upper())    #w gore
print(s.lower())    #w doł
print(s.title())    #formatowanie jako tytuł
print(s.swapcase()) #duze->male, małe na duże
print(s.center(1))   #centrowanie
print(s.center(100))
print(s.replace("R", "D"))  #zamiana znaków
print("Czy liczba: ", s.isdecimal())    #sprawdzanie czy string jest liczbą

print("4 litera to: ", s[3])    #pobierz 4-tą literę napisu
print("Litera przedostatnia to: ", s[-2])

print(s[0,5])

#   poproś uczestnika o podanie liczb x i y
#   na tej podstawie powiedz mu gdzie jest na planszy

x = int(input("Podaj współrzędną x punktu na planszy"))
y = int(input("Podaj współrzędną y punktu na planszy"))
#x, y = 51, 50

if x > 100 or x < 0 or y > 100 or y < 0:
    print("jesteś poza polem")
elif x <= 10 and y <= 10:
    print("Lewy Dolny Róg")
elif x >= 90 and y <= 10:
    print("Prawy Dolny Róg")
elif x <= 10 and y >= 90:
    print("Lewy Górny Róg")
elif x >= 90 and y >= 90:
    print("Prawy Górny Róg")
elif x <= 10 :
    print("Lewa Krawędź")
elif x >= 90:
    print("Prawa Krawędź")
elif y <= 10:
    print("Dolna Krawędź")
elif y >= 90:
    print("Górna Krawędź")
else:
    print("Jesteś w centrum")
# x < 10 or x > 90 or y < 10 or y > 90:
#ASCI
# a-z A-Z 0-9
# cofniecie karetki, itp.
# 7 bit - 128
# 1111111 = 1 + 2 + 4 + 8 + 16 + 32 + 64
# Unicode
# UTF-8 - kodowanie, każdy ze znaków od 1 do 4 bitów, początkowe są jak w ASCI

f = open("test")
print(f) #na razie to tylko uchwyt do pliku
# żeby przeczytać to np. w ponizszy sposob
for line in f:
    print(line)
f.close()

#print(dri(f))

f = open("test")
print(f.read())
f.close()

# zeby zabezpieczyć sie przed bledem nie zamkniecia pliku z powodu jakiegos bledu w kodzie
try:
    f = open("test")
    # coś tu robimy
except Exception:
    print("Wyjątek")
finally:
    f.close()


# prostsze rozwiazanie - manager konkekstu

with open("test") as f:
    print(f.read())

with open("test", encoding='utf-8') as f:
    print(f.read())



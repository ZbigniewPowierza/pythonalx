#
# array slicing
#

s = "Hello!"
print(s[-3])    #3-ci znak od końca
print(s[0:5])   #od indeksu 0 do 4 włącznie

s = "Ruda tańczy jak szalona"
arr = s.split(" ")    #podziel wedłog spacji
print(arr)  #dostajemy listę słów
print(arr[0])   #pierwszy element listy

print(s[0:16:2])    #co drugi znak od indeksu 0 do 15 włącznie
print(s[::3])   #cały string co 3 znak
print(s[100]) # dostaniemy Error IndexError: string index out of range

print(s[::-1])                #odwrócenie tekstu - reverse w Pythonie

print("Hello" + "World!")

a = "Hello"
b= "ALX"

print(f"{a} {b} {1+2}")
print("{} {} {}".format(a , b, 1+3))

x = input("Podaj wartość x")  #wartość z inputu zawsze stringiem
print(x, type(x))

x = input("Podaj wartość x")  #wartość z inputu zawsze stringiem
x = int(x)
print(x, type(x))

x = int(input("Podaj wartość x"))  #wartość z inputu zawsze stringiem
#x = int(x)
print(x, type(x))


#print(help(open))

with open("nazwa.txt", 'w') as f:
    print(f.write("Ala "))
    print(f.write("ma "))
    print(f.write("kota."))
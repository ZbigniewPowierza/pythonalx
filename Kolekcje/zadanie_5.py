print("   ", end="")
for i in range(10):
    print(f"{i:3}", end="")
print()
for i in range(10):
    print(i, end="  ")
    for j in range(10):
        print(f"{i*j:3}", end="")
    print()
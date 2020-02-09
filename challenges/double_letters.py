a = "aabcdee"

for i, j in enumerate(a[:-1]):
    print(f"Numer {i}  - znak '{j}'")
    if j == a[i + 1]:
        print(f"Znak nr {i} w {len(a)}-znakowym stringu to '{a}' to litera '{j}' i jest równy znakowi następnemu, czyli znakowi numer {i + 1}")

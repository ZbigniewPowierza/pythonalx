a = "aabcdee"
for i, j in enumerate(a[:-1]):
    print(f"Numer {i}  - znak '{j}'")
    if j == a[i + 1]:
        print(f"Znak nr {i} w {len(a)}-znakowym stringu '{a}' to znak '{j}' i jest równy znakowi następnemu, czyli znakowi numer {i + 1}")
    else:
        print(f"Znak nr {i} w {len(a)}-znakowym stringu '{a}' to znak '{j}' i NIE JEST on równy znakowi następnemu, czyli znakowi numer {i + 1}")

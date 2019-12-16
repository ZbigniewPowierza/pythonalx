"""

$ python czytaj_logi.py dane/input.txt

user-9: 3520 s
user-6: 2950 s

zliczyć dla każdego użytkownika czas przebywania w systemie i posoartować i pokazać print
"""

with open ("dane\logs.txt") as f:
    rezultat = []
    for l in f:
        rezultat = l.split(sep=";")
        print(l.split(";"))
        # print(l)
        #
        # for i in l:
        #     str.split (str="", num=string.count (str))
        #
        #     print(i, end=)

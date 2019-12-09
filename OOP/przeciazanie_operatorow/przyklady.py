# class Soldier:
#     def __init__(self, rank):
#         self.rank = rank
#
# s1 = Soldier('szeregowy')
# s2 = Soldier('major')
#
# s1 > s2 # false, bo s2 ma większy stopień

# wynik dzialania
#   File "C:/Users/kurs/PycharmProjects/pythonalx/OOP/przeciazanie_operatorow/przyklady.py", line 8, in <module>
#     s1 > s2 # false, bo s2 ma większy stopień
# TypeError: '>' not supported between instances of 'Soldier' and 'Soldier'
#
# Process finished with exit code 1

# dlatego trzeba wprowadzic slownik

RANKS = ['szeregowy', 'plutonowy', 'sierżant', 'podpułkownik', 'pułkownik', 'major']

class Soldier:
    def __init__(self, rank):
        self.rank = rank

    def greater(self, other):
        return RANKS.index(self.rank) > RANKS.index(other.rank)

    def __gt__(self, other):
        return self.greater(other)

s1 = Soldier('szeregowy')
s2 = Soldier('major')

# s1 > s2 # false, bo s2 ma większy stopień

print(s1.greater(s2))  # False
print(s2.greater(s1))  # True

print(dir(s1))
print(s1 > s2)
print(s1 < s2)
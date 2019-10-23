# liczby całkowuite integer
print(type(10))
print(int())
print(int("10"))
print(int("10", base = 3))
print(int(2.7))
# liczby zmiennoprzecinkowe - float
print(float())
print(float(1/3))
print(0.1 + 0.1 + 0.1)
print(0.1 + 0.1 + 0.1 == 0.3)
from decimal import Decimal
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1))
print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1"))
print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") == Decimal("0.3"))
# notacja naukowa
print(1e12)
print(1e-12)
# liczby zespolone: complex
print(complex())
print(10+11j)

#  wartości boolowskie: bool True False
print(bool())
print(10+True)
# print(10/False)

# github - założyć konto
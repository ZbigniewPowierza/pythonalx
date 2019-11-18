"""
Napisac funkcje do obliczenia pola i obwodu kola

"""

# import math
# def oblicz_pole_kola(r):
#     return math.pi*r**2
#
# def oblicz_obwod_kola(r):
#     return 2*math.pi*r

from math import pi, sin #jak jest na szaro to znaczy że nie jest używany
def oblicz_pole_kola(r):
    return pi*r**2

def oblicz_obwod_kola(r):
    return 2*pi*r

def oblicz_pole_i_obwod_kola(r):
    return oblicz_pole_kola(r), oblicz_obwod_kola(r)

print(oblicz_pole_i_obwod_kola(4))
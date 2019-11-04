import turtle

print (help (turtle))

# turtle.right(90) # w prawo o zadany kąt
# turtle.forward(50) # do przodu iles tam kroków
#
# turtle.right(90) # w prawo o zadany kąt
# turtle.forward(50) # do przodu iles tam kroków
#
# turtle.right(90) # w prawo o zadany kąt
# turtle.forward(50) # do przodu iles tam kroków
#
# turtle.right(90) # w prawo o zadany kąt
# turtle.forward(50) # do przodu iles tam kroków

# narysuj kwadrat optymalnie
# for i in range(4):
#
#     turtle.right(90) # w prawo o zadany kąt
#     turtle.forward(50) # do przodu iles tam kroków

# narysuj trójkąt
# for i in range(3):
#
#      turtle.right(120) # w prawo o zadany kąt
#      turtle.forward(50) # do przodu iles tam kroków
#
# turtle.done()
"""
napisz funkcje która narysuje dowolny wielokąt foremny
"""


def narysuj_wielokat(n):
    for i in range (n):
        turtle.right (360 / n)  # w prawo o zadany kąt
        turtle.forward (1000 / n)  # do przodu iles tam kroków

    turtle.done ()


narysuj_wielokat(8)

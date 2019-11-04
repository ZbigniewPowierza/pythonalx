import turtle

"""
setheading
0 - east
90 - north
120 - west
270 - south
"""
turtle.speed(0)
def move_up(steps=60):
    turtle.setheading (90)
    turtle.forward (60)

def move_right(steps=60):
    turtle.setheading(0)
    turtle.forward(steps)

def move_left(steps=60):
    turtle.setheading(270)
    turtle.forward(steps)

turtle.setheading(180)
turtle.forward(60)

for i in range(30):
    move_up()
    # turtle.setheading(90)
    # turtle.forward (60)
    move_right()
    # turtle.setheading (0)
    # turtle.forward (1)
    move_right()
    # turtle.setheading (270)
    # turtle.forward (60)
    turtle.setheading (0)
    turtle.forward (1)

turtle.done()
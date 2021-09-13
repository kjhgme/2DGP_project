import turtle
import random

turtle.shape('turtle')
while (True):
    drunken_level = random.randint(1, 10)
    turtle.setheading(random.randint(0,36*drunken_level))
    turtle.forward(random.randint(100,200))
    turtle.stamp()

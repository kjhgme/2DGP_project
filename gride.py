import turtle
count = 5
turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()
distance = 500
while ( count > 0):
        turtle.forward(distance)
        turtle.right(90)
        turtle.forward(distance)
        turtle.right(90)
        turtle.forward(distance)
        turtle.right(90)
        turtle.forward(distance)
        turtle.right(90)
        count -= 1
        distance -=100

turtle.penup()
turtle.goto(300, -300)
turtle.pendown()
turtle.right(180)
count2 = 4
distance2 = 400
while ( count2 > 0):
        turtle.forward(distance2)
        turtle.right(90)
        turtle.forward(distance2)
        turtle.right(90)
        turtle.forward(distance2)
        turtle.right(90)
        turtle.forward(distance2)
        turtle.right(90)
        count2 -= 1
        distance2 -=100

turtle.exitonclick()

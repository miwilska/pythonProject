import turtle
import random
turtle.bgcolor('black')
t = turtle.Turtle()
t.speed(0)
for x in range(50, 300):
    t.color(random.choice(['white','red','blue','green','yellow']))
    t.forward(x)
    t.right(91)

turtle.exitonclick()
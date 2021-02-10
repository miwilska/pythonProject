import turtle
import random
t = turtle.Turtle()
t.pensize(7)


def up():
    t.forward(100)
    t.color(random.choice(['red', 'blue', 'green', 'yellow']))


def left():
    t.left(30)


def right():
    t.right(30)


def bye():
    turtle.bye()


turtle.onkey(up, 'Up')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')
turtle.onkey(bye, 'q')

turtle.listen()
turtle.mainloop()

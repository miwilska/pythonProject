import turtle
import random
window = turtle.Screen()
t = turtle.Turtle()
t.pensize(7)


def click(x, y):
    t.color(random.choice(['red', 'blue', 'yellow', 'green']))
    t.goto(x, y)


def bye():
    turtle.bye()


window.onkey(bye, 'q')
window.onclick(click)

window.listen()
window.mainloop()


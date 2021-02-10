import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.setheading(90)
t.penup()
t.goto(0, -200)
t.pendown()


def gałąź(t, len):
    if len == 0: return
    nt = t.clone()
    nt.pensize(len * 3)
    if len < 3:
        nt.color('green')
        nt.forward(50)
        if random.randint(0, 2) in (1, 2):
            nt.begin_fill()
            if random.randint(0, 10) == 10: nt.color('red')
            nt.circle(20)
            nt.end_fill()
    elif len < 6:
        nt.color('brown')
        nt.forward(50)
    else:
        nt.forward(50)
    nt.left(20)
    gałąź(nt, len - 1)

    nt.right(40)
    gałąź(nt, len - 1)


gałąź(t, 8)
t.penup()
t.goto(-100, -250)
t.write("Analityk.Edu.Pl", font=("Arial", 20, "bold"))
window = turtle.Screen()
window.exitonclick()


import turtle
import time
import random

turtle.bgcolor('black')
turtle.title("Wyścig żółwi")
# meta
meta = turtle.Turtle()
meta.color('white')
meta.penup()
meta.goto(240, 220)
meta.write("Finish Line", font=("Arial", 15, "bold"))
meta.penup()
meta.goto(300, 200)
meta.pendown()
meta.goto(300, -200)
meta.hideturtle()
# zawódnicy
red = turtle.Turtle()
red.shape('turtle')
red.color('red')
red.pensize(7)
red.penup()
red.goto(-200, 100)
red.pendown()
blue = turtle.Turtle()
blue.shape('turtle')
blue.color('blue')
blue.pensize(7)
blue.penup()
blue.goto(-200, -100)
blue.pendown()
# odliczanie
odliczanie = turtle.Turtle()
odliczanie.color('white')
odliczanie.penup()
odliczanie.goto(-200, 200)
odliczanie.hideturtle()
for x in range(3):
    odliczanie.write(3 - x, font=("Arial", 40, 'bold'))
    time.sleep(1)
    odliczanie.clear()
odliczanie.write("Start !!!", font=("Arial", 30, 'bold'))


# czy wygrał
def sprawdz():
    if red.position()[0] >= 300:
        odliczanie.clear()
        odliczanie.color('red')
        odliczanie.write('Wygrał CZERWONY !!', font=("Arial", 20, 'bold'))
        return True
    if blue.position()[0] >= 300:
        odliczanie.clear()
        odliczanie.color('blue')
        odliczanie.write('Wygrał NIEBIESKI !!', font=("Arial", 20, 'bold'))
        return True
    return False


# petla główna
first = random.choice(['red', 'blue'])
while True:
    if first == 'red':
        red.forward(random.randint(0, 70))
        if sprawdz(): break
        blue.forward(random.randint(0, 70))
        if sprawdz(): break
    else:
        blue.forward(random.randint(0, 70))
        if sprawdz(): break
        red.forward(random.randint(0, 70))
        if sprawdz(): break

    time.sleep(0.3)
turtle.exitonclick()
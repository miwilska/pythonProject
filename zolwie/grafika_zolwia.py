import turtle


t = turtle.Turtle()
t.shape('turtle')
t.forward(200)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.home()



t2 = turtle.Turtle()
t2.shape('turtle')
t2.circle(50)
t2.right(45)
t2.circle(60)
t2.right(45)
t2.circle(70)
t2.right(45)
t2.circle(80)


turtle.bgcolor('black')
t3 = turtle.Turtle()
t3.shape('turtle')
t3.color('red')
t3.circle(50)
t3.penup()
t3.goto(-200,0)
t3.pendown()
t3.color('white')
t3.write('Cześć', font=("Arial",30,"bold"))
t3.hideturtle()

t4 = turtle.Turtle()
t4.shape('turtle')

t4.color('red')
t4.begin_fill()
t4.forward(100)
t4.right(90)
t4.forward(100)
t4.right(90)
t4.forward(100)
t4.right(90)
t4.forward(100)
t4.right(90)
t4.end_fill()

turtle.exitonclick()
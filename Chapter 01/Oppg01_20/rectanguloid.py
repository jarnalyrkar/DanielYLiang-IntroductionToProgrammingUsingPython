import turtle

nowpos = (-100, 100)

#Første hjørne
turtle.penup()
turtle.goto(nowpos)
turtle.pendown()

turtle.forward(200)
turtle.penup()
turtle.goto(nowpos)
turtle.pendown()

turtle.right(90)
turtle.forward(100)
turtle.right(-90)
turtle.forward(200)
turtle.right(-90)
turtle.forward(100)

turtle.penup()
turtle.goto(nowpos)
turtle.pendown()

turtle.right(40)
turtle.forward(50)
turtle.right(-40)
turtle.right(90)
turtle.forward(200)
turtle.right(-90)

nowpos = turtle.pos()
turtle.left(140)
turtle.fd(50)
turtle.penup()
turtle.goto(nowpos)
turtle.pendown()
turtle.left(-140)

turtle.left(180)
turtle.forward(100)
turtle.right(90)
turtle.fd(200)
turtle.right(90)
turtle.forward(100)

turtle.penup()
turtle.right(180)
turtle.forward(100)
turtle.pendown()
turtle.right(180)

turtle.left(140)
turtle.forward(50)

turtle.penup()
turtle.goto(nowpos)
turtle.left(-140)
turtle.right(180)
turtle.forward(100)
turtle.right(180)
turtle.pendown()

turtle.left(140)
turtle.forward(50)





turtle.done()
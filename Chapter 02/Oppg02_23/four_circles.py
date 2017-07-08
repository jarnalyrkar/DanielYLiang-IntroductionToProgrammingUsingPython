import turtle

radius = 90#eval(input("Enter a radius: "))

turtle.circle(radius)
turtle.penup()
turtle.setx(turtle.xcor()+(radius*2))
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.sety(turtle.ycor()+(radius*2))
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.setx(turtle.xcor()-(radius)*2)
turtle.pendown()
turtle.circle(radius)
turtle.done()
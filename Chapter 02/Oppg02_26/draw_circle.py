import turtle
import math

#User enter center
center = -50, -50
#User enter radius
radius = 50

#Draw circle
turtle.penup()
turtle.setx(center[0]-radius)
turtle.sety(center[1]-radius)
turtle.pendown()
turtle.circle(radius)

#calculate area of circle
a = math.pi * (radius ** 2)

#write area within circle
turtle.penup()
#turtle.setx(center[0])
turtle.sety(center[1])
turtle.pendown()
turtle.write(str(a))
turtle.done()

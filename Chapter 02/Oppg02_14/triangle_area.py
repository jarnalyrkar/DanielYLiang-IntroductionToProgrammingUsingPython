ss = eval(input("Enter three points for a triangle: ")) #1.5, -3.4, 4.6, 5, 9.5, -3.4
x1 = ss[0]
y1 = ss[1]
x2 = ss[2]
y2 = ss[3]
x3 = ss[4]
y3 = ss[5]

area = 0.5 * (x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1-y2))
if (area < 0):
    area *= -1

print("The area of the triangle is " + str(area))
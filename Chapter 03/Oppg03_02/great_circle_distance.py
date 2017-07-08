#d = radius * arccos(sin(x1) * sin(x2) + cos(x1) * cus(x2) * cos(y1 - y2)))

import math

point1 = eval(input("Enter point 1 (latitude and logitude) in degrees: " )) #39.55, -116.25
point2 = eval(input("Enter point 2 (latitude and logitude) in degrees: " )) #41.5, 87.37
radius = 6371.01

x1 = math.radians(point1[0])
y1 = math.radians(point1[1])
x2 = math.radians(point2[0])
y2 = math.radians(point2[1])

d = radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1-y2))

print(d)
from math import pi
tup = eval(input("Enter the radius and length of a cylinder: "))

area = (tup[0]*tup[0]*pi)

print('Area:', area)
print('Volume', (area*tup[1]))
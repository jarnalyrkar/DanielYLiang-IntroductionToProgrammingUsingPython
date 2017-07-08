import math

n = eval(input("Enter the number of sides: ")) #5
s = eval(input("Enter the side: ")) #6.5

area = (n * (s ** 2)) / (4 * math.tan(math.pi / n))

print(area)
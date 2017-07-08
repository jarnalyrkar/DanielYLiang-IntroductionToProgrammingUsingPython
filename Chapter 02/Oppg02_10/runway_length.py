innskot = eval(input("Enter speed and acceleration: "))
length = (innskot[0]**2) / (2*innskot[1])

print("The minimum runway length for this airplane is " + str(length) + " meters")
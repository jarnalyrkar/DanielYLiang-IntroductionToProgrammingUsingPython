ia = 1000#eval(input("Enter investment amount: ")
air = 4.25 / 100#eval(input("Enter annual interest rate: "))
noy = 1 #eval(input("Enter number of years"))

value = ia * (1 + (air*12)**(noy*12))

print("Accumulated value is", value)
#finalAccountValue
fav = 1000#eval(input("Enter final account value: "))
#monthlyInterestRate
mir = 4.25#eval(input("Enter annual interest rate in percent: "))
#numberOfYears
noy = 5#eval(input("Enter number of years: "))
#initialDepositAmount
ida = fav / ((1 + ((mir/100)/12)) ** (noy * 12))

print("Initial deposit value is " + str(ida))

M = eval(input("Enter the amount of water in kilograms: "))
finalTemperature = eval(input("Enter the initial temperature: "))
initialTemperature = eval(input("Enter the final temperature: "))

Q = M * (finalTemperature - initialTemperature) * 4184
Q = Q*-1

print("The energy needed is " + str(Q))
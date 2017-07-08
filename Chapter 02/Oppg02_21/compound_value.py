innskot = 100 #eval(input("Enter the monthly saving amount: "))
monthly = 1.00417

firstMonth = innskot * monthly
secondMonth = (innskot + firstMonth) * monthly
thirdMonth = (innskot + secondMonth) * monthly
fourthMonth = (innskot + thirdMonth) * monthly
fifthMonth = (innskot + fourthMonth) * monthly
sixthMonth = (innskot + fifthMonth) * monthly

print("After the sixth month, the account value is", sixthMonth)
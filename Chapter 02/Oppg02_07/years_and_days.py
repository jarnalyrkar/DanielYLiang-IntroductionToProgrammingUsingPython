minutes_in_a_day = 1440
days_in_a_year = 365

user_input = 1000000000#eval(input('Enter the number of minutes: '))
#forventet: et år.

#Hvor mange år og dager utgjør x-minutter?
days = user_input / minutes_in_a_day
years = user_input / (minutes_in_a_day*days_in_a_year)

days = days - int(years)*days_in_a_year
print(str(user_input) + " is approximately " + str(int(years)) + " year, and " + str(int(days)) + " days")
'''
Created on 13. feb. 2017

@author: Proghodet
'''
user_input = eval(input('Enter an integer between 11 and 999: '))

if (user_input < 1000 and user_input > 10):
    num1 = int(user_input / 100)
    num2 = int(user_input % 100 / 10)
    num3 = user_input % 10
    print((num1+num2+num3))
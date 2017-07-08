'''
Created on 13. feb. 2017

@author: Proghodet
'''

inputted = eval(input('Enter the subtotal and a gratuity rate:'))

subtotal = inputted[0]
gratuity_rate = inputted[1] / 100
gratuity = gratuity_rate * subtotal

print('The gratuity is', gratuity, 'and the total is', (float("{0:.2f}".format(gratuity+subtotal))))
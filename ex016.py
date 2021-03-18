
# crie um programa que leia  um numero real qualquer pelo teclado e mostre na tela sua porçao inteira

import math

num = float(input('Digite o numero'))
print('O numero {} tem a parte inteira {}'.format(num, math.floor(num)))
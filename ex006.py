# Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

import math

numero: float = float(input('Digite o número:'))
print('O dobro do número digitado é {} \n O triplo é {} \n e sua raiz quadrada é {}'.format(numero*2,numero*3,math.sqrt(numero)))
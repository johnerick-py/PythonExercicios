# faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,cosseno,tangente desse angulo

import math
angulo = float(input('Digite o angulo:'))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O angulo {} tem o SENO de {:.2f}'.format(angulo,seno))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo,cos))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo,tan))
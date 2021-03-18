import math # PARA IMPORTAR UM ESPECIFICO : from math import sqrt

num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('Raiz de {} e igual a {}'.format(num, math.ceil(raiz))) # formatar para baixo usar floor.

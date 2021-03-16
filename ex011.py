# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade
# de tinta necessaria para pinta-la,sabendo que cada litro de tinta pinta uma area de 2 metros quarados.

altura = int(input('Altura da parede:'))
largura = int(input('Largura da aprede:'))  # base
area = altura * largura

print('A aréa de sua parede é {} metros quadrados e irá consumir {}L de tinta.'.format(area, area/2))
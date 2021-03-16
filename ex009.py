# Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.


numero = int(input('Digite o número que deseja a tabuada:'))
cont = 0

while(cont<=10):
    print(cont,'* {}'.format(cont*numero))
    cont = cont + 1
else:
    print('Tabuada de {} calculada com sucesso!'.format(numero))

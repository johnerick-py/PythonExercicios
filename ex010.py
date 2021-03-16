# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# Considere US$1.00 = R$3.27

reais = float(input('Quantos Reais você tem em sua carteira?'))
print('Você podere comprar {:.2f} dólares'.format(reais/3.27))
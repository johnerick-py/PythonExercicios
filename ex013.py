# Faça um algoritmo que leia o salario de um funcionario e mostre seu novvo salario, com 15% de aumento.

salario = float(input('Salário do funcionário:'))
print('O salário do funcionário com 15% de aumento ficou:{:.2f}'.format((salario/100)*15+salario))
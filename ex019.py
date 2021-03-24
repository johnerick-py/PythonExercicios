# um profesor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele,
# lendo o nome deles escrevendo o nome escolhido
import random
n1, n2, n3, n4 = str(input('Nome do aluno:')), str(input('Nome do aluno:')), str(input('Nome do aluno:')), str(input('Nome do aluno:'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O Aluno escolhido foi {}'.format(escolhido))

import random
n1, n2, n3, n4 = str(input('Nome do aluno:')), str(input('Nome do aluno:')), str(input('Nome do aluno:')), str(input('Nome do aluno:'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
escolhido = random.choice(lista)
print('A ordem de apresentação sera: ')
print(lista)

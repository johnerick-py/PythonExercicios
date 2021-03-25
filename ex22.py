
nome = input('Digite seu nome:')
primeironome = nome.split()
print('Em maiuscculo: {}\nEm minusculo {}\nQuantas letras ao todo {}\n'.format(nome.upper(), nome.lower(), len(nome)))
print('Primeiro nome tem {} letras'.format(len(primeironome[0])))
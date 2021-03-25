nome = input('Digite o nome de uma pessoa completo:')
nome = nome.upper()

if 'SILVA' in nome:
    print('O nome da pessoa e {} e contem SILVA'.format(nome))
else:
    print('o nome da pessoa e {} e nao contem SILVA'.format(nome))
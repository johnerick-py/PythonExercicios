
cidade = input('Digite o nome de uma cidade:')
resultado = 'SANTO' in cidade

if 'SANTO' in cidade:
    print('O nome da cidade e {} e contem SANTO'.format(cidade))
else:
    print('o nome da cidade e {} e nao contem SANTO'.format(cidade))
print('*********************************')
print("Bem vindo no jogo de adivinhação!")
print('*********************************')

numero_secreto = 32
chute_str = input('Digite o seu numero: ')
print('Voce digitou {}'.format(chute_str))

chute = int(chute_str)

if numero_secreto == chute:
    print('Voce acertou')
else:
    print('Voce errou o numero era {}'.format(numero_secreto))
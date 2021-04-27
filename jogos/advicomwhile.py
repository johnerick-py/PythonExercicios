print('********************************')
print('Bem vindo ao jogo de advinhação!')
print('********************************')

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada < total_de_tentativas):
    print('Tentativa: {} de {}'.format(rodada, total_de_tentativas))
    chute_str = input('Digite o seu numero:')
    print('Voce digitou {}'.format(chute_str))
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print('Voce acertou!')
    else:
        if(maior):
            print('voce errou! o seu chute foi maior do que o numero secreto.')
        elif(menor):
            print('Voce errou! o seu chute foi menor do que o numero secreto.')

        rodada = rodada + 1
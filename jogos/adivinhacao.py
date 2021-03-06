import random




def jogo_adivinhacao():


    print('*********************************')
    print("Bem vindo no jogo de adivinhação!")
    print('*********************************')

    numero_secreto: int = random.randrange(1, 100)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual nivel de dificuldade?')
    print('(1) fácil (2) Médio (3) Dfícil')

    nivel = int(input(('Define o nivel:')))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativas {} de {}'.format(rodada, total_de_tentativas))

        chute_str = input('Digite o seu numero entre 1 e 100: ')
        print('Voce digitou {}'.format(chute_str))
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print('VOCE DEVE DIGITAR UM NUMERO DE 1 A 100...\n\n')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print('Voce acertou e fez {} pontos!'.format(pontos))
            break
        else:
            if (maior):
                print('voce errou o seu chute foi maior do que o numero secreto.')
            elif (menor):
                print('voce errou, seu chute foi menor do que o numero secreto.')

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('Fim de jogo.')

if(__name__ == "__main__"):
    jogo()



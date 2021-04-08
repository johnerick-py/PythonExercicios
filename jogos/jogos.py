import forca
import adivinhacao

def escolhe_jogo():
    print('*********************************')
    print("*******ESCOLHA O JOGO***********!")
    print('*********************************')

    print('(1) Forca (2) Advinhação')

    jogo = int(input('Qual jogo?'))

    if(jogo == 1):
        print('Jogando Forca')
        forca.jogo_forca()
    elif(jogo == 2):
        print('Jogando advinhação')
        adivinhacao.jogo_adivinhacao()

if(__name__ == "__main__"):
    escolhe_jogo()
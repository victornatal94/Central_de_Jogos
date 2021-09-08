from random import randint
from time import sleep

def jogar():

    lista = ('Pedra', 'Papel', 'Tesoura')
    pc = randint(0, 2)
    print ('Suas opções\n[0] Pedra\n[1] Papel\n[2] Tesoura')
    jogada = int(input('Qual sua jogada? '))
    if jogada < 0 or jogada > 2:
        print('Jogada inválida!')
    else:
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!!')
        print('=-'*10)
        print('Você escolheu {}!'.format(lista[jogada]))
        print('O computador escolheu {}!'.format(lista[pc]))
        print('=-'*10)
        if pc == 0:
            if jogada == 0:
                print('EMPATE!!!!')
            elif jogada == 1:
                print('Você ganhou!!!')
            elif jogada == 2:
                print('Você perdeu!!!')
            else:
                print('Jogada inválida!')
        elif pc == 1:
            if jogada == 0:
                print('Você perdeu!!!')
            elif jogada == 1:
                print('EMPATE!!!!')
            elif jogada == 2:
                print('Você ganhou!!!')
            else:
                print('Jogada inválida!')
        elif pc == 2:
            if jogada == 0:
                print('Você ganhou!!!')
            elif jogada == 1:
                print('Voce perdeu!!!!')
            elif jogada == 2:
                print('EMPATEEE!!!')
            else:
                print('Jogada inválida!')

if __name__ == '__main__':
    jogar()
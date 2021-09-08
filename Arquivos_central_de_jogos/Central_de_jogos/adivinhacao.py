from random import randint

def jogar():

    print('*'*25)
    print('Bem vindo ao jogo de Adivinhação!')
    print('*'*25)

    numero_secreto = randint(1, 11)
    total_tentativas = 3

    for rodada in range(1, total_tentativas + 1):
        print('Tentativa {} '.format(rodada),)
        chute = int(input('Digite seu número: '))
        print(f'Voce digitou {chute}')

        if chute < 1 or chute > 10:
            print('Entre 1 e 10!')
            continue

        if chute == numero_secreto:
            print('Voce acertou!')
            break
        else:
            if chute > numero_secreto:
                print('Errou! O número secreto é menor!')
            elif chute < numero_secreto:
                print('Errou! O numero secreto é maior')

    print('O numero secreto era ', numero_secreto)

if __name__ == '__main__':
    jogar()
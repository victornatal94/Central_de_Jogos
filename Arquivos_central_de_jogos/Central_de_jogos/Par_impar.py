from random import randint

def jogar():

    v=0
    while True:
        jogador = int(input('Sua mão é de: '))
        pc= randint(0, 10)
        total = jogador + pc
        pi = ' '
        while pi not in 'pi':
            pi = str(input('Você quer par ou impar?[P / I]')).strip().lower()[0]
        print(f'Voce jogou {jogador} e o computador jogou {pc}. Total de {total}')
        print('DEU PAR' if total % 2 ==0 else 'DEU IMPAR')
        if pi == 'p':
            if total % 2 == 0:
                print('Venceu!!!')
                v += 1
            else:
                print('Perdeu!!')
                break
        elif pi == 'i':
            if total % 2 == 0:
                print('Perdeu!!')
                break
            else:
                print('Venceu!!!')
                v += 1
        print('Vamos jogar de novo!!!!')
    if v == 0:
        print('Não me venceu, bobo!')
    elif v == 1:
        print('Voce ganhou só 1 vez')
    else:
        print(f'Voce ganhou {v} vezes')


if __name__ == '__main__':
    jogar()
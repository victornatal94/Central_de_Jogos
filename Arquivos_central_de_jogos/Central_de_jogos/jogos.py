import adivinhacao
import forca
import Par_impar
import Jokenpo
import pong

print('*'*20)
print('Bem vindxs a Central de Jogos')
print('Escolha seu jogo!')
print('*'*20)

print('(1) Jogo da Forca (2) Adivinhação (3) Par ou Ímpar (4) Jo Ken Po (5) Pong')
jogo = int(input('Qual jogo?'))

if jogo == 1:
    print('Jogando forca')
    forca.jogar()
elif jogo == 2:
    print('Jogando Adivinhação')
    adivinhacao.jogar()
elif jogo == 3:
    print('Jogando Par ou Ímpar')
    Par_impar.jogar()
elif jogo == 4:
    print('Jogando Jo Ken Po!')
    Jokenpo.jogar()
elif jogo == 5:
    print('Jogando Pong!')
    pong.jogar()

from random import randrange

def imprime_mensagem_abertura():
    print('*' * 25)
    print('Bem vindo ao jogo de Forca!')
    print('*' * 25)

def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        palavras.append(linha)

    arquivo.close()

    numero = randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower().strip()
    return palavra_secreta

def inicializa_palavras_acertadas(palavra):
    return ['_' for letra in palavra]

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    imprime_mensagem_abertura()
   
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_palavras_acertadas(palavra_secreta)
    enforcado = False
    acertou = False
    erros = 0

    while not enforcado and not acertou:

        print(letras_acertadas)
        chute = input('Escolha uma letra: ').lower().strip()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            print('Não tem a letra {}'.format(chute))
            erros += 1
            desenha_forca(erros)
        enforcado = erros == 7
        acertou = '_' not in letras_acertadas



    print('Fim do jogo!')
    if enforcado:
        imprime_mensagem_perdedor(palavra_secreta)
    elif acertou:
        imprime_mensagem_vencedor()



if __name__ == '__main__':
    jogar()
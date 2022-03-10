import random


def jogo():
    mensagem_de_apresentação()
    palavra_chave = carregar_palavra_secreta()
    acertos = ["_"]*len(palavra_chave)      #Ou acertos = ["_" for letras in palavra_chave]
    print(acertos)

    enforcado = False
    acertou = False
    tentativas = 0

    while(not enforcado and not acertou):
        chute = input("Qual a letra? ").strip().upper()      #strip()--> Remove os espaços
        if(chute in palavra_chave):
            adiciona_letra_certa(palavra_chave, chute, acertos)
        else:
            tentativas += 1
            desenha_forca(tentativas)
            if (tentativas == 7):
                enforcado = True                             # Ou enforcado = tentativas == 6
                mensagem_perdedor(palavra_chave)
            else:
                print(f"Você errou, restam {7 - tentativas} tentativas")
                print(acertos)
        if(acertos.count("_") == 0):                         #acertos.count("_")--> Conta quantos "_" existem em acertos
            acertou = True                                   #Ou acertou = "_" not in acertos
            mensagem_vencedor()

def mensagem_de_apresentação():
    print("+++++++++++++++++++++")
    print("++++Jogo da Forca++++")
    print("+++++++++++++++++++++")

def carregar_palavra_secreta(nome_arquivo="palavras"):       #Se nenhum nome de arquivo for passado, o arquivo padrão é "palavras"
    arquivo = open(nome_arquivo, "r")
    lista_palavras = []
    for linha in arquivo:
        linha = linha.strip()
        lista_palavras.append(linha)
    arquivo.close()
    n = random.randrange(0, len(lista_palavras))
    palavra_chave = lista_palavras[n].upper()
    return palavra_chave

def adiciona_letra_certa(palavra_chave, chute, acertos):
    index = 0
    for letra in palavra_chave:
        if (chute == letra):  # lower()--> Transfrma para letras minúsculas
            acertos[index] = letra
        index += 1
    print(acertos)

def mensagem_perdedor(palavra_chave):
    print(f"Você Perdeu! a palavra era {palavra_chave}")
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

def mensagem_vencedor():
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

def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogo()

##List Comprehension:
# inteiros = [1,3,4,5,7,8,9]
# pares = [x for x in inteiros if x % 2 == 0] --> adiciona o número x na lista 'pares' se x for par
#
##Escrita em Arquivos:
# arquivo = open("palavras", "w") --> A função open recebe dois valores, o arquivo a ser aberto, e w para escrever; r para ler; a para adicionar
# arquivo.write("Banana") --> Depois de abrir o arquivo, write para escrever nele
# arquivo.close() --> fechar arquivo
# arquivo = open("palavras.txt", "r")
# linha = arquivo.readline()
# print(linha)
def jogo():
    import random as r
    print("+++++++++++++++++++++")
    print("+Jogo de Adivinhação+")
    print("+++++++++++++++++++++")
    n = r.randrange(1, 101)                                           #r.randrange(1, 101)--> inteiro aleatório de 1 a 100
    rodadas = int(input("Quantas rodadas? "))                         #r.ramdo() -> número aleatório entre 0.0 e 1.0
    c = 1
    print("Você tem", rodadas, "tentativas")
    while (c <= rodadas):
        print(f"Tentativa {c} de {rodadas}")
        chute = int(input("Tente adivinhar o número entre 0 e 100: "))
        print(f"Você chutou o número {chute}")

        if (chute < 1 or chute > 100):
            print("Inválido! Chute um valor entre 0 e 100\n")
            continue                                                   #Volta para o inicio do laço

        acertou = chute == n
        maior = chute > n
        menor = chute < n
        c += 1

        if acertou:
            print("Você acertou\n")
            break
        elif maior:
            print("Você errou, chute um número menor\n")
        else:
            print("Você errou, chute um número maior\n")

    print(f"O número secreto é {n}")
    print("## Fim do Jogo ##")

if(__name__ == "__main__"):                                   #Se o arquivo for o principal, a função irá rodar
    jogo()
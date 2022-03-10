import adivinhação_de_número
import forca

print("++++++++++++++++++++")
print("Jogo de Adivinhação")
print("++++++++++++++++++++")

print("(1) Jogo da Adivinação  (2) Jogo da Forca")
jogo = int(input("Escolha um Jogo: "))

if jogo == 1:
    adivinhação_de_número.jogo()
elif jogo == 2:
    forca.jogo()
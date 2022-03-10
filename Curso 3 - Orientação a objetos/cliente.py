
class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property                             #Permite chamar o nome sem colocar parenteses, como se fosse um get
    def nome(self):
        print("Pegando o nome...")
        return self.__nome.title()

    @nome.setter                          #Adiciona nome sem utilizar o parenteses, e sim um = (Mesmo nome do construtor)
    def nome(self, nome):
        print("Adicionando nome...")
        self.__nome = nome
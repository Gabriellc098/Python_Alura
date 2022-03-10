
class Conta:
    def __init__(self, numero, nome, saldo, limite):                #Função construtora
        print("Criando...")
        self.__numero = numero                                      #Atributos da classe
        self.__nome = nome                                          #__ atributo privado
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):                                              #Primeiro método
        print(f"{self.__nome} tem um saldo de {self.__saldo}")

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):                          #Método privado
        valor_disponivel_para_sacar = self.__saldo + self.__limite
        if(valor_a_sacar <= valor_disponivel_para_sacar):
            return True

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou do limite")

    def transfere(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod                        #Métodos que não precisam do objeto(self), não precisam de referência--> Métodos da classe
    def codigo_banco():
        return "001"

conta = Conta(24, "Gabriel", 500, 1000)
conta.extrato()
conta.depositar(300)
conta.extrato()
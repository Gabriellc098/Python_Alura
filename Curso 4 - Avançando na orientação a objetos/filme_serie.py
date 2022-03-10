
class Audiovisual:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):                                              #Função interna para exibição de textos (o print já identifica essa função)
        return f"{self._nome} - {self.ano} - {self._likes} likes"

class Filme(Audiovisual):                                           #Subclasse com herança da classe Audiovisual
    def __init__(self, nome, ano, duração):
        super().__init__(nome, ano)                                 #Chama os atributos da classe mãe 'Audiovisual'
        self.duração = duração

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duração}min - {self._likes} likes"

class Serie(Audiovisual):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} likes"

class Playlist:
    def __init__(self, nome, lista):
        self.nome = nome
        self._lista = lista

    def __getitem__(self, item):                   #Faz com que a Playlist possa ser iterável (utilizar for in, len)
        return self._lista[item]

    def __len__(self):                             #Ganha a característica de ser sized
        return len(self._lista)

    @property
    def listagem(self):
        return self._lista

    @property
    def tamanho(self):
        return len(self._lista)

#class Playlist(list):                              #list--> classe builtin, transforma a classe Playlist em uma lista
#    def __init__(self, nome, lista):
#        self.nome = nome
#        super().__init__(lista)                    #Utiliza as propriedades da classe mãe (list), no caso inicializa uma lista

filme = Filme("eternos", 2021, 150)
filme2 = Filme("parasita", 2020, 130)
serie = Serie("stranger things", 2018, 3)
serie2 = Serie("Chucky", 2021, 1)
filme.dar_likes()
filme.dar_likes()
filme.dar_likes()
filme2.dar_likes()
filme2.dar_likes()
filme2.dar_likes()
filme2.dar_likes()
serie.dar_likes()
serie.dar_likes()
serie.dar_likes()
serie2.dar_likes()
#print(f"O filme {filme.nome}, lançado em {filme.ano}, tem {filme.likes} likes")
#print(f"A série {serie.nome}, de {serie.temporadas} temporadas, tem {serie.likes} likes\n")

filme_e_serie = [filme, serie, filme2, serie2]
maratona = Playlist("Maratona de filmes e séries", filme_e_serie)
print(filme2)
print(f"Tamanho da playlist maratona: {len(maratona)}")
for programa in maratona:                                               #maratona já é uma lista, por causa da herança da classe list
    print(programa)


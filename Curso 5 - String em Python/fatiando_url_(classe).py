import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitaniza_url(url)
        self.valida_url()

    def sanitaniza_url(self, url):
        if type(url) == str:                           #Verifica se o url é uma string. EX: None não é string é uma classe específica do python
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:                               #Verifica se a url esta vazia
            raise ValueError("A URL está vazia")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")  # () indica que a string precisa ser igual a informação contida no parenteses. [] indica que a string pode conter qualquer caracter contido nos colchetes
        match = padrao_url.match(self.url)  # match é um atributo do método patern, retornado pelo compile. o match verifica se determinada string(url) se exatamente o padrão determinado
        if match:
            print("URL é válida")
        else:
            raise ValueError("URL inválida")

    def get_url_base(self):
        index_interrogação = self.url.find("?")
        url_base = self.url[:index_interrogação]
        return url_base

    def get_url_parametros(self):
        index_interrogação = self.url.find("?")
        url_parametros = self.url[index_interrogação + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(
            parametro_busca) + 1  # inicio do parametro + tamanho do parametro + o sinal de "="
        indice_e_comercial = self.get_url_parametros().find("&",
                                                  indice_valor)  # find("valor a ser achado", onde começa a procurar)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetro: " + self.get_url_parametros() + "\n" + "Base: " + self.get_url_base()

    def __eq__(self, other):                        #__eq__ método especial de igualdade. other --> objeto a diretira da comparação. x1.__eq__(other).
        return self.url == other.url

extrator_url = ExtratorURL("bytebank.com/cambio?moedaDestino=dolar&quantidade=1000&moedaOrigem=real")
print("Tamanho da URL:", len(extrator_url))
valor_quantidade = extrator_url.get_valor_parametro("moedaOrigem")
print(valor_quantidade)
print(extrator_url)
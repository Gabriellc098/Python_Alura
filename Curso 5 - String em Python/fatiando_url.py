url = "bytebank.com/cambio?moedaDestino=dolar&quantidade=1000&moedaOrigem=real"

url = url.replace(" ","")                               #Poderia usar o strip no lugar
if url == "":                                           #Validar a URL
    raise ValueError("A URL está vazia")

# Separa base e parâmentros
index_interrogação = url.find("?")
url_base = url[:index_interrogação]
url_paramentros = url[index_interrogação+1:]
print(url_paramentros)

# Busca valor de um parâmentro
parametro_busca = "quantidade"
indice_parametro = url_paramentros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1          #inicio do parametro + tamanho do parametro + o sinal de "="
indice_e_comercial = url_paramentros.find("&", indice_valor)        #find("valor a ser achado", onde começa a procurar)
if indice_e_comercial == -1:
    valor = url_paramentros[indice_valor:]
else:
    valor = url_paramentros[indice_valor:indice_e_comercial]
print(valor)

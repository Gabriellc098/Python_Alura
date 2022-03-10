# Expressões Regulares - Regular Expression - RegEx

import re    # regular expression
# padrão de cep: 5 dígitos + hífen(opcional) + 3 dígitos
endereço = "Rua Antônio Camilo Dias 81, partamento 702, Madalena, 50720-585"

#padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")    #O compile cria um padrão, retorna o objeto patern. a '?' indica que o hífen pode ou não estar no padrão
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}") #dentro das chaves estão os quantificadores, indicando quantas vezes os númeoros precisam aparecer. [0-9] indica que pode ser um número de 0 a 9. {0,1} quantificador com limites, nesse caso o hífen pode aparecer de 0 a 1 vez
busca = padrao.search(endereço)         #o search busca o padrão dentro da string (nesse caso o endereço). o search é um método do próprio objeto patern que é retornado do compile. Match se for encontrado, none se não for
if busca:
    cep = busca.group()  #a partir do match, é salvado a string encontrada no padrão
    print(cep)
else:
    print("CEP não encontrado")

# Padrão de uma URL
# https://www.bytebank.com.br/cambio

url = "https://www.bytebank.com.br/cambio"
padrão_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")     # () indica que a string precisa ser igual a informação contida no parenteses. [] indica que a string pode conter qualquer caracter contido nos colchetes
match = padrão_url.match(url)            # match é um atributo do método patern, retornado pelo compile. o match verifica se determinada string(url) bate exatamente com o padrão determinado

if match:
    print("URL é válida")
else:
    raise ValueError("URL inválida")
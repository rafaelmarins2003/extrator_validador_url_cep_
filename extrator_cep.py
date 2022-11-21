endereço = ""

import re  #RegEx

#CEP - possui 5 numeros + hifen (opcional) + 3 digitos

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereço)  # Match
if busca:
    cep = busca.group()
    print(cep)
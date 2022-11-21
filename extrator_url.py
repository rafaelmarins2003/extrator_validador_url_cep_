import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)

        if not match:
            raise ValueError("A URL não é valida.")

    def get_url_base(self):
        interrogacao = self.url.find('?')
        url_base = self.url[:interrogacao]
        return url_base

    def get_url_parametros(self):
        interrogacao = self.url.find('?')
        url_parametros = self.url[interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        paramentro_busca = "quantidade"
        indice_parametro = self.get_url_parametros().find(paramentro_busca)
        indice_valor = indice_parametro + len(paramentro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
print("O tamanho da URL é", len(extrator_url))

valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
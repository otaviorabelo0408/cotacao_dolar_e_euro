# Arquivo destinado à criação dos objetos utilizados nesse projeto:

class Dolar(object):

    def __init__(self, cotacao):
        self.__cotacao = cotacao

    @property
    def cotacao(self):
        return f"R${self.__cotacao:.4f}"

    @cotacao.setter
    def cotacao(self, novo):
        self.__cotacao = novo


class Euro(object):

    def __init__(self, cotacao):
        self.__cotacao = cotacao

    @property
    def cotacao(self):
        return f"R${self.__cotacao:.4f}"

    @cotacao.setter
    def cotacao(self, novo):
        self.__cotacao = novo

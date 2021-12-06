# Arquivo destinado aos testes realizados sobre esse projeto:

from unittest import (TestCase, main)
from utilidades.objetos import *
from requests import get


class TesteClasse(TestCase):
    def teste_classe(self):
        self.assertIsInstance(Dolar(
            float(get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()["USDBRL"]["bid"])),
            Dolar)
        self.assertIsInstance(Euro(
            float(get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()["EURBRL"]["bid"])),
            Euro)


if __name__ == '__main__':
    main()

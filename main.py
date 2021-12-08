# Arquivo com a função principal desse projeto:

from utilidades.funcoes import (apresenta_cotacao, sleep, system)

if __name__ == '__main__':
    print("Sistema inicializando. Aguarde.")
    sleep(3)
    system("clear")
    apresenta_cotacao()

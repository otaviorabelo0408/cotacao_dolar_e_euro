# Arquivo com a função principal desse projeto:

from utilidades.funcoes import (apresenta_cotacao, sleep, limpa_tela)

if __name__ == '__main__':
    print("Sistema inicializando. Aguarde.")
    sleep(3)
    limpa_tela()
    apresenta_cotacao()

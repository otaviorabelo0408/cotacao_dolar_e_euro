# Arquivo com a função principal desse projeto:

from utilidades.funcoes import atualiza, dolar, euro, sleep, system, d, e

if __name__ == '__main__':
    print("Sistema inicializando. Aguarde.")
    sleep(3)
    system("clear")
    atualiza(dolar, euro, d, e)

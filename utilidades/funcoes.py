# Arquivo destinado às funções utilizadas nesse projeto:

from utilidades.objetos import *
from requests import get
from time import sleep
from os import (system, name)
from csv import writer
from datetime import (date, datetime)
from statistics import mean
from matplotlib.pyplot import (plot, ylabel, xlabel, title, show, legend)

# Inicializando listas:

lista_dolar = list()
lista_euro = list()
lista_tempo = list()
dolar_plotagem = list()
euro_plotagem = list()


# Função que apresenta a cotação atual do Dólar e do Euro:

def apresenta_cotacao():
    """Função que imprime as cotações do
    Dólar e do Euro e atualiza esses valores
    a cada 30 segundos."""
    if date.today().isoweekday() == 6 or date.today().isoweekday() == 7:
        print("Durante o fim de semana o mercado está fechado!")
        print("Encerrando programa. Aguarde 5 segundos.")
        sleep(5)
        exit(0)
    else:
        if int(datetime.now().strftime("%H")) >= 18:
            print("O mercado funciona apenas até às 18h. Volte no próximo dia útil!")
            print("Encerrando programa. Aguarde 5 segundos.")
            sleep(5)
            exit(0)
        elif int(datetime.now().strftime("%H")) < 10:
            print("O mercado funciona apenas a partir das 10h.")
            print("Mantenha o programa aberto até as 10h, e então ele iniciará a cotação automaticamente.")
            while int(datetime.now().strftime("%H")) < 10:
                pass
        d = float(get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL").json()["USDBRL"]["bid"])
        e = float(get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL").json()["EURBRL"]["bid"])
        dolar = Dolar(d)
        euro = Euro(e)
        limpa_tela()
        print(f"Cotação do Dólar: {dolar.cotacao}")
        print(f"Cotação do Euro: {euro.cotacao}")
        lista_dolar.append(d)
        lista_euro.append(e)
        lista_tempo.append(datetime.now().strftime("%H:%M"))
        dolar_plotagem.append(d)
        euro_plotagem.append(e)
        while datetime.now().strftime("%H:%M") != "18:00":
            print("\nAguarde pela próxima atualização.")
            for i in range(30, 0, -1):
                sleep(1)
            limpa_tela()
            d = float(get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL").json()["USDBRL"]["bid"])
            e = float(get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL").json()["EURBRL"]["bid"])
            dolar.cotacao = d
            euro.cotacao = e
            lista_dolar.append(d)
            lista_euro.append(e)
            if int(datetime.now().strftime("%M")) == 0 or int(datetime.now().strftime("%M")) == 30:
                if datetime.now().strftime("%H:%M") != lista_tempo[len(lista_tempo) - 1]:
                    lista_tempo.append(datetime.now().strftime("%H:%M"))
                    dolar_plotagem.append(d)
                    euro_plotagem.append(e)
            print(f"Cotação do Dólar: {dolar.cotacao}")
            print(f"Cotação do Euro: {euro.cotacao}")
        menu()


# Função destinada ao arquivamento dos dados catalogados:

def arquiva_dados():
    """Função que ariquiva os dados catalogados
    em um arquivo do tipo .csv."""
    with open("cotacoes.csv", 'a') as arq:
        arq = writer(arq)
        arq.writerow([date.today().strftime("%d/%m/%y"), "Dólar", f"R${mean(lista_dolar):.4f}"])
        arq.writerow([date.today().strftime("%d/%m/%y"), "Euro", f"R${mean(lista_euro):.4f}"])


# Função destinada à plotagem dos gráficos:

def plotagem(moeda, lista, cor):
    """Função que plota um gráfico de acordo com a
    solicitação do usuário."""
    plot(lista_tempo, lista, color=cor, label=moeda)
    xlabel("Horários das cotações")
    ylabel("Valores medidos")
    legend(title='Moeda:', loc='best')
    title(f"Variação da cotação do {moeda} com o tempo.")
    show()


# Função destinada ao menu final do programa:

def menu():
    """Função que executa o menu final do programa."""
    limpa_tela()
    print("Bem vindo ao menu final do programa:\n")
    while True:
        try:
            print("Digite sua opção e tecle ENTER:")
            print("\nOpção 1: atualiza o arquivo cotacoes.csv com a data e a média da cotação de cada moeda"
                  " nessa data e encerra o programa;")
            print("Opção 2: exibe um gráfico com a variação da cotação das moedas ao longo do"
                  " período medido e encerra o programa;")
            print("Opção 3: realiza as duas ações acima e encerra o programa;")
            print("Opção 4: apenas encerra o programa.")
            opc = int(input("Escolha sua opção: "))
            limpa_tela()
            if opc == 1:
                arquiva_dados()
                print("Dados arquivados com sucesso. Aguarde 5 segundos pelo encerramento do programa.")
                sleep(5)
                exit(0)
            elif opc == 2:
                plotagem("Dólar", dolar_plotagem, 'red')
                plotagem("Euro", euro_plotagem, 'green')
                print("Aguarde 5 segundos pelo encerramento do programa.")
                sleep(5)
                exit(0)
            elif opc == 3:
                arquiva_dados()
                plotagem("Dólar", dolar_plotagem, 'red')
                plotagem("Euro", euro_plotagem, 'green')
                print("Dados arquivados com sucesso. Aguarde 5 segundos pelo encerramento do programa.")
                sleep(5)
                exit(0)
            elif opc == 4:
                print("Obrigado por utilizar o programa. Aguarde 5 segundos pelo seu encerramento.")
                sleep(5)
                exit(0)
            else:
                print("Opção invállida. Tente novamente!")
        except ValueError:
            limpa_tela()
            print("Opção inválida. Tente novamente!")


# Função destinada à limpar a tela de acordo com o sistema operacional:

def limpa_tela():
    """Função que limpa a tela do terminal
    de acordo com o sistema operacional
    vigente na máquina."""
    if name == 'nt':
        system("cls")
    else:
        system("clear")

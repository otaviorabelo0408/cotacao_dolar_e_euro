# Arquivo destinado às funções utilizadas nesse projeto:

from utilidades.objetos import *
from requests import get
from time import sleep
from os import system
from csv import writer
from datetime import (date, datetime)
from statistics import mean
from matplotlib.pyplot import (plot, ylabel, xlabel, title, show, legend)

# Iniciando cotação:

lista_dolar = list()
lista_euro = list()
lista_tempo = list()
dolar_plotagem = list()
euro_plotagem = list()


# Atualizando cotação:

def atualiza():
    """Função que imprime a primeira cotação
    catalogada e atualiza os valores das
    cotações."""
    if date.today().isoweekday() == 6 or date.today().isoweekday() == 7:
        print("Durante o fim de semana o mercado está fechado!")
        print("Encerrando programa. Aguarde 5 segundos.")
        sleep(5)
        exit(0)
    else:
        if int(datetime.now().strftime("%H")) < 10:
            print("O mercado funciona apenas a partir das 10:00. Volte mais tarde!")
            print("Encerrando programa. Aguarde 5 segundos.")
            sleep(5)
            exit(0)
        elif int(datetime.now().strftime("%H")) >= 18:
            print("O mercado funciona apenas até às 18:00. Volte no próximo dia útil!")
            print("Encerrando programa. Aguarde 5 segundos.")
            sleep(5)
            exit(0)
        else:
            d = float(get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL").json()["USDBRL"]["bid"])
            e = float(get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL").json()["EURBRL"]["bid"])
            dolar = Dolar(d)
            euro = Euro(e)
            print(f"Cotação do dólar: {dolar.cotacao}")
            print(f"Cotação do euro: {euro.cotacao}")
            lista_dolar.append(d)
            lista_euro.append(e)
            lista_tempo.append(datetime.now().strftime("%H:%M"))
            dolar_plotagem.append(d)
            euro_plotagem.append(e)
            while datetime.now().strftime("%H:%M") != "18:00":
                print("\nAguarde pela próxima atualização.")
                for i in range(30, 0, -1):
                    sleep(1)
                system("clear")
                d_n = float(get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL").json()["USDBRL"]["bid"])
                e_n = float(get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL").json()["EURBRL"]["bid"])
                dolar.cotacao = d_n
                euro.cotacao = e_n
                lista_dolar.append(d_n)
                lista_euro.append(e_n)
                if int(datetime.now().strftime("%M")) == 0 or int(datetime.now().strftime("%M")) == 30:
                    if datetime.now().strftime("%H:%M") != lista_tempo[len(lista_tempo) - 1]:
                        lista_tempo.append(datetime.now().strftime("%H:%M"))
                        dolar_plotagem.append(d_n)
                        euro_plotagem.append(e_n)
                print(f"Cotação do dólar: {dolar.cotacao}")
                print(f"Cotação do euro: {euro.cotacao}")
            menu()


def arquiva_dados():
    """Função que ariquiva os dados catalogados
    em um arquivo do tipo .csv."""
    with open("/home/otavio/PycharmProjects/cotacao/cotacoes.csv", 'a') as arq:
        arq = writer(arq)
        arq.writerow([date.today().strftime("%d/%m/%y"), "Dólar", float(f"{mean(lista_dolar):.4f}")])
        arq.writerow([date.today().strftime("%d/%m/%y"), "Euro", float(f"{mean(lista_euro):.4f}")])


def plotagem(moeda, lista, cor):
    """Função que plota um gráfico de acordo com a
    solicitação do usuário."""
    plot(lista_tempo, lista, color=cor, label=moeda)
    xlabel("Horário da cotação")
    ylabel("Cotação")
    legend(title='Legenda:', loc='best')
    title(f"Variação da cotação do {moeda} com o tempo.")
    show()


def menu():
    """Função que executa o menu final do programa."""
    system("clear")
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
            system("clear")
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
            system("clear")
            print("Opção inválida. Tente novamente!")

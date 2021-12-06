# Arquivo destinado às funções utilizadas nesse projeto:

from utilidades.objetos import *
from requests import get
from time import sleep
from os import system
from csv import writer
from datetime import (date, datetime)
from statistics import mean
from matplotlib.pyplot import (plot, ylabel, xlabel, title, show, legend, axis)

# Iniciando cotação:

d = float(get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL").json()["USDBRL"]["bid"])
e = float(get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL").json()["EURBRL"]["bid"])
dolar = Dolar(d)
euro = Euro(e)
lista_dolar = list()
lista_euro = list()
lista_tempo = list()
dolar_plotagem = list()
euro_plotagem = list()
lista_tempo.append(datetime.now().strftime("%H:%M:%S"))


# Atualizando cotação:

def atualiza(dolar_obj, euro_obj, d_1, e_1):
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
        elif int(datetime.now().strftime("%H")) > 17 or (
                int(datetime.now().strftime("%H")) == 17 and int(datetime.now().strftime("%M")) != 0
        ):
            print("O mercado funciona apenas até às 17:00. Volte no próximo dia útil!")
            print("Encerrando programa. Aguarde 5 segundos.")
            sleep(5)
            exit(0)
        else:
            print(f"Cotação do dólar: {dolar_obj.cotacao}")
            print(f"Cotação do euro: {euro_obj.cotacao}")
            lista_dolar.append(d_1)
            lista_euro.append(e_1)
            lista_tempo.append(datetime.now().strftime("%H:%M"))
            dolar_plotagem.append(d_1)
            euro_plotagem.append(e_1)
            while datetime.now().strftime("%H:%M") != "17:00":
                print("\nAguarde pela próxima atualização.")
                for i in range(30, 0, -1):
                    sleep(1)
                system("clear")
                d_i = float(get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL").json()["USDBRL"]["bid"])
                e_i = float(get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL").json()["EURBRL"]["bid"])
                dolar_obj.cotacao = d_i
                euro_obj.cotacao = e_i
                lista_dolar.append(d_i)
                lista_euro.append(e_i)
                if int(datetime.now().strftime("%M")) == 0 or int(datetime.now().strftime("%M")) == 30:
                    if datetime.now().strftime("%H:%M") != lista_tempo[0]:
                        lista_tempo.append(datetime.now().strftime("%H:%M"))
                        dolar_plotagem.append(d_i)
                        euro_plotagem.append(e_i)
                print(f"Cotação do dólar: {dolar_obj.cotacao}")
                print(f"Cotação do euro: {euro_obj.cotacao}")
            menu()


def arquiva_dados():
    """Função que ariquiva os dados catalogados
    em um arquivo do tipo .csv."""
    with open("/home/otavio/PycharmProjects/cotacao/cotacoes.csv", 'a') as arq:
        arq = writer(arq)
        arq.writerow([date.today(), "Dólar", float(f"{mean(lista_dolar):.4f}")])
        arq.writerow([date.today(), "Euro", float(f"{mean(lista_dolar):.4f}")])


def plotagem(legenda, dados_1, dados_2):
    """Função que plota um gráfico de acordo com a
    solicitação do usuário."""
    plot(legenda, dados_1, color='red')
    plot(legenda, dados_2, color='green')
    xlabel("Horário da cotação")
    ylabel("Valor alcançado")
    title(f"Variação da cotação do dólar e do euro com o tempo.")
    legend(title='Legenda:', loc='best')
    axis('equal')
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
                plotagem(lista_tempo, dolar_plotagem, euro_plotagem)
                print("Aguarde 5 segundos pelo encerramento do programa.")
                sleep(5)
                exit(0)
            elif opc == 3:
                arquiva_dados()
                plotagem(lista_tempo, dolar_plotagem, euro_plotagem)
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

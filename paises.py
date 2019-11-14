import sys
import json

import requests

URL_ALL = "https://restcountries.eu/rest/v2/all"
URL_NAME = "https://restcountries.eu/rest/v2/name"


def requisiscao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print("Erro ao fazer requisição em:", url)


def parsing(texto):
    try:
        return json.loads(texto)
    except:
        print("Errou ao fazer o parsing")


def contagem_de_paises():
    resposta = requisiscao(URL_ALL)
    if resposta:
        lista_de_paises = parsing(resposta)
        return len(lista_de_paises)


def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais['name'])


def mostrar_populacao(nome_do_pais):
    resposta = requisiscao("{}/{}".format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        for pais in lista_de_paises:
            print("População {}: {}".format(pais['name'],pais['population']))
    else:
        print("País não encontrado")


def mostrar_moedas(nome_do_pais):
    resposta = requisiscao("{}/{}".format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        for pais in lista_de_paises:
            print("Moedas {}".format(pais['name']))
            moedas = pais['currencies']
            for moeda in moedas:
                print(" {} - {}".format(moeda['name'], moeda['code']))
    else:
        print("País não encontrado")


def ler_nome_do_pais():
    try:
        nome_do_pais = sys.argv[2]
        return nome_do_pais
    except:
        print("É preciso passar o nome do país")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Sistema de países")
        print("Uso: python paises.py <ação> <nome do país>")
        print("Ações disponíveis: contagem, moeda, população")
    else:
        argumento1 = sys.argv[1]
        if argumento1 == 'moeda':
            mostrar_moedas(ler_nome_do_pais())
        elif argumento1 == 'contagem':
            print("Existem {} países na API".format(contagem_de_paises()))
        elif argumento1 == 'populacao':
            mostrar_populacao(ler_nome_do_pais())
        else:
            print("Argumento inválido!!!")
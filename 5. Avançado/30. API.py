# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Consumo de API com a biblioteca 'requests' em Python

Este arquivo apresenta exemplos de como consumir APIs utilizando a biblioteca 'requests'.

Certifique-se de ter o requests instalado usando o seguinte comando:
pip install requests
"""

# FIXME: Parâmetros de Requisição
# headers: envio de cabeçalho http
# data: envio de dados no corpo da requisição
# json: envio de dados no corpo da requisição em formato JSON
# params: envio de parâmetros na URL

# FIXME: Métodos de requisicão
# get: serve para obter dados de uma API
# post: serve para enviar dados para uma API
# put: serve para atualizar dados em uma API

import requests


# Exemplo 1: Requisição GET simples
def exemplo_get_simples():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.put(url)

    if response.status_code == 200:
        # Exibe o conteúdo da resposta (em formato JSON)
        print("Exemplo 1:")
        print(response.json())
    else:
        print(f"Erro na requisição GET: {response.status_code}")


# Exemplo 2: Requisição GET com parâmetros
def exemplo_get_com_parametros():
    url = "https://app.omie.com.br/api/v1/geral/departamentos/"
    headers = {'Content-type': 'application/json'}
    data = {"call":"AlterarDepartamento","app_key":"38333295000","app_secret":"fed2******************1258","param":[{"descricao":"","codigo":"000000000723648"}]}
    response = requests.get(url=url, headers=headers, data=data)

    if response.status_code == 200:
        # Exibe o conteúdo da resposta (em formato JSON)
        print("\nExemplo 2:")
        print(response.json())
    else:
        print(f"Erro na requisição GET com parâmetros: {response.status_code}")


# Exemplo 3: Requisição POST
def exemplo_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(url, json=data)

    if response.status_code == 201:
        # Exibe o conteúdo da resposta (em formato JSON)
        print("\nExemplo 3:")
        print(response.json())
    else:
        print(f"Erro na requisição POST: {response.status_code}")


# Exemplo 4: Manipulando Cabeçalhos
def exemplo_cabecalhos():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    headers = {"User-Agent": "MeuApp/1.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Exibe o conteúdo da resposta (em formato JSON)
        print("\nExemplo 4:")
        print(response.json())
    else:
        print(f"Erro na requisição GET com cabeçalhos: {response.status_code}")


# Executar os Exemplos
if __name__ == "__main__":
    exemplo_get_simples()
    exemplo_get_com_parametros()
    exemplo_post()
    exemplo_cabecalhos()

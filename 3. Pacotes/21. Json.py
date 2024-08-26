# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Uso do Módulo json em Python

Este arquivo demonstra o uso do módulo json em Python para enviar os dados para outros sistemas ou para armazenar em arquivos.

1. Codificando (Serializando) um Dicionário para JSON
2. Decodificando (Deserializando) JSON para um Dicionário
3. Escrevendo JSON em um Arquivo
4. Lendo JSON de um Arquivo
"""

import json

print("1. Codificando (Serializando) um Dicionário para JSON:")
# Criando um dicionário
dados_dict = {
    "nome": "Alice",
    "idade": 30,
    'cidade': 'Cidade A'
}
print(dados_dict)
print(type(dados_dict))

# Codificando o dicionário para JSON: implementar as aspas duplas (Prepara o dicionário para ser enviado em requisições)
dados_json = json.dumps(dados_dict)
print(f"Dados em formato JSON:\n{dados_json}")
print(type(dados_dict))


print("\n2. Decodificando (Deserializando) JSON para um Dicionário:")
# Decodificando JSON em string para um dicionário python
dados_decodificados = json.loads(dados_json)
print(f"Dados Decodificados:\n{dados_decodificados}")


# Converter lista em string para tipo lista
lista = "[ 1,2,3]"
print(json.loads(lista))
print(type(json.loads(lista)))

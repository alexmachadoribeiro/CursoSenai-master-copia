"""
Anos atrás você desenvolveu um programa que lê um arquivo CSV chamado housing.csv e imprime os dados na tela.
O objetivo do programa era localizar pelo menos 5 imóveis com preço maior do que 12.000.000.
O programa funcionava perfeitamente, mas por algum motivo agora ele está em loop infinito, nunca para de executar.
Seu cliente te procurou para corrigir o problema e você precisa resolver isso o mais rápido possível.

"""

import csv

nome_arquivo = 'housing.csv'

# Lista para armazenar os dados do CSV como uma matriz de listas
dados_matriz = []

# Abrir o arquivo CSV e ler os dados
with open(nome_arquivo, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    # Iterar sobre as linhas do CSV e adicionar à matriz
    for linha in leitor_csv:
        dados_matriz.append(linha)

tamanho_dados = len(dados_matriz)

# Localize pelo menos 5 imóveis com preço maior do que 12.000
qtd_imoveis_12k = 5
imoveis_localizados = 0

contador = 0
while imoveis_localizados < qtd_imoveis_12k:
    try:
        # print(dados_matriz[contador])
        contador += 1

        if float(dados_matriz[contador][0]) > 12000000:
            print(f"Imóvel localizado: {dados_matriz[contador]}")
            imoveis_localizados += 1
    except:
        print("Todos os imovéis foram analisados")
        print(f"Foram encontrados apenas {imoveis_localizados} na sua base de dados")
        break

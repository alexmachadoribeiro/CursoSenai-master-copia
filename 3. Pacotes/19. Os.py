# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Uso do Módulo os em Python (incluindo Leitura de Arquivos)

Este arquivo demonstra o uso do módulo os em Python, incluindo leitura de arquivos.

1. Obtendo Informações sobre o Diretório Atual
2. Listando Arquivos em um Diretório
3. Criando e Removendo Diretórios
4. Executando Comandos do Sistema
5. Leitura de Arquivo
"""

import os

print("1. Obtendo Informações sobre o Diretório Atual:")
diretorio_atual = os.getcwd()
print(f"Diretório Atual: {diretorio_atual}")

print("\n2. Listando Arquivos em um Diretório:")
arquivos_no_diretorio = os.listdir(diretorio_atual)
print(f"Arquivos no Diretório Atual: {arquivos_no_diretorio}")

print("\n3. Criando e Removendo Diretórios:")
novo_diretorio = "novo_diretorio"
os.mkdir(novo_diretorio)
print(f"Diretório '{novo_diretorio}' criado.")

os.rmdir(novo_diretorio)
print(f"Diretório '{novo_diretorio}' removido.")

print("\n4. Leitura de Arquivo:")
# Vamos criar um arquivo de exemplo para leitura
nome_arquivo = "exemplo.txt"
conteudo_arquivo = "Conteúdo do arquivo de exemplo."

with open(nome_arquivo, "w") as arquivo:
    arquivo.write(conteudo_arquivo)

# Obtendo o caminho absoluto do arquivo
caminho_arquivo = os.path.abspath(nome_arquivo)
print(f"Caminho do Arquivo: {caminho_arquivo}")

# Leitura do arquivo
with open(caminho_arquivo, "r") as arquivo:
    conteudo_lido = arquivo.read()
    print(f"Conteúdo do Arquivo:\n{conteudo_lido}")

# Escrevendo no arquivo
novo_conteudo = "Novo conteúdo do arquivo de exemplo."
with open(caminho_arquivo, "a", encoding="UTF-8") as arquivo:
    arquivo.write(novo_conteudo)

# Removendo o arquivo de exemplo
os.remove(caminho_arquivo)
print(f"Arquivo '{nome_arquivo}' removido.")

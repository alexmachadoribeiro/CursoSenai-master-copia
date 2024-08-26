# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Uso do Módulo shutil em Python

Este arquivo demonstra o uso do módulo shutil em Python.

1. Copiando um Arquivo
2. Copiando um Diretório
3. Removendo um Arquivo
4. Removendo um Diretório Recursivamente
5. Movendo um Arquivo ou Diretório
"""

import shutil
import os

print("1. Copiando um Arquivo:")
# Criando um arquivo de exemplo
nome_arquivo_origem = "exemplo_origem.txt"
conteudo_arquivo = "Conteúdo do arquivo de exemplo."

with open(nome_arquivo_origem, "w") as arquivo_origem:
    arquivo_origem.write(conteudo_arquivo)

# Copiando o arquivo
nome_arquivo_destino = "exemplo_destino.txt"
shutil.copy(nome_arquivo_origem, nome_arquivo_destino)
print(f"Arquivo '{nome_arquivo_origem}' copiado para '{nome_arquivo_destino}'.")

diretorio_origem = "diretorio_origem"

# Copiando o diretório
diretorio_destino = "diretorio_destino"
shutil.copytree(diretorio_origem, diretorio_destino)
print(f"Diretório '{diretorio_origem}' copiado para '{diretorio_destino}'.")

# Removendo os diretórios de exemplo
shutil.rmtree(diretorio_origem)
shutil.rmtree(diretorio_destino)
print("Diretórios de exemplo removidos.")

print("\n5. Movendo um Arquivo ou Diretório:")
nome_arquivo_movimento = "exemplo.txt"

# Movendo o arquivo
diretorio_destino_movimento = "diretorio_novo"
shutil.move(nome_arquivo_movimento, diretorio_destino_movimento)
print(f"Arquivo '{nome_arquivo_movimento}' movido para '{diretorio_destino_movimento}'.")
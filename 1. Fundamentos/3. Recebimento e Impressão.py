# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Recebimento e Impressão de Dados em Python

Este arquivo demonstra o uso das funções input() e print() para interação com o usuário.

1. Recebimento de Dados com input():
   A função input() é utilizada para receber dados do usuário.

2. Impressão de Dados com print():
   A função print() é utilizada para exibir dados na tela.

"""

# 1. Recebimento de Dados com input()
nome = input("Digite seu nome: ")
idade_str = input("Digite sua idade: ")  # input() retorna uma string

# Converter a idade para um número inteiro
idade = int(idade_str)

# 2. Impressão de Dados com print()
print("\nInformações do Usuário:")
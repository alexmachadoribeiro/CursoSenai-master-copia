# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Tuplas em Python

Este arquivo demonstra o uso de tuplas em Python.

1. Criando uma Tupla
2. Acessando Elementos da Tupla
3. Imutabilidade das Tuplas
4. Desempacotamento de Tuplas
5. Métodos de Tuplas

"""

# 1. Criando uma Tupla
tupla_frutas = ("maçã", "banana", "uva", "laranja")
# tupla_frutas = "maçã", "banana", "uva", "laranja"

print(tupla_frutas)

# 2. Acessando Elementos da Tupla
print("1. Acessando Elementos da Tupla:")
print(f"Primeira fruta: {tupla_frutas[0]}")
print(f"Última fruta: {tupla_frutas[-1]}")

# 3. Imutabilidade das Tuplas
print("\n2. Imutabilidade das Tuplas:")
# Tentativa de modificação (irá gerar um erro)
# tupla_frutas[1] = "kiwi"

# 4. Desempacotamento de Tuplas
print("\n3. Desempacotamento de Tuplas:")
fruta1, fruta2, fruta3, fruta4 = tupla_frutas
print(f"Desempacotamento: {fruta1}, {fruta2}, {fruta3}, {fruta4}")

# 5. Métodos de Tuplas
print("\n4. Métodos de Tuplas:")
tupla_numeros = (1, 2, 3, 2)

# Identificando a posição
indice = tupla_numeros.index(3)
print(f"Índice do elemento 3: {indice}")

# Tamanho da tupla
tamanho = len(tupla_numeros)
print(f"Tamanho da tupla: {tamanho}")

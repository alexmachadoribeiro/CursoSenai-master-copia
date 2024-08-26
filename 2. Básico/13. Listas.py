# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Operações com Listas em Python

Este arquivo demonstra diversas operações com listas em Python.

1. Criando uma Lista
2. Acessando Elementos da Lista
3. Modificando Elementos da Lista
4. Adicionando Elementos à Lista
5. Removendo Elementos da Lista
6. Operações com Listas
7. Listas Aninhadas
8. Métodos de Listas

"""

# 1. Criando uma Lista
frutas = ["maçã", "banana", "uva", "laranja"]

# 2. Acessando Elementos da Lista
print("1. Acessando Elementos da Lista:")
print(f"Primeira fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")

# 3. Modificando Elementos da Lista
print("\n2. Modificando Elementos da Lista:")
frutas[1] = "kiwi"
print(f"Lista de frutas atualizada: {frutas}")

# 4. Adicionando Elementos à Lista
print("\n3. Adicionando Elementos à Lista:")
frutas.append("abacaxi")
frutas.insert(2, "morango")
print(f"Lista de frutas após adição: {frutas}")

# 5. Removendo Elementos da Lista
print("\n4. Removendo Elementos da Lista:")
frutas.remove("uva")
del frutas[0]
print(f"Lista de frutas após remoção: {frutas}")

# 6. Operações com Listas
print("\n5. Operações com Listas:")
numeros = [1, 2, 3]
outra_lista = frutas + numeros
print(f"Concatenação de listas: {outra_lista}")
repeticao = frutas * 2
print(f"Repetição da lista: {repeticao}")

# 7. Listas Aninhadas
print("\n6. Listas Aninhadas:")
lista_aninhada = [["a", "b", "c"], [1, 2, 3], ["x", "y", "z"]]
print(f"Elemento na segunda lista, terceiro índice: {lista_aninhada[1][2]}")

# 8. Métodos de Listas
print("\n7. Métodos de Listas:")
lista = [1, 2, 3, 2]

# Adicionando elementos
lista.append(4)
print(f"Lista após append(4): {lista}")

# Removendo elementos
lista.remove(2)
print(f"Lista após remove(2): {lista}")

# Removendo pelo índice
elemento = lista.pop(0)
print(f"Elemento removido pelo pop(0): {elemento}, Lista atual: {lista}")

# Identificando a posição
indice = lista.index(3)
print(f"Índice do elemento 3: {indice}")

# Contando ocorrências
ocorrencias = lista.count(2)
print(f"Ocorrências do elemento 2: {ocorrencias}")

# Ordenando a lista
lista.sort()
print(f"Lista ordenada: {lista}")

# Invertendo a lista
lista.reverse()
print(f"Lista invertida: {lista}")

# Limpando a lista
lista.clear()
print(f"Lista após clear(): {lista}")

# Copiando a lista
lista_original = [1, 2, 3]
lista_copia = lista_original.copy()
print(f"Cópia da lista: {lista_copia}")

# Acessando parte da lista
sublista = lista_copia[1:3]
print(f"Sublista [1:3]: {sublista}")

# Tamanho da lista
tamanho = len(lista_copia)
print(f"Tamanho da lista: {tamanho}")

# Desempacotamento de listas
lista_numeros = [1, 2, 3]
a, b, c = lista_numeros
print(f"Desempacotamento de listas: a={a}, b={b}, c={c}")

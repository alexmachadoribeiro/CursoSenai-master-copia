# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Uso do Loop For em Python

Este arquivo demonstra o uso do loop for em Python.

1. Iterando sobre uma Lista
2. Iterando sobre uma String
3. Utilizando a Função range()
4. Utilizando a Instrução break no Loop For
5. Utilizando a Instrução continue no Loop For

"""

# 1. Iterando sobre uma Lista
frutas = ["maçã", "banana", "uva", "laranja"]

print("1. Iterando sobre uma Lista:")
for fruta in frutas:
    print(fruta)

# 2. Iterando sobre uma String
mensagem = "Python"

print("\n2. Iterando sobre uma String:")
for letra in mensagem:
    print(letra)

# 3. Utilizando a Função range()
print("\n3. Utilizando a Função range():")
for numero in range(5):
    print(numero)

# 4. Utilizando a Instrução break no Loop For
print("\n4. Utilizando a Instrução break no Loop For:")
for i in range(10):

    if i == 5:
        break
    elif i == 7:
        pass
    else:
        print(i)

# 5. Utilizando a Instrução continue no Loop For
print("\n5. Utilizando a Instrução continue no Loop For:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

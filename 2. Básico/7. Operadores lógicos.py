# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Operadores Lógicos em Python

Este arquivo demonstra o uso dos operadores lógicos básicos em Python.

1. Operador AND (and)
2. Operador OR (or)
3. Operador NOT (not)

"""

# 1. Operador AND (and)
idade = 25
tem_cartao = True

if idade >= 18 and tem_cartao:
    print("1. Você pode fazer uma compra, pois é maior de idade e possui um cartão.")
else:
    print("1. Você não pode fazer a compra.")

# 2. Operador OR (or)
tem_entrada = False
tem_convite = True

if tem_entrada or tem_convite:
    print("2. Você pode entrar, pois possui entrada ou um convite.")
else:
    print("2. Você não pode entrar.")

# 3. Operador NOT (not)
tem_cartao = False

if not tem_cartao:
    print("3. Você não possui um cartão.")
else:
    print("3. Você possui um cartão.")

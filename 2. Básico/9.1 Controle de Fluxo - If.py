# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Uso de if, elif, else e Operador Ternário em Python

Este arquivo demonstra o uso de if, elif, else e o operador ternário em Python.

1. Estrutura if simples
2. Estrutura if-else
3. Estrutura if-elif-else
4. Operador Ternário

"""

# 1. Estrutura if simples
idade = 18

if idade >= 18:
    print("1. Você é maior de idade.")

# 2. Estrutura if-else
numeral = 25

if numeral > 20:
    print(f"Imprime o valor de numeral: {numeral}")
else:
    print("Não imprime")

# 3. Estrutura if-elif-else
nota = 75

if nota >= 90:
    print("3. Você recebeu uma nota A.")
elif nota >= 80:
    print("3. Você recebeu uma nota B.")
elif nota >= 70:
    print("3. Você recebeu uma nota C.")
else:
    print("3. Você não atingiu a nota mínima.")

# 4. Operador Ternário
idade = 21
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(f"4. Status: {status}")
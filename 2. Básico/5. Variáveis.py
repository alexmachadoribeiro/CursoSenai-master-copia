# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Variáveis, Constantes e Seus Usos em Python

Este arquivo demonstra o conceito de variáveis e constantes, e mostra alguns usos práticos.

1. Variáveis:
   - Locais para armazenar dados.
   - Podem ter seus valores modificados durante a execução do programa.

2. Constantes:
   - Valores que não devem ser alterados durante a execução do programa.
   - Em Python, não há constantes estritas, mas convenções são usadas para indicar que uma variável é uma constante.

3. Usos Práticos:
   - Demonstração de como usar variáveis e constantes em situações do dia a dia.

"""

# 1. Variáveis
nome = "Alice"
idade = "30"
altura = 1.75
print(type(idade))

idade = int(idade)

print(type(idade))

# Modificando o valor de uma variável
idade = 31

# 2. Constantes
PI = 3.14159
TAXA_DE_JUROS = 0.05

# Em Python, convenção de nomes em maiúsculas indica que a variável é uma constante,
# embora isso seja uma convenção e não uma regra estrita do Python.

# 3. Usos Práticos
# Cálculo do IMC (Índice de Massa Corporal)
peso = 70
altura = 1.75
imc = peso / altura**2

# Exibindo resultados
print(f"\nDados do Usuário:")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura} metros")
print("\nConstantes:")
print(f"Valor de PI: {PI}")
print(f"Taxa de Juros: {TAXA_DE_JUROS}")
print("\nCálculo do IMC:")
print(f"IMC: {imc:.2f}")

# Usando constantes em cálculos
raio = 5
area_circulo = PI * (raio**2)
print("\nÁrea de um Círculo:")
print(f"Raio: {raio}")
print(f"Área do Círculo: {area_circulo:.2f}")

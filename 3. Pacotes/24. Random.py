# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Uso do Pacote random em Python

Este arquivo demonstra o uso do pacote random em Python.

1. Geração de Números Aleatórios Inteiros
2. Geração de Números Aleatórios de Ponto Flutuante
3. Escolha Aleatória de Elementos de uma Sequência
4. Embaralhamento de uma Sequência
"""

import random

print("1. Geração de Números Aleatórios Inteiros:")
# Gerando um número aleatório inteiro entre 1 e 10 (inclusive)
numero_inteiro = random.randint(1, 10)
print(f"Número Aleatório Inteiro: {numero_inteiro}")

print("\n2. Geração de Números Aleatórios de Ponto Flutuante:")
# Gerando um número aleatório de ponto flutuante entre 0 e 1
numero_ponto_flutuante = random.random()
print(f"Número Aleatório de Ponto Flutuante: {numero_ponto_flutuante}")

print("\n3. Escolha Aleatória de Elementos de uma Sequência:")
# Escolhendo aleatoriamente um elemento de uma lista
frutas = ['maçã', 'banana', 'laranja', 'uva']
fruta_aleatoria = random.choice(frutas)
print(f"Fruta Escolhida Aleatoriamente: {fruta_aleatoria}")

print("\n4. Embaralhamento de uma Sequência:")
# Embaralhando aleatoriamente os elementos de uma lista
sequencia = [1, 2, 3, 4, 5]
random.shuffle(sequencia)
print(f"Sequência Embaralhada: {sequencia}")

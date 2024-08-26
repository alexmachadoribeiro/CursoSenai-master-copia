# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Argumentos em Funções em Python

Este arquivo demonstra o uso de argumentos em funções em Python.

1. Argumentos Posicionais
2. Argumentos Nomeados
3. Argumentos Padrão
4. Argumentos Arbitrários (*args)
5. Argumentos Nomeados Arbitrários (**kwargs)

"""


# 1. Argumentos Posicionais
def saudacao(nome, mensagem):
    print(f"{mensagem}, {nome}!")

# Chamando a função com argumentos posicionais
saudacao("Alice", "Olá")


# 2. Argumentos Nomeados
def calcular_potencia(base, expoente):
    resultado = base ** expoente
    print(f"{base} elevado a {expoente} é {resultado}.")

# Chamando a função com argumentos nomeados
calcular_potencia(base=2, expoente=3)


# 3. Argumentos Padrão
def calcular_juros(valor, taxa=0.1):
    juros = valor * taxa
    total = valor + juros
    print(f"Valor inicial: {valor}, Juros: {juros}, Total: {total}.")

# Chamando a função com argumento padrão e sem argumento padrão
calcular_juros(1000)
calcular_juros(1000, 0.05)


# 4. Argumentos Arbitrários (*args)
def somar_numeros(*args):
    total = sum(args)
    print(f"Soma dos números: {total}.")

# Chamando a função com um número arbitrário de argumentos
somar_numeros(1, 2, 3, 4, 5)


# 5. Argumentos Nomeados Arbitrários (**kwargs)
def exibir_info(**kwargs):
    print("kwargs")
    print(kwargs)
    print(kwargs.items())
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Chamando a função com argumentos nomeados arbitrários
exibir_info(nome="Alice", idade=25, cidade="Cidade A")


# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Funções em Python

Este arquivo demonstra o uso de funções em Python, incluindo definição, parâmetros, parâmetros nomeados,
parâmetros não nomeados, valor padrão para parâmetros e retorno de valores.

1. Definindo uma Função Simples
2. Função com Parâmetros
3. Parâmetros Nomeados e Não Nomeados
4. Valor Padrão para Parâmetros
5. Retorno de Valores

"""


# 1. Definindo uma Função Simples
def saudacao():
    print("Olá! Bem-vindo.")


# Chamando a função
saudacao()


# 2. Função com Parâmetros
def saudacao_personalizada(nome):
    print(f"Olá, {nome}! Bem-vindo.")


# Chamando a função com um argumento
saudacao_personalizada("Alice")


# 3. Parâmetros Nomeados e Não Nomeados
def soma(a, b):
    resultado = a + b
    print(f"A soma de {a} e {b} é {resultado}.")


# Chamando a função com parâmetros nomeados
soma(b=3, a=2)


# 4. Valor Padrão para Parâmetros
def potencia(base, expoente=2):
    resultado = base ** expoente
    print(f"{base} elevado a {expoente} é {resultado}.")


# Chamando a função com valor padrão e sem valor padrão
potencia(3)
potencia(2, 3)


# 5. Retorno de Valores
def calcular_media(notas):
    quantidade = len(notas)
    soma = sum(notas)
    media = soma / quantidade
    return media


# Chamando a função e recebendo o valor de retorno
notas_aluno = [8, 9, 7.5, 9.5]
media_aluno = calcular_media(notas_aluno)
print(f"A média do aluno é {media_aluno}.")

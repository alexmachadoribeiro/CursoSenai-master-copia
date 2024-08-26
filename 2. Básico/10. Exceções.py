# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Tratamento de Exceções em Python

Este arquivo demonstra o uso de exceções em Python com as cláusulas try, except, else e finally.

1. Tratamento Básico de Exceções
2. Tratamento de Exceções Específicas
3. Cláusula else e finally
4. Levantando Exceções Personalizadas

"""

# 1. Tratamento Básico de Exceções
try:
    numerador = 10
    denominador = 0
    resultado = numerador / denominador
except ZeroDivisionError:
    print("1. Erro: Divisão por zero.")
else:
    print(f"1. Resultado: {resultado}")
finally:
    print("1. Executando a cláusula finally.")

# 2. Tratamento de Exceções Específicas
try:
    lista = [1, 2, 3]
    elemento = lista[5]
except IndexError:
    print("2. Erro: Índice fora do alcance da lista.")
else:
    print(f"2. Elemento: {elemento}")
finally:
    print("2. Executando a cláusula finally.")

# 3. Cláusula else e finally
try:
    arquivo = open("arquivo_inexistente.txt", "r")
except FileNotFoundError:
    print("3. Erro: Arquivo não encontrado.")
else:
    conteudo = arquivo.read()
    print(f"3. Conteúdo do arquivo: {conteudo}")
finally:
    if 'arquivo' in locals():
        arquivo.close()
    print("3. Executando a cláusula finally.")


# 4. Levantando Exceções Personalizadas
class MeuErroPersonalizado(Exception):
    pass

try:
    raise MeuErroPersonalizado("4. Uma mensagem de erro personalizada.")
except MeuErroPersonalizado as e:
    print(e)
finally:
    print("4. Executando a cláusula finally.")

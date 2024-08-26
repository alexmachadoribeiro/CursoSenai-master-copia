# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Uso do Módulo re em Python (Atualizado)
Documentação: https://docs.python.org/pt-br/3/library/re.html

Este arquivo demonstra o uso do módulo re em Python para trabalhar com expressões regulares.

1. Correspondência Simples
2. Utilizando Metacaracteres
3. Agrupamento e Captura
4. Busca com Modificadores
5. Buscando Datas
6. Buscando Horas
7. Encontrando Sequências de 3 Letras Seguidas de 2 Dígitos

\d -> Dígitos (0-9)
\w -> Caracteres Alfanuméricos (A-Z, a-z, 0-9, _)
    Buscar não numéricos: \D
\b[A-Za-z] -> letras
\s -> Espaços em Branco (tab, espaço, nova linha)
\b -> Limite de Palavra
^ ->20 Início de uma String
$ -> Fim de uma String
[] -> Conjunto de Caracteres
[^] -> Conjunto Negado de Caracteres
. -> Qualquer Caractere, exceto nova linha
* -> 0 ou mais ocorrências
+ -> 1 ou mais ocorrências
? -> 0 ou 1 ocorrência
{3} -> Exatamente 3 ocorrências
{3,4} -> De 3 a 4 ocorrências
{3,} -> 3 ou mais ocorrências
"""

import re

# re.search: procura a 1ª ocorrência do padrão na string / erro caso não encontre
# group(): retorna a string correspondente ao padrão

# re.findall: procura todas as ocorrências do padrão na string (retorna uma lista)


print("1. Correspondência Simples:")
# Verifica se a string contém a palavra "Python"
padrao_simples = re.search(pattern=r'Python', string='Python é uma linguagem de programação poderosa.')
if padrao_simples:
    print(f"Correspondência encontrada: {padrao_simples.group()}")
else:
    print("Correspondência não encontrada.")

print("\n2. Utilizando Metacaracteres:")
# Encontrando todos os dígitos em uma string
padrao_metacaracter = re.findall(pattern=r'\d', string='A idade de Alice é 25 e a de Bob é 30.')
print(f"Dígitos encontrados: {padrao_metacaracter}")

print("\n3. Agrupamento e Captura:")
# Capturando o código de área de um número de telefone
# Group 0 - padrão completo
# Group 1 - primeiro parêntese
padrao_captura = re.search(pattern=r'(\d{3})-\d{3}-\d{4}', string='Telefone: 123-456-7890')
if padrao_captura:
    codigo_area = padrao_captura.group(1)
    print(f"Código de Área Capturado: {codigo_area}")

print("\n4. Busca com Modificadores:")
# Buscando a palavra "python" independentemente de maiúsculas ou minúsculas
padrao_modificador = re.search(pattern=r'python', string='Python é uma linguagem de programação.', flags=re.IGNORECASE)
if padrao_modificador:
    print("Correspondência encontrada (ignorando maiúsculas/minúsculas).")
else:
    print("Correspondência não encontrada.")

print("\n5. Buscando Datas:")
# Buscando datas no formato dd/mm/aaaa
padrao_datas = re.findall(pattern=r'\d{2}/\d{2}/\d{4}', string='Datas: 01/01/2022, 15/03/2023, 30/12/2024')
print(f"Datas encontradas: {padrao_datas}")

print("\n6. Buscando Horas:")
# Buscando horas no formato hh:mm
padrao_horas = re.findall(pattern=r'\d{2}:\d{2}', string='Horas: 09:30, 14:45, 18:00')
print(f"Horas encontradas: {padrao_horas}")

print("\n7. Encontrando Sequências de 3 Letras Seguidas de 2 Dígitos:")
# Encontrando padrões alfanuméricos específicos
padrao_sequencia = re.findall(pattern=r'\b[A-Za-z]{3}\d{2}\b', string='ABC12 XYZ45 LMN78')
print(f"Sequências encontradas: {padrao_sequencia}")

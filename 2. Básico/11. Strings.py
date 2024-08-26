# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Operações com Strings em Python

Este arquivo demonstra diversas operações com strings em Python.

1. Iteração sobre uma String
2. Utilizando o Método join()
3. Utilizando o Método split()
4. Utilizando o Método strip()
5. Verificando se uma String Começa ou Termina com Outra
6. Encontrando a Posição de uma Substring
7. Substituindo Substrings
8. Convertendo Maiúsculas e Minúsculas
9. Formatando Strings

"""

# 1. Iteração sobre uma String
mensagem = "Python é incrível!"

print("1. Iteração sobre uma String:")
for caractere in mensagem:
    print(caractere)

# 2. Utilizando o Método join()
palavras = ["Python", "é", "incrível!"]

print("\n2. Utilizando o Método join():")
frase = " ".join(palavras)
print(frase)

# 3. Utilizando o Método split()
frase = "Python é incrível!"

print("\n3. Utilizando o Método split():")
palavras = frase.split()
print(palavras)

# 4. Utilizando o Método strip()
espacoso = "    Python    "

print("\n4. Utilizando o Método strip():")
sem_espacos = espacoso.strip()
print(sem_espacos)

# 5. Verificando se uma String Começa ou Termina com Outra
nome_arquivo = "documento.txt"

print("\n5. Verificando se uma String Começa ou Termina com Outra:")
if nome_arquivo.startswith("doc"):
    print("O arquivo é um documento.")
if nome_arquivo.endswith(".txt"):
    print("O arquivo é um documento de texto.")

# 6. Encontrando a Posição de uma Substring
frase = "Python é incrível!"

print("\n6. Encontrando a Posição de uma Substring:")
posicao = frase.find("incrível")
print(f"A substring 'incrível' começa na posição: {posicao}")

# 7. Substituindo Substrings
frase = "Python é incrível!"

print("\n7. Substituindo Substrings:")
nova_frase = frase.replace("incrível", "fantástico")
print(nova_frase)

# 8. Convertendo Maiúsculas e Minúsculas
texto = "Python é Fantástico!"

print("\n8. Convertendo Maiúsculas e Minúsculas:")
print(f"Maiúsculas: {texto.upper()}")
print(f"Minúsculas: {texto.lower()}")

# 9. Formatando Strings
nome = "Alice"
idade = 30

print("\n9. Formatando Strings:")
mensagem_formatada = "Olá, meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(mensagem_formatada)

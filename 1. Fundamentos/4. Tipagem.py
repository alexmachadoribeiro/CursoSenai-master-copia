# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Tipos de Dados em Python

Este arquivo demonstra os principais tipos de dados em Python e como utilizá-los.

1. Tipos Numéricos:
   - int: Números inteiros
   - float: Números de ponto flutuante

2. Tipo Booleano:
   - bool: Valores booleanos (True ou False)

3. Tipo String:
   - str: Sequências de caracteres

4. Tipo Nulo:
   - None: Representa a ausência de valor

5. Operadores 'is' e 'is not':
   - Utilizados para verificar identidade de objetos, especialmente úteis com None.

6. Função type():
   - Utilizada para obter o tipo de um objeto.

"""

# 1. Tipos Numéricos
numero_inteiro = 42
numero_ponto_flutuante = 3.14

# 2. Tipo Booleano
verdadeiro = True
falso = False

# 3. Tipo String (aspas duplas ou simples)
mensagem = "Olá, Python!"
altenar_aspas = "Olá, 'Python'!"

# caracter_escape = "Olá, \"Python\"!" # Não é lido pelo interpretador
ler_escape = r"Olá, \"Python\"!" # Lê o caracter de escape
print("caracter_escape")
# print(caracter_escape)
print(ler_escape)

nome = "Luciano"
idade = 65
mensagem_fstring = (f" Olá, meu nome é {nome} e "
                    f"eu tenho {idade} anos.asdkjfbasdbhfkjashfshdk"
                    f"fhsdkjfvhnksdjhngkljçs")
print("mensagem_fstring")
print(mensagem_fstring)

# 4. Tipo Nulo
valor_nulo = None

# 5. Operadores 'is' e 'is not'
# 'is' verifica se dois objetos são o mesmo (mesmo objeto na memória)
# 'is not' verifica se dois objetos não são o mesmo
if valor_nulo is None:
    print("O valor é nulo.")

# 6. Função type()
print("\nTipos dos Objetos:")
print(f"Tipo de numero_inteiro: {type(numero_inteiro)}")
print(f"Tipo de numero_ponto_flutuante: {type(numero_ponto_flutuante)}")
print(f"Tipo de verdadeiro: {type(verdadeiro)}")
print(f"Tipo de falso: {type(falso)}")
print(f"Tipo de mensagem: {type(mensagem)}")
print(f"Tipo de valor_nulo: {type(valor_nulo)}")

# Exemplo de como usar type() para verificar o tipo de uma variável
if type(numero_inteiro) is int:
    print("É um número inteiro.")

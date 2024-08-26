# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Uso do Loop While em Python

Este arquivo demonstra o uso do loop while em Python.

1. Loop While Simples
2. Utilizando Condição de Parada
3. Utilizando a Instrução break
4. Utilizando a Instrução continue

"""

# 1. Loop While Simples
contador = 0

while contador < 5:
    print(f"1. Contador: {contador}")
    contador += 1

# 2. Utilizando Condição de Parada
numero = 1

while numero <= 10:
    print(f"2. Número: {numero}")
    numero += 2  # Apenas números ímpares
    # Condição de parada
    if numero == 7:
        break

# 3. Utilizando a Instrução break
tentativas = 0

while True:
    senha = input("3. Digite a senha: ")
    if senha == "senha123":
        print("Senha correta. Acesso permitido!")
        break
    else:
        print("Senha incorreta. Tente novamente.")
        tentativas += 1

        if tentativas == 3:
            print("Você atingiu o limite de tentativas. Acesso bloqueado.")
            break

# 4. Utilizando a Instrução continue
contador = 0

while contador < 5:
    contador += 1

    # Pula a iteração se o contador for ímpar
    if contador % 2 != 0:
        continue

    print(f"4. Contador par: {contador}")
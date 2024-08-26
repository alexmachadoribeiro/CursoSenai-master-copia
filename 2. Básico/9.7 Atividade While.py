"""
Faça um programa que receba um número do usuário com as seguintes funcionalidades:
    - verifique se o número informado é um número convertível para inteiro, se não solicite novamente
    outro número
    - utilize este número como um limite para um contador, ou seja, de 0 até o número informado
    execute a ação a seguir
        - verifique o módulo do número por 2 é igual a 0, se sim imprima o número
"""

numero = 0
while True:
    numero = input("Digite um número: ")
    try:
        numero = int(numero)
        print("Número convertido com sucesso")
        break
    except:
        print("O valor informado não pode ser convertido para inteiro")

print(f"Número {numero} - tipo: {type(numero)}")

contador = 0
while contador < numero:
    if contador % 2 == 0:
        print(f"O número {contador} é par")
    contador += 1

print("Código finalizado")



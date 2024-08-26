"""
    1. IF... ELSE COMPOSTO
    Verifique se o número inteiro digitado pelo usuário é:
        - é par E maior do que 10
        - é ímpar OU menor do que 5
 """

# FIXME: Construa aqui sua solução
print("<<< Exercício n° 1 >>>")
numero = input("Digite um número: ")
try:
    numero = int(numero)
except:
    print("Erro na conversão")

if numero % 2 == 0 and numero > 10:
    print("par E maior do que 10")
elif numero % 2 != 0 or numero < 5:
    print("ímpar OU menor do que 5")



"""
    2. LEITURA DE DADOS COM FOR
    Utilizando os mesmos dados do arquivo CSV housing.csv, solicite ao usuário que digite um número inteiro N.
    Em seguida, leia as N primeiras linhas do arquivo e imprima na tela utilizando o laço de repetição for.
"""
print("\n\n<<< Exercício n° 2 >>>")
import csv

nome_arquivo = 'housing.csv'

# Lista para armazenar os dados do CSV como uma matriz de listas
dados_matriz = []

# Abrir o arquivo CSV e ler os dados
with open(nome_arquivo, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    # Iterar sobre as linhas do CSV e adicionar à matriz
    for linha in leitor_csv:
        dados_matriz.append(linha)

# Os dados se encontram na variável dados_matriz
# FIXME: Construa aqui sua solução
repeticoes_str = input("Número de repetições: ")
repeticoes_int = int(repeticoes_str)

for enum, linha in enumerate(dados_matriz):
    print(linha)
    if enum == repeticoes_int:
        break


"""
    3. EXERCÍCIO DE TRY... EXCEPT
    Receba um número do usuário dentro de um loop infinito
    Converta o número recebido para float
    Tratando possíveis erros de conversão
    Caso o valor seja convertido com sucesso, imprima o valor utilizando a clásula que só imprime 
        o valor se não houver exceção
    Caso contrário, imprima a mensagem de erro correspondente e reinicie o loop
    Tanto no caso de sucesso como erro, sempre imprima uma mensagem de que o loop nº {{1}} foi 
        executado
"""
print("\n\n<<< Exercício n° 3 >>>")

# # FIXME: Construa aqui sua solução
contador = 0
while True:
    try:
        var1 = input("Informe um número convertível para float: ")
        var1_float = float(var1)
    except:
        print("Houve um erro na conversão do número informado, favor informar outro")
    else:
        print(f"O número {var1_float} foi convertido para float com sucesso")
        break
    finally:
        print(f"O loop nº {contador} foi executado com sucesso")
        contador += 1



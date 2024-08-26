# Estudo sobre Funções Lambda em Python

# 1. Introdução às Funções Lambda
# Funções lambda em Python são funções anônimas, úteis para situações onde você precisa de uma função temporária e simples.

# 2. Sintaxe Básica
# Sintaxe: lambda argumentos: expressao

# Exemplo:
dobro = lambda x: x * 2

# Uso da função lambda
resultado = dobro(5)
print("Dobro de 5:", resultado)  # Saída: 10

# 3. Características Principais
# - São anônimas
# - Consistem em uma única expressão
# - Sintaxe leve
# - Escopo limitado

# 4. Usos Comuns
# - Utilizadas com funções como map(), filter(), sorted().

# Exemplo com map() --> Utilizado para iteração com iteráveis
numeros = [1, 2, 3, 4, 5]
quadrados = map(lambda x: x**2, numeros)
quadrados = list(quadrados)  # Converte um objeto map para uma lista
print("Quadrados da lista:", quadrados)  # Saída: [1, 4, 9, 16, 25]

# 5. Considerações Finais
# - Use com moderação e clareza para manter o código legível.

# Exemplo com filter():  --> Utilizado para filtrar elementos de um iterável
pares = filter(lambda x: x % 2 == 0, numeros)
pares = list(pares)
print("Números pares da lista:", pares)  # Saída: [2, 4]

# 6. Conclusão
# Funções lambda são úteis para expressar lógica concisa em situações específicas, mas é importante usá-las com moderação.
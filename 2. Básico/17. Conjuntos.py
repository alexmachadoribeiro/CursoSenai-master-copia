# Estudo sobre Conjuntos em Python

# 1. Introdução aos Conjuntos
# Em Python, um conjunto é uma estrutura de dados que representa uma coleção não ordenada de elementos únicos.

# 2. Criando Conjuntos
# Existem várias maneiras de criar conjuntos em Python:

# Usando a função set():
conjunto1 = set([1, 2, 3, 4, 5])

# Usando a notação de chaves {}:
conjunto2 = {3, 4, 5, 6, 7}

# 3. Operações de Conjuntos
# Os conjuntos em Python suportam várias operações que são comuns em teoria dos conjuntos:

# União:
conjunto_uniao = conjunto1.union(conjunto2)

# Interseção:
conjunto_intersecao = conjunto1.intersection(conjunto2)

# Diferença:
conjunto_diferenca = conjunto1.difference(conjunto2)  # Elementos que existem no 1º, mas não no 2º

# Teste de Associação:
pertence = 3 in conjunto1

# 4. Mutabilidade e Modificação de Conjuntos
# Os conjuntos são mutáveis, o que significa que você pode modificar seu conteúdo após a criação.

# Adição de Elementos:
conjunto1.add(6)

# Remoção de Elementos:
conjunto1.remove(3)

# 5. Utilidade Prática
# Os conjuntos em Python são úteis em situações onde a exclusividade de elementos é crucial.

# 6. Limitações
# Os conjuntos em Python têm algumas limitações, como a falta de ordenação e a impossibilidade de indexação.

# 7. Conclusão
# Em resumo, os conjuntos em Python são uma ferramenta poderosa para lidar com coleções de elementos únicos.

# Exemplo de uso:
print("Conjunto União:", conjunto_uniao)
print("Conjunto Interseção:", conjunto_intersecao)
print("Conjunto Diferença:", conjunto_diferenca)
print("Pertence ao Conjunto1:", pertence)
print("Conjunto1 Modificado:", conjunto1)

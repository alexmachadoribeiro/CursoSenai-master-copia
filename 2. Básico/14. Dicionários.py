# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Dicionários em Python

Este arquivo demonstra o uso de dicionários em Python.

1. Criando um Dicionário
2. Acessando Valores por Chave
3. Adicionando, Modificando e Removendo Pares Chave-Valor
4. Verificando se uma Chave Existe
5. Obtendo Valor com um Padrão
6. Obtendo as Chaves, Valores e Itens do Dicionário
7. Removendo um Elemento com pop()
8. Removendo o Último Elemento com popitem()
9. Atualizando o Dicionário com update()
10. Atualizando o Dicionário com update() e Valor por Chave
"""

# 1. Criando um Dicionário
dicionario = {'nome': 'Alice', 'idade': 30, 'cidade': 'Cidade A'}

# 2. Acessando Valores por Chave
print("1. Acessando Valores por Chave:")
print(f"Nome: {dicionario['nome']}")
print(f"Idade: {dicionario['idade']}")
print(f"Cidade: {dicionario['cidade']}")

# 3. Adicionando, Modificando e Removendo Pares Chave-Valor
print("\n2. Adicionando, Modificando e Removendo Pares Chave-Valor:")
dicionario['profissao'] = 'Engenheiro'
print(f"Dicionário após adição: {dicionario}")

dicionario['idade'] = 31
print(f"Dicionário após modificação: {dicionario}")

del dicionario['cidade']
print(f"Dicionário após remoção: {dicionario}")

# 4. Verificando se uma Chave Existe
print("\n3. Verificando se uma Chave Existe:")
chave = 'cidade'
if chave in dicionario:
    print(f"A chave '{chave}' existe no dicionário.")
else:
    print(f"A chave '{chave}' não existe no dicionário.")

# 5. Obtendo Valor com um Padrão
print("\n4. Obtendo Valor com um Padrão:")
idade = dicionario.get('idade', None)
profissao = dicionario.get('profissao', None)
print(f"Idade: {idade}")
print(f"Profissão: {profissao}")

# 6. Obtendo as Chaves, Valores e Itens do Dicionário
print("\n5. Obtendo as Chaves, Valores e Itens do Dicionário:")
chaves = dicionario.keys()
valores = dicionario.values()
itens = dicionario.items()

print(f"Chaves: {chaves}")
print(f"Valores: {valores}")
print(f"Itens: {itens}")

# 7. Removendo um Elemento com pop()
print("\n6. Removendo um Elemento com pop():")
profissao_removida = dicionario.pop('profissao', None)
print(f"Profissão removida: {profissao_removida}")
print(f"Dicionário após remoção: {dicionario}")

# 8. Removendo o Último Elemento com popitem()
print("\n7. Removendo o Último Elemento com popitem():")
item_removido = dicionario.popitem()
print(f"Último item removido: {item_removido}")
print(f"Dicionário após remoção: {dicionario}")

# 9. Atualizando o Dicionário com update()
print("\n8. Atualizando o Dicionário com update():")
novos_itens = {'profissao': 'Desenvolvedor', 'cidade': 'Cidade B'}
dicionario.update(novos_itens)
print(f"Dicionário atualizado: {dicionario}")

# 10. Atualizando o Dicionário com update() e Valor por Chave
print("\n9. Atualizando o Dicionário com update() e Valor por Chave:")
dicionario.update(nome="Novo Nome")
print(f"Dicionário após atualização do nome: {dicionario}")

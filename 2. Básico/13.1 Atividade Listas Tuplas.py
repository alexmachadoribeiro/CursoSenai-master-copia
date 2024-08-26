import requests
import json


url = "https://consultreds.com/dados/"
headers = {'Content-type': 'application/json'}

request = requests.get(url=url, headers=headers)
response = json.loads(request.content)

lista = response['dados']
lista = json.loads(lista)

print(f"Lista de números: {lista} - type: {type(lista)}")


# Ordene a lista do maior para o menor
lista.sort(reverse=True)

# Remova os três primeiros elementos da lista
del lista[:3]

# Multiplique cada elemento da lista por 2
for enum, item in enumerate(lista):
    print(f"Índice: {enum} - valor {item}")
    lista[enum] = lista[enum] * 2


# Remova o último elemento da lista
lista.pop()

# Altere o primeiro elemento da lista para 0
lista[0] = 0

# Adicione 3 ao final da lista
lista.append(3)

# Obtenha os elementos de índice 2 a 5 da lista
lista = lista[2:6]

# Some todos os elementos da lista
soma = 0
for item in lista:
    soma = soma + item
print(lista)
print(f"Soma: {soma}")

print(f"Soma dos elementos da lista: {soma}")
print(lista)


# Transforme a lista em uma tupla
tupla = tuple(lista)
print(f"Tupla: {tupla} - type: {type(tupla)}")

tupla[1] = 4
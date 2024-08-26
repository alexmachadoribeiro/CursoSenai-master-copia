import requests
import traceback
import json

# Requisição GET na URL https://consultreds.com/dados/
url = "https://consultreds.com/api/produtos/"
headers = {'Content-type': 'application/json'}

request = requests.get(url=url, headers=headers)

response = json.loads(request.content)
print(response)

dados_json = response['dados'].replace("'", '"')

response1 = json.loads(dados_json)

novo_dicionario = json.dumps(response1)
# print(novo_dicionario)
# print(type(novo_dicionario))

import requests
import json
import pandas as pd

from credenciais import APP_KEY, APP_SECRET

app_key = APP_KEY
app_secret = APP_SECRET
call = "ListarProdutos"
reg_pg = 14

dados_completos = []

url = "https://app.omie.com.br/api/v1/geral/produtos/"
headers = {'Content-type': 'application/json'}

# Json válido
data = '{"call":"' + str(call) + '","app_key":"' + str(app_key) + '","app_secret":"' + str(app_secret) + '","param":[{"pagina":1,"registros_por_pagina":' + str(reg_pg) + ', "apenas_importado_api":"N","filtrar_apenas_omiepdv":"N"}]}'

request = requests.post(url=url, data=data, headers=headers)

# Retorno completo do json
javascript = json.loads(request.content)
# print(javascript)
# Retorno dos lançamentos
total_paginas = javascript['total_de_paginas']
print(f"Total de páginas: {total_paginas}")

# for pagina in range(total_paginas):
#     pagina += 1
#     headers = {'Content-type': 'application/json'}
#     parametros_paginado = '"param":[{"pagina":' + str(pagina) +',"registros_por_pagina":' + str(reg_pg) + ', "apenas_importado_api":"N","filtrar_apenas_omiepdv":"N"}] }'
#     data_paginada = '{"call":"' + str(call) + '"'\
#               ',"app_key":" ' + app_key + '",'\
#               '"app_secret":"' + app_secret + '"' \
#               ',' + parametros_paginado
#
#     request_paginada = requests.post(url=url, headers=headers, data=data_paginada)
#     conteudo_paginado = json.loads(request_paginada.content)
#     # print(conteudo_paginado)
#     dados_paginados = conteudo_paginado['produto_servico_cadastro']
#     dados_completos += dados_paginados
#
# # print(dados_completos)
# produtos_omie = pd.DataFrame(dados_completos)
# print(produtos_omie)
#
# produtos_omie.to_excel("produtos_omie.xlsx", index=False)

informacoes = javascript['produto_servico_cadastro']

for item in informacoes:
    print(f"O market place do produto {item['descricao']} - {item['recomendacoes_fiscais']['market_place']}")
    print()

print(f"Quantidade de produtos: {len(informacoes)}")
import hashlib
import requests
import datetime
from pprint import pprint as pp
import pandas as pd

timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
pub_key = '4e08cfbc9a8ee4d1459f8b3c79c6a4cd'
priv_key = 'bc890d012d514ec6b7e9fff76e03bd72dae1c1fa'

dados_completos = []


def hash_params():
    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params


params = {'ts': timestamp, 'apikey': pub_key, 'hash': hash_params()}
res = requests.get('https://gateway.marvel.com:443/v1/public/characters',
                   params=params)

results = res.json()
# pp(results)

listagem = results['data']['results']

for item in listagem:
    list_items = item['comics']['items']
    for objeto in list_items:
        dados_completos.append(objeto)


# pp(dados_completos)
# pp(type(dados_completos))


df = pd.DataFrame(dados_completos)
df.to_excel("dados_marvel.xlsx", index=False)
print(df.info())

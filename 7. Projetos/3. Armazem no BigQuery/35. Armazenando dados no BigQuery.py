# pip install --upgrade google-cloud-bigquery
# pip install google-oauth
import traceback

from google.oauth2 import service_account

# pip install pandas-gbq
# Documentação Pandas GBQ: https://pandas-gbq.readthedocs.io/en/latest/
import pandas as pd
pd.options.display.width = 0
import pandas_gbq as pd_gbq  # Importe como pd_gbq para evitar conflitos com pandas

from arquivo_json import arquivo_json


class Armazem:
    def __init__(self, df_dict, projeto, conjunto, tabela):
        self.credentials = service_account.Credentials.from_service_account_info(arquivo_json)
        self.df_dict = df_dict
        self.projeto = projeto
        self.conjunto = conjunto
        self.tabela = tabela

    def armazena(self):
        # Armazenando o dataframe para os dataframes
        try:
            # Reset nos índices
            dados = self.df_dict.reset_index()

            # Convertendo séries em string
            dados = dados.astype(str)

            # Convertendo para feather
            dados.to_feather('df_feather.feather')

            # Redefinindo o index
            dados.set_index('index', inplace=True)
            dados = dados.reset_index(drop=True)

            # Exportando dados para o BigQuery
            pd_gbq.to_gbq(dados, credentials=self.credentials,
                                 project_id=self.projeto,
                                 destination_table=f"{self.conjunto}.{self.tabela}",
                                 if_exists='replace')
            return f"<<< Tabela {self.tabela} registrada / atualizada com sucesso no BigQuery >>>"

        except Exception as e:
            traceback.print_exc()
            print(e)
            return f"Erro na armazenagem dos dados da tabela {self.tabela}"

    def leitura(self):
        # Leitura dos dados do BigQuery
        try:
            # Consulta SQL
            query = f"SELECT * FROM {self.projeto}.{self.conjunto}.{self.tabela}"
            # Leitura dos dados
            df = pd_gbq.read_gbq(query, project_id=self.projeto, credentials=self.credentials)
            print(df)
            print(df.info())
            return df
        except Exception as e:
            traceback.print_exc()
            print(e)
            return f"Erro na leitura dos dados da tabela {self.tabela}"


if __name__ == '__main__':
    df_dict = pd.read_excel('produtos_omie.xlsx')
    armazem = Armazem(df_dict=df_dict, projeto='senaicurso', conjunto='dados', tabela='produtos_omie')
    armazem.armazena()
    # armazem.leitura()
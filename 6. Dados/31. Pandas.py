# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Uso do Pandas em Python

Este arquivo apresenta diversos exemplos do uso da biblioteca Pandas em Python para manipulação e análise de dados.

Certifique-se de ter o Pandas instalado usando o seguinte comando:
pip install pandas

Instale o Jupyter Notebook usando o seguinte comando:
    pip install jupyter

Para iniciar o Jupyter Notebook, execute o seguinte comando:
    jupyter notebook
"""

import pandas as pd

print(pd.Series([1, 2, 3, 4], index=['num1', 'num2', 'num3', 'num4']))
# Exemplo 1: Criando um DataFrame a partir de uma lista de dicionários
def exemplo_criar_dataframe():
    dados = [
        {"Nome": "Alice", "Idade": 25, "Cidade": "São Paulo"},
        {"Nome": "Bob", "Idade": 30, "Cidade": "Rio de Janeiro"},
        {"Nome": "Charlie", "Idade": 22, "Cidade": "Belo Horizonte"}
    ]

    df = pd.DataFrame(dados)


# Exemplo 2: Carregando dados de um arquivo CSV
def exemplo_carregar_csv():
    # Suponha que o arquivo "dados.csv" contém dados em formato CSV
    df = pd.read_csv("dados.csv")
    print("\nExemplo 2:")
    print(df)


# Exemplo 3: Indexação e Seleção de Dados
def exemplo_indexacao_selecao():
    dados = {
        "Nome": ["Alice", "Bob", "Charlie"],
        "Idade": [25, 30, 22],
        "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
    }

    df = pd.DataFrame(dados, index=["A", "B", "C"])

    # Selecionando coluna pelo nome
    nome_coluna = df["Nome"]
    print("\nExemplo 3.1:")
    print(nome_coluna)

    # Selecionando linhas pelo índice
    linha_a = df.loc["A"]
    print("\nExemplo 3.2:")
    print(linha_a)

    # Selecionando célula específica
    celula = df.at["B", "Idade"]
    print("\nExemplo 3.3:")
    print(celula)


# Exemplo 4: Adicionando e Removendo Colunas
def exemplo_adicionar_remover_colunas():
    dados = {
        "Nome": ["Alice", "Bob", "Charlie"],
        "Idade": [25, 30, 22],
        "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
    }

    df = pd.DataFrame(dados)

    # Adicionando uma nova coluna
    df["Profissao"] = ["Engenheira", "Desenvolvedor", "Estudante"]
    print("\nExemplo 4.1:")
    print(df)

    # Removendo uma coluna
    df = df.drop("Idade", axis=1)
    print("\nExemplo 4.2:")
    print(df)


# Exemplo 5: Operações Estatísticas e Agregações
def exemplo_operacoes_estatisticas():
    dados = {
        "Nota1": [90, 85, 88, 92],
        "Nota2": [88, 89, 84, 90],
        "Nota3": [87, 90, 82, 88]
    }

    df = pd.DataFrame(dados)

    # Calculando a média das notas por aluno
    df["Media"] = df.mean(axis=1)
    print("\nExemplo 5.1:")
    print(df)

    # Calculando a média das notas de toda a turma
    media_turma = df.mean()
    print("\nExemplo 5.2:")
    print(media_turma)


# Exemplo 6: Filtrando Dados
def exemplo_filtrar_dados():
    dados = {
        "Nome": ["Alice", "Bob", "Charlie"],
        "Idade": [25, 30, 22],
        "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
    }

    df = pd.DataFrame(dados)

    # Filtrando dados com base em uma condição
    menores_de_30 = df[df["Idade"] < 30]
    print("\nExemplo 6:")
    print(menores_de_30)


# Exemplo 7: Agrupamento e Contagem
def exemplo_agrupamento_contagem():
    dados = {
        "Nome": ["Alice", "Bob", "Charlie", "Alice", "Bob"],
        "Idade": [25, 30, 22, 25, 30],
        "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "São Paulo", "Rio de Janeiro"]
    }

    df = pd.DataFrame(dados)

    # Agrupando por idade e contando o número de ocorrências
    contagem_por_idade = df.groupby("Idade").size().reset_index(name="Contagem")
    print("\nExemplo 7:")
    print(contagem_por_idade)


# Exemplo 8: Mesclando DataFrames
def exemplo_mesclar_dataframes():
    dados1 = {
        "ID": [1, 2, 3],
        "Nome": ["Alice", "Bob", "Charlie"]
    }

    dados2 = {
        "ID": [2, 3, 4],
        "Cargo": ["Engenheira", "Desenvolvedor", "Estudante"]
    }

    df1 = pd.DataFrame(dados1)
    df2 = pd.DataFrame(dados2)

    # Mesclando DataFrames com base na coluna "ID"
    df_merged = pd.merge(df1, df2, on="ID")
    print("\nExemplo 8:")
    print(df_merged)


# Executar os Exemplos
if __name__ == "__main__":
    exemplo_criar_dataframe()
    exemplo_carregar_csv()
    exemplo_indexacao_selecao()
    exemplo_adicionar_remover_colunas()
    exemplo_operacoes_estatisticas()
    exemplo_filtrar_dados()
    exemplo_agrupamento_contagem()
    exemplo_mesclar_dataframes()

"""
URL: https://www.kaggle.com/datasets/yasserh/housing-prices-dataset?select=Housing.csv
LINK DO GOOGLE COLAB: https://colab.research.google.com/drive/1rcUiEzRmT0zQElB9QEQ5r4rDnHIfTr1h?usp=sharing
INSTALAÇÃO DO JUPYTER NOTEBOOK: https://jupyter.org/install
"""

import pandas as pd

# Carregando os dados
df = pd.read_csv("housing.csv")

# Exibindo as primeiras linhas do DataFrame
print(df.head())

# Exibindo informações sobre o DataFrame
print(df.info())

# Exibindo estatísticas descritivas
print(df.describe())

# Exibindo a média dos valores
print(df.mean())

# Exibindo a mediana dos valores de cada coluna
print(df.median())

# Exibindo a moda dos valores de cada coluna
print(df.mode())

# Exibindo a variância dos valores de cada coluna
# A variância é uma medida de dispersão que mostra o quão distantes os valores estão da média.
print(df.var())

# Exibindo o desvio padrão dos valores de cada coluna
# O desvio padrão é a raiz quadrada da variância e é uma medida de dispersão que mostra o quão distantes os valores estão da média.
print(df.std())

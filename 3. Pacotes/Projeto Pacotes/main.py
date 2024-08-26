import pandas as pd

df = pd.read_csv('housing.csv')

df.to_excel('housing.xlsx', index=False)
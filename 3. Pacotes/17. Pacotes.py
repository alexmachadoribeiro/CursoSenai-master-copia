# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Importação de Pacotes em Python

Este arquivo demonstra o uso de pacotes em Python, incluindo as instruções import, from, as e *.

1. Importando um Pacote
2. Importando um Módulo Específico
3. Importando com um Nome Diferente (as)
4. Importando Todas as Funções com *
5. Importando Funções ou Variáveis Específicas com from
"""

# 1. Importando um Pacote
import math

print("1. Importando um Pacote:")
raiz_quadrada = math.sqrt(25)
print(f"A raiz quadrada de 25 é {raiz_quadrada}.")

# 2. Importando um Módulo Específico
from datetime import datetime

print("\n2. Importando um Módulo Específico:")
data_atual = datetime.now()
print(f"A data e hora atual são: {data_atual}")

# 3. Importando com um Nome Diferente (as)
import pandas as pd

print("\n3. Importando com um Nome Diferente (as):")
dados = {'Nome': ['Alice', 'Bob', 'Charlie'], 'Idade': [25, 30, 35]}
df = pd.DataFrame(dados)
print("DataFrame criado:")
print(df)

# 4. Importando Todas as Funções com *
from random import *

print("\n4. Importando Todas as Funções com *:")
numero_aleatorio = randint(1, 100)
print(f"Número aleatório entre 1 e 100: {numero_aleatorio}")

# 5. Importando Funções ou Variáveis Específicas com from
from math import pow, pi

print("\n5. Importando Funções ou Variáveis Específicas com from:")
area_circulo = pow(5, 2) * pi
print(f"A área de um círculo com raio 5 é: {area_circulo}")

# 6. Instalando Pacotes com pip
# pip install pandas

# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Uso Avançado do Pacote datetime com Alias em Python

Este arquivo demonstra o uso avançado do pacote datetime importado como dt em Python.

1. Construindo uma Data Personalizada
2. Obtendo Componentes Específicos da Data e Hora
3. Somente Data, Somente Hora, Somente Minuto, etc.
"""

# Importando datetime com Alias
import datetime as dt

print("1. Construindo uma Data Personalizada:")
# Construindo uma data específica (ano, mês, dia, hora, minuto, segundo)
data_personalizada = dt.datetime(2025, 2, 15, 14, 30, 0)
print(f"Data Personalizada: {data_personalizada}")

# 2. Obtendo Componentes Específicos da Data e Hora
print("\n2. Obtendo Componentes Específicos da Data e Hora:")
ano = data_personalizada.year
mes = data_personalizada.month
dia = data_personalizada.day
hora = data_personalizada.hour
minuto = data_personalizada.minute
segundo = data_personalizada.second

print(f"Ano: {ano}")
print(f"Mês: {mes}")
print(f"Dia: {dia}")
print(f"Hora: {hora}")
print(f"Minuto: {minuto}")
print(f"Segundo: {segundo}")

# 3. Somente Data, Somente Hora, Somente Minuto, etc.
print("\n3. Somente Data, Somente Hora, Somente Minuto, etc.:")
# Somente Data
data_apenas = data_personalizada.date()
print(f"Somente Data: {data_apenas}")

# Somente Hora
hora_apenas = data_personalizada.time()
print(f"Somente Hora: {hora_apenas}")

# Somente Minuto e Segundo
minuto_segundo_apenas = data_personalizada.strftime("%M:%S")
print(f"Somente Minuto e Segundo: {minuto_segundo_apenas}")

# Data completa formatada
data_completa = data_personalizada.strftime("%d/%m/%Y %H:%M:%S")
print(f"Data Completa Formatada: {data_completa}")

# Obter a data atual
data_atual = dt.datetime.now()

# Verificar se a data atual é maior que a data personalizada
if data_atual > data_personalizada:
    print("\nA data atual é maior que a data personalizada.")
else:
    print("\nA data atual é menor que a data personalizada.")


# Somar ou diminuir datas
data_soma = data_atual + dt.timedelta(days=1)
data_subtrai = data_atual - dt.timedelta(days=1, hours=24)
import datetime as dt

data_hora_atual = dt.datetime.now()
response = data_hora_atual.strftime("%m-%d-%Y")
print(response)


def forma_data(ano, mes, dia):
    ano = int(ano)
    mes = int(mes)
    dia = int(dia)

    data = dt.datetime(year=ano, month=mes, day=dia)

    return data


ano = input("Digite o ano: ")
mes = input("Digite o mês: ")
dia = input("Digite o dia: ")

data_usuario = forma_data(ano=ano, mes=mes, dia=dia)

diferenca = data_hora_atual.year - data_usuario.year
print(f"A diferença de datas é de {diferenca} anos")

data_especifica = dt.datetime(year=1985, month=3, day=24)
print(f"Data específica: {data_especifica}")
print(type(data_especifica))

print(data_especifica.date())
print(data_especifica.time())

lista_datas = [
    dt.datetime(year=1985, month=3, day=24),
    dt.datetime(year=1990, month=4, day=12),
    dt.datetime(year=1995, month=5, day=14),
    dt.datetime(year=2000, month=5, day=27),
    dt.datetime(year=2005, month=1, day=12),
]

print(lista_datas)
for data in lista_datas:
    print(data - dt.timedelta(days=1, seconds=50))
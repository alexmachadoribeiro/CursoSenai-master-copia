# -*- coding: utf-8 -*-

from classe import CarrosNissan

livina = CarrosNissan(versao="SL", nome="Livina", motor="2.0")

livina.set_ligar()

try:
    livina.set_motor("2.2")
except:
    pass

print(livina)

versa = CarrosNissan.criar_carro(nome="Versa", motor="1.0", versao="SV",
                                 motores_disponiveis=["1.0", "1.6", "2.0", "3.0"],
                                 ligado=False)

print(versa)

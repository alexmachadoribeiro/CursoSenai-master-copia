# -*- coding: utf-8 -*-
"""As classes se relacionam, mas podem existir independentemente uma da outra"""


class CarrosNissan:
    marca = "Nissan"

    def __init__(self, nome, fabrica=None):
        self.nome = nome
        self.fabrica = fabrica

        if fabrica:
            fabrica.transferir_carro(self)

    def __str__(self):
        if not self.fabrica:
            return f"{self.marca} {self.nome} não vinculado a uma fábrica"
        else:
            return f"{self.marca} {self.nome} fabricado no {self.fabrica.nome}"


class FabricaNissan:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

    def transferir_carro(self, carro):
        if carro not in self.carros:
            self.carros.append(carro)
            carro.fabrica = self

    def __str__(self):
        return f"Fabrica {self.nome} com os carros: {', '.join([carro.nome for carro in self.carros])}"


if __name__ == "__main__":
    fabricaBrasil = FabricaNissan("Brasil")
    fabricaJapao = FabricaNissan("Japão")
    fabricaEua = FabricaNissan("EUA")

    versa = CarrosNissan(nome="Versa", fabrica=fabricaBrasil)

    print(versa)

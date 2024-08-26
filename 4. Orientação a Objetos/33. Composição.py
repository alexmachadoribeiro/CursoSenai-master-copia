# -*- coding: utf-8 -*-
"""Uma classe contém outra classe como um de seus campos."""


class Endereco:
    def __init__(self, rua, cidade, estado):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado

    def obter_endereco_completo(self):
        return f"{self.rua}, {self.cidade}, {self.estado}"


class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco  # Composição: Pessoa tem um Endereco

    def obter_info_pessoal(self):
        return f"{self.nome}, {self.idade} anos, mora em {self.endereco.obter_endereco_completo()}"


# Exemplo de uso
endereco_pessoa1 = Endereco("Rua A", "Cidade X", "Estado Y")

pessoa1 = Pessoa("Alice", 25, endereco_pessoa1)

print(pessoa1.obter_info_pessoal())

print(pessoa1.endereco.rua)
print(pessoa1.endereco.cidade)
print(pessoa1.endereco.estado)

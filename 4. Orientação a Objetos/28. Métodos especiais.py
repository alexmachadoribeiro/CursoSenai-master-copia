# -*- coding: utf-8 -*-

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def __str__(self):
        return f"O nome desta pessoa é {self.nome} e a idade é {self.idade}"

    def __repr__(self):
        return f"Pessoa('{self.nome}', {self.idade})"


# Exemplos de Uso
if __name__ == "__main__":
    pessoa = Pessoa(nome="Alice", idade=30)
    print(str(pessoa))  # Chama o __str__
    print(repr(pessoa))  # Chama o __repr__

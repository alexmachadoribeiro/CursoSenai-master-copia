# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Aspectos Básicos da Orientação a Objetos em Python

Este arquivo apresenta os aspectos básicos da orientação a objetos em Python.

1. Definindo uma Classe
2. Método __init__
3. Métodos em uma Classe
4. Atributos de Instância
5. Utilizando a Referência 'self'
"""


# 1. Definindo uma Classe
class Pessoa:
    pass  # 'pass' é usado para indicar que a classe está vazia, mas você pode adicionar membros posteriormente


# 2. Método __init__
class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano


# 3. Métodos em uma Classe
class Cachorro:
    def latir(self):
        return "Woof!"


# 4. Atributos de Instância
class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


# 5. Utilizando a Referência 'self'
class Circulo:
    pi = 3.14  # Atributo de Classe

    def __init__(self, raio):
        self.raio = raio  # Atributo de Instância

    def calcular_area(self):
        return self.pi * (self.raio ** 2)


# Exemplos de Uso
if __name__ == "__main__":
    # 1. Definindo uma Classe
    pessoa = Pessoa()

    # 2. Método __init__
    carro = Carro(modelo="Civic", ano=2022)

    # 3. Métodos em uma Classe
    cachorro = Cachorro()
    print(cachorro.latir())

    # 4. Atributos de Instância
    aluno = Aluno(nome="Maria", idade=25)
    print(f"Nome: {aluno.nome}, Idade: {aluno.idade}")

    # 5. Utilizando a Referência 'self'
    circulo = Circulo(raio=5)
    area = circulo.calcular_area()
    print(f"Área do círculo: {area}")

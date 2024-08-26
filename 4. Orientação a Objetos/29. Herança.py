# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Herança em Python

Este arquivo apresenta o conceito de herança em programação orientada a objetos em Python.

1. Definindo uma Classe Base
2. Herança Simples
3. Sobrescrita de Métodos
4. Chamando o Método da Classe Base
5. Adicionando Atributos à Subclasse
"""


# 1. Definindo uma Classe Base
class Animal:
    def __init__(self, nome, raca=None):
        self.nome = nome
        self.raca = raca

    def fazer_som(self):
        pass


# 2. Herança Simples
class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!" # Polimorfismo


# 3. Sobrescrita de Métodos
class Gato(Animal):
    def fazer_som(self):
        return "Miau!"


# 4. Chamando o Método da Classe Base
class Pato(Animal):
    def fazer_som(self):
        som_animal = super().fazer_som()
        return f"Quack! ({som_animal})"


# 5. Adicionando Atributos à Subclasse
class Cavalo(Animal):
    def __init__(self, nome, raca, cor):
        super().__init__(nome=nome, raca=raca)
        self.cor = cor

    def fazer_som(self):
        return "Relincho!"

    def cavalgar(self):
        return "cavalgando..."


class Carro:
    pneus = True
    lataria = True

    def __init__(self, chaci, motor):
        self.__chaci = chaci
        self.__motor = motor

    def get_motor(self):
        return self.__motor

    def get_chaci(self):
        return self.__chaci

    def set_chaci(self, novo_chaci):
        self.__chaci = novo_chaci

    def set_motor(self, novo_motor):
        self.__motor = novo_motor

    def __str__(self):
        return f"O chaci do carro é {self.__chaci}, o motor é {self.__motor}, possui pneus: {self.pneus}, possui lataria: {self.lataria}"


class Versa(Carro):
    nome = "Versa"

    def __init__(self, chaci, motor, versao):
        super().__init__(chaci=chaci, motor=motor)
        self.versao = versao

    def __str__(self):
        return f"""Este {self.nome} tem o chaci {super().get_chaci()}, o motor {super().get_motor()} e a versão dele é {self.versao}"""


# Exemplos de Uso
if __name__ == "__main__":
    # 2. Herança Simples
    rex = Cachorro(nome="Rex")
    print(f"{rex.nome} faz: {rex.fazer_som()}")

    # 3. Sobrescrita de Métodos
    whiskers = Gato(nome="Whiskers")
    print(f"{whiskers.nome} faz: {whiskers.fazer_som()}")

    # 4. Chamando o Método da Classe Base
    donald = Pato(nome="Donald")
    print(f"{donald.nome} faz: {donald.fazer_som()}")

    # 5. Adicionando Atributos à Subclasse
    spirit = Cavalo(nome="Spirit", cor="Marrom", raca="Manga Larga")
    print(f"Nome: {spirit.nome} (cor: {spirit.cor} - raça: {spirit.raca}) faz: {spirit.fazer_som()} e {spirit.cavalgar()}")

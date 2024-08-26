# -*- coding: utf-8 -*-
"""
Arquivo de Exemplo: Encapsulamento em Python

Este arquivo apresenta o conceito de encapsulamento em programação orientada a objetos em Python.

1. Atributos Privados
2. Métodos Privados
3. Propriedades
"""


# 1. Atributos Privados
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular  # Atributo privado, só alterado mediante métodos específicos
        self.__saldo = saldo      # Atributo privado

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor


# 2. Métodos Privados
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__ligado = False  # Atributo privado

    def __verificar_combustivel(self):
        return "Combustível Suficiente" if self.__ligado else "Carro desligado"

    def ligar(self):
        self.__ligado = True
        print("Carro ligado.")

    def desligar(self):
        self.__ligado = False
        print("Carro desligado.")

    def status_combustivel(self):
        return self.__verificar_combustivel()


if __name__ == "__main__":
    # 1. Atributos Privados
    conta = ContaBancaria(titular="João", saldo=1000)
    print(f"Saldo inicial: {conta.get_saldo()}")
    conta.depositar(500)
    conta.sacar(200)
    print(f"Saldo final: {conta.get_saldo()}")

    # 2. Métodos Privados
    carro = Carro(marca="Toyota", modelo="Corolla")
    carro.ligar()
    print(f"Status do Combustível: {carro.status_combustivel()}")
    carro.desligar()
    print(f"Status do Combustível: {carro.status_combustivel()}")

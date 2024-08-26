# -*- coding: utf-8 -*-

class CarrosNissan:
    marca = "Nissan"
    motores_disponiveis = ["1.0", "1.6", "2.0"]

    def __init__(self, nome, motor, versao, ligado=False):
        self.__nome = nome  # protected
        self.__motor = motor  # private motores: 1.0, 1.6 e 2.0
        self._versao = versao
        self.__ligado = ligado

    @classmethod
    def altera_marca(cls, nova_marca):
        cls.marca = nova_marca

    @classmethod
    def criar_carro(cls, nome, motor, versao, motores_disponiveis, ligado=False):
        instance = cls(nome, motor, versao, ligado)
        instance.motores_disponiveis = motores_disponiveis
        return instance

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if novo_nome:
            self.__nome = novo_nome
        else:
            print("O nome do carro não pode ser nulo")

    @nome.deleter
    def nome(self):
        resposta = input("Tem certeza que deseja apagar este registro? Digite S para sim e N para não: ")
        if resposta == "S":
            self.__nome = ""
        else:
            print("Voltando para a página inicial")

    def set_ligar(self):
        self.__ligado = True

    def set_desligar(self):
        self.__ligado = False

    def get_ligado(self):
        return self.__ligado

    def get_motor(self):
        return self.__motor

    def set_motor(self, novo_motor):
        if novo_motor not in self.motores_disponiveis:
            raise "Motor não disponível para a Nissan"
        else:
            self.__motor = novo_motor

    def __str__(self):
        return f"{self.marca} - {self.__nome} {self._versao} {self.__motor} (Motores disponíveis: {self.motores_disponiveis}"

    def __repr__(self):
        return f"Representação da instância: {self.__nome}"

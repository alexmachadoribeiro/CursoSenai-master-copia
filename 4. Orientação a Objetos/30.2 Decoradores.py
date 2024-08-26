# -*- coding: utf-8 -*-
import random


# 3. Propriedades
class Pessoa:
    tipo = "humano"

    def __init__(self, nome, idade):
        self.__nome = nome  # Atributo privado
        self.__idade = idade  # Atributo privado
        self.ano = 2021  # Atributo privado

    @classmethod  # Método de classe: pode ser usado para construtores alternativos ou alterar atributos da classe
    def alterar_tipo(cls, novo_tipo):
        cls.tipo = novo_tipo

    @classmethod  # Construtor alternativo
    def criar_pessoa(cls, nome, idade, ano, tipo):
        instance = cls(nome, idade)
        instance.ano = ano
        instance.tipo = tipo
        return instance

    @staticmethod  # Método estático: não depende de instâncias
    def embaralhar_nome(nome):
        nome = list(nome)
        random.shuffle(nome)
        return "".join(nome)

    # Transformar método em propriedade - somente leitura sem parênteses
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if novo_nome:
            self.__nome = novo_nome
        else:
            print("Nome não pode ser vazio.")

    @property
    def idade(self):
        return self.__idade

    @idade.setter  # Pode ser usado quando existe uma propriedade de mesmo nome, é chamado sempre que for setado um valor
    def idade(self, nova_idade):
        if nova_idade > 0:
            self.__idade = nova_idade
        else:
            raise ValueError("Idade deve ser um valor positivo.")

    @idade.deleter  # Pode ser usado quando existe uma propriedade de mesmo nome, é chamado sempre que for deletado um valor
    def idade(self):
        resposta = input("Tem certeza que deseja deletar a idade? (s/n) ")
        if resposta == "s":
            del self.__idade


if __name__ == "__main__":
    # 3. Propriedades
    pessoa = Pessoa(nome="Alice", idade=30)
    print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}, Tipo: {pessoa.tipo}, Ano: {pessoa.ano}")
    pessoa.idade = 25
    pessoa.alterar_tipo("pessoa")

    # del pessoa.idade
    print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}, Tipo: {pessoa.tipo}, Ano: {pessoa.ano}")

    pessoa2 = Pessoa.criar_pessoa(nome="Maria", idade=25, ano=2022, tipo="robô")
    pessoa2.nome = pessoa2.embaralhar_nome(pessoa2.nome)
    print(f"Nome2: {pessoa2.nome}, Idade2: {pessoa2.idade}, Tipo2: {pessoa2.tipo}, Ano: {pessoa2.ano}")

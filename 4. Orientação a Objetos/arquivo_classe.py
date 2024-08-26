# -*- coding: utf-8 -*-

def naozero(funcao):
    def validar(num1, num2):
        if num1 == 0 or num2 == 0:
            return "Nenhum número pode ser zero"
        return funcao(num1, num2)
    return validar


@naozero
def somar(num1, num2):
    return num1 + num2


print(somar(8,0))

def validar(funcao):
    def verifica_zero(*args):
        if 0 in args:
            return 'Não pode ter zero'
        return funcao(*args)
    return verifica_zero


@validar
def somar(*args):
    return sum(args)


print(somar(1, 12, 4, 4, 5))

print(validar(somar)(1, 12, 4, 0, 5))

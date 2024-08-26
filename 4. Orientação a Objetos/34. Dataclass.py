from dataclasses import dataclass


@dataclass
class Person:
    nome: str
    idade: int


rodrigo = Person(nome="Rodrigo", idade=25)
alex = Person(nome="Rodrigo", idade=25)

print(rodrigo)
print(f"Este objeto se refere ao {rodrigo.nome} de idade {rodrigo.idade}")

# -*- coding: utf-8 -*-
"""As classes se relacionam, mas podem existir independentemente uma da outra"""


class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.cursos_inscritos = []  # Lista para armazenar os cursos associados ao aluno

    def inscrever_curso(self, curso):
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)
            curso.adicionar_aluno(self)  # Associa o aluno ao curso

    def listar_cursos(self):
        lista = []
        for curso in self.cursos_inscritos:
            lista.append(curso.nome)
        return lista


class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos_inscritos = []  # Lista para armazenar os alunos associados ao curso

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos_inscritos:
            self.alunos_inscritos.append(aluno)
            aluno.inscrever_curso(self)  # Associa o curso ao aluno

    def listar_alunos(self):
        lista = []
        for aluno in self.alunos_inscritos:
            lista.append(aluno.nome)


# Exemplo de Uso
aluno1 = Aluno("João", "2021001")
aluno2 = Aluno("Maria", "2021002")

curso1 = Curso("Matemática")
curso2 = Curso("História")

aluno1.inscrever_curso(curso1)
aluno1.inscrever_curso(curso2)
aluno2.inscrever_curso(curso1)

print(f"{aluno1.nome} está inscrito nos cursos: {aluno1.listar_cursos()}")
print(f"{aluno2.nome} está inscrito nos cursos: {aluno2.listar_cursos()}")

print(f"\nNo curso {curso1.nome} estão os alunos: {curso1.listar_alunos()}")
print(f"No curso {curso2.nome} estão os alunos: {curso2.listar_alunos()}")

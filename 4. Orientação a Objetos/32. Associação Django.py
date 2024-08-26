from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    data_publicacao = models.DateField()

    def __str__(self):
        return self.titulo


class Leitor(models.Model):
    nome = models.CharField(max_length=100)
    livros_lidos = models.ManyToManyField(Livro)

    def __str__(self):
        return self.nome


class Biblioteca(models.Model):
    nome = models.CharField(max_length=150)
    responsavel = models.OneToOneField(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

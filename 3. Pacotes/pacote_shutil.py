# -*- coding: utf-8 -*-
import os
import chardet

"""
- No diretório 3. Pacotes existem os diretórios Downloads e Quarentena.
- Crie um função que faça a leitura de todas as subpastas do diretório Downloads e leia o conteúdo de cada arquivo.
- Caso o script encontre as palavras "troia", "trojan", "malware" ou "vírus" em qualquer arquivo, mova o arquivo para o
diretório Quarentena.
- Após 2 segundos apague todos os arquivos do diretório Quarentena, inclusive o diretório.
"""


# Faz a leitura dos diretórios / arquivos da pasta Downloads
class VerificacaoArquivos:
    def __init__(self):
        ...

    def leitura_downloads(self, diretorio):
        pastas = os.listdir(diretorio)
        return pastas

    def leitura_arquivo(self, arquivo):
        dados = ""
        codigo = self.codificacao_arquivo(arquivo)
        with open(arquivo, 'r', encoding=codigo) as arquivo:
            conteudo = arquivo.read()
            dados = conteudo

        return dados

    def antivirus(self, conteudo):
        verificacoes = ["troia", "trojan", "malware", "vírus"]
        infectado = False

        for verificacao in verificacoes:
            if verificacao in conteudo:
                infectado = True
                break

        return infectado

    def codificacao_arquivo(self, diretorio_arquivo):
        codificacao = ""
        with open(diretorio_arquivo, 'rb') as f:
            result = chardet.detect(f.read())

        codificacao = result['encoding']
        return codificacao


if __name__ == "__main__":
    verificacao = VerificacaoArquivos()
    response = verificacao.codificacao_arquivo('Downloads/Outros/vida_nova.txt')
    print(response)